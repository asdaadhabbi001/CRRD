import subprocess
process=subprocess.Popen(["powershell.exe","Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False"])

process=subprocess.Popen(["powershell.exe","& {$P = $env:TEMP + '\chromeremotedesktophost.msi'; Invoke-WebRequest 'https://dl.google.com/edgedl/chrome-remote-desktop/chromeremotedesktophost.msi' -OutFile $P; Start-Process $P -Wait; Remove-Item $P}"])
process=subprocess.Popen(["powershell.exe","& "${Env:PROGRAMFILES(X86)}\Google\Chrome Remote Desktop\CurrentVersion\remoting_start_host.exe" --code="4/0AX4XfWg81Vod4fOfFCmVjnE_5KyVNcjETz8QQTP6mqpeWtT5dlCa8K2qVzxUT32SO_IMdw" --redirect-url="https://remotedesktop.google.com/_/oauthredirect" --name=$Env:COMPUTERNAME -pin=123456])
