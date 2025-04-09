import subprocess
import xml.etree.ElementTree as ET
from tqdm import tqdm
import sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from pathlib import Path
import plotly.express as px

def analyze_opus_bitrate(audio_path):
    # FFprobe komutu
    cmd = [
        'ffprobe',
        '-hide_banner',
        '-show_packets',
        '-select_streams', 'a:0',
        '-show_entries', 'packet=size,pts_time,duration_time',
        '-loglevel', 'error',
        '-print_format', 'xml',
        str(audio_path)
    ]
    
    # FFprobe'u çalıştır
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("FFprobe hatası:", result.stderr)
        return
    
    try:
        root = ET.fromstring(result.stdout)
    except ET.ParseError as e:
        print(f"XML parse hatası: {e}")
        return
    
    # Paketleri işle
    packets = root.findall('.//packet')
    if not packets:
        print("Ses verisi bulunamadı!")
        return
    
    # Veri toplama
    data = {
        'timestamp': [],
        'bitrate': [],
        'size': [],
        'duration': []
    }
    
    print(f"\nAnaliz edilen paket sayısı: {len(packets)}")
    progress = tqdm(packets, unit='packet', ncols=80)
    
    last_pts = None
    for packet in progress:
        try:
            # Temel verileri al
            size = int(packet.get('size', 0))
            pts = float(packet.get('pts_time', 0))
            duration = float(packet.get('duration_time', 0))
            
            # Süre hesaplama
            if duration <= 0 and last_pts is not None:
                duration = pts - last_pts
            if duration <= 0:
                duration = 0.020  # Varsayılan Opus frame süresi
                
            # Bitrate hesapla
            bitrate = (size * 8) / duration if duration > 0 else 0
            
            # Verileri kaydet
            data['timestamp'].append(pts)
            data['bitrate'].append(bitrate)
            data['size'].append(size)
            data['duration'].append(duration)
            
            last_pts = pts
            
        except Exception as e:
            continue
    
    # Veri kontrolü
    if not data['timestamp']:
        print("İşlenebilir veri bulunamadı!")
        return
    
    # DataFrame oluştur
    df = pd.DataFrame(data)
    df['bitrate_kbps'] = df['bitrate'] / 1000
    
    # Dosya adı temeli
    base_name = Path(audio_path).stem
    output_dir = Path.cwd()
    
    # 1. CSV Kaydetme
    csv_path = output_dir / f"{base_name}_bitrate.csv"
    try:
        df.to_csv(csv_path, index=False)
        print(f"\nCSV kaydedildi: {csv_path}")
    except Exception as e:
        print(f"\nCSV kaydetme hatası: {str(e)}")
    
    # 2. Interaktif HTML Grafik
    html_path = output_dir / f"{base_name}_interactive.html"
    try:
        fig = px.line(df, 
                     x='timestamp', 
                     y='bitrate_kbps',
                     title='Opus Bitrate Analizi',
                     labels={'timestamp':'Zaman (s)', 'bitrate_kbps':'Bitrate (kbps)'},
                     hover_data={
                         'timestamp': ':.3f',
                         'bitrate_kbps': ':.2f',
                         'size': True,
                         'duration': ':.3f'
                     })
        fig.write_html(html_path)
        print(f"HTML grafik kaydedildi: {html_path}")
    except Exception as e:
        print(f"HTML grafik hatası: {str(e)}")
    
    # 3. Vektörel Grafikler (SVG + PNG)
    try:
        plt.figure(figsize=(15, 5))
        plt.plot(df['timestamp'], df['bitrate_kbps'], 
                alpha=0.7, linewidth=0.8, color='navy')
        plt.title(f'Opus Bitrate Dağılımı - {base_name}', pad=20)
        plt.xlabel('Zaman (saniye)', labelpad=15)
        plt.ylabel('Bitrate (kbps)', labelpad=15)
        plt.grid(True, alpha=0.2)
        
        # SVG Kaydet
        svg_path = output_dir / f"{base_name}_plot.svg"
        plt.savefig(svg_path, format='svg', bbox_inches='tight')
        print(f"SVG grafik kaydedildi: {svg_path}")
        
        # PNG Kaydet (Yüksek Çözünürlüklü)
        png_path = output_dir / f"{base_name}_bitrate.png"
        plt.savefig(png_path, format='png', dpi=300, bbox_inches='tight')
        print(f"PNG grafik kaydedildi: {png_path}")
        
        plt.close()
        
    except Exception as e:
        print(f"Grafik kaydetme hatası: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Kullanım: python opus_bitrate_analyzer.py <dosya.opus>")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    if not input_file.exists():
        print(f"Hata: {input_file} bulunamadı!")
        sys.exit(2)
    
    analyze_opus_bitrate(input_file)