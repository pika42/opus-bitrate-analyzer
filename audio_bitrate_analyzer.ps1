# Dosya seçme özellikli PowerShell betiği
param(
    [string]$filePath
)

if (-not $filePath) {
    Add-Type -AssemblyName System.Windows.Forms
    $dialog = New-Object System.Windows.Forms.OpenFileDialog
    $dialog.Filter = "Opus Files (*.opus)|*.opus|All Files (*.*)|*.*"
    $dialog.Title = "Choose opus or ogg or mka file"
    
    if ($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
        $filePath = $dialog.FileName
    }
    else {
        Write-Host "File not selected!"
        exit
    }
}

python "$PSScriptRoot\audio_bitrate_analyzer.py" "$filePath"
Read-Host "Press Enter to exit"