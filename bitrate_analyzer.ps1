# Dosya seçme özellikli PowerShell betiği
param(
    [string]$filePath
)

if (-not $filePath) {
    Add-Type -AssemblyName System.Windows.Forms
    $dialog = New-Object System.Windows.Forms.OpenFileDialog
    $dialog.Filter = "Opus Files (*.opus)|*.opus|All Files (*.*)|*.*"
    $dialog.Title = "Opus Dosyası Seçin"
    
    if ($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
        $filePath = $dialog.FileName
    }
    else {
        Write-Host "Dosya seçilmedi!"
        exit
    }
}

python "$PSScriptRoot\bitrate_analyzer.py" "$filePath"
Read-Host "Press Enter to exit"