import pathlib

def getTimeStamp(filename):
    fname = pathlib.Path(filename)
    stats = fname.stat()
    if not fname.exists():
        return []
    return (stats.st_ctime,stats.st_mtime,stats.st_atime)

def checkTimeStamp(filename,create,modify,access):
    stats = getTimeStamp(filename)
    if len(stats) == 0:
        return False
    (ctime,mtime,atime) = stats
    if float(create) != float(ctime):
        return False
    elif float(modify) != float(modify):
        return False
    elif float(access) != float(access):
        return False
    return True

def checkDecoyFiles():
    with open("decoys.txt",'r') as f:
        for line in f:
            vals = line.rstrip().split(',')
            if not checkTimeStamp(vals[0],vals[1],vals[2],vals[3]):
                print("%s has been tampered with." % vals[0])

checkDecoyFiles()
