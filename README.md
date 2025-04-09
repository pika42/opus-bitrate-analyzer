# opus-bitrate-analyzer
A python script that analyzes the bitrate-time of audio files created with the libopus codec in .opus format. opus bitrate analyzer


![Shivers_bitrate](https://github.com/user-attachments/assets/280522a9-0743-4fb6-8997-538aed995219)



The video bitrate analyzer was created using a python script:
https://github.com/InB4DevOps/bitrate-viewer/blob/main/_bitrate_analyzer.py

Thanks to [@InB4DevOps](https://github.com/InB4DevOps) 

Development is accelerated with the help of DeepSeek R1 DeepThink.

First it analyzes the opus file and creates a .csv table data file with bitrate - time columns.

This file creates a bitrate-time graph and saves it in .svg format.

It also saves in .png format.

Generates detailed bitrate-time graph in .html format for interactive and detailed graphing.

Requirements:

    Python 3.6+
    pip install -r requirements.txt
    FFprobe in your PATH.

System requirements:

ffmpeg>=4.0
ffprobe>=4.0

ffmpeg for Windows 11:

    choco install ffmpeg

Kullanım:

python opus_bitrate_analyzer_txt.py <file_name>.opus
