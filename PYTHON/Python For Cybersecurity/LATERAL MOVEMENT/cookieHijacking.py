import sqlite3,os

profile="jpb273b5.default-release"
firefoxpath=os.path.join("C:\\Users\\shiva\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles",profile,"cookies.sqlite")

conn=sqlite3.connect(firefoxpath)
c=conn.cursor()
c.execute("SELECT * FROM moz_cookies")

data=c.fetchall()

cookies={
    ".amazon.com":["aws-userInfo","aws-creds"],
    ".google.com":["OSID","HSID","SID","SSID","APISID","SAPISID","LSID"],
    ".microsoftonline.com":["ESTAUTHPERSISTENT"],
    ".facebook.com":["c_user","cs"],
    ".onelogin.com":["sub_session_onelogin.com"],
    ".github.com":["user_session"],
    ".live.com":["RPSSecAuth"],
}

for cookie in data:
    for domain in cookie:
        if cookie[4].endswith(domain) and cookie[2] in cookies[domain]:
            print("%s %s %s" % (cookie[4],cookie[2],cookie[3][:20]))