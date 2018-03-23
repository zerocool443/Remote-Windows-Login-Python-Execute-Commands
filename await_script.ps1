import-module await
Start-AwaitSession
Send-AwaitCommand "netsh"
Send-AwaitCommand "wlan show profiles"
$text = (Receive-AwaitResponse)
$text
Stop-AwaitSession