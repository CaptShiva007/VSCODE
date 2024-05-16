import os,wmi

w=wmi.WMI()

admins=None

for group in w.Win32_Group():
    if group.Name=="Administrators":
        admins=[a.name for a in group.associators(wmi_result_class="Win32_UserAccount")]

for user in w.Win32_UserAccount():
    print("Username: %s"% user.Name)
    print("Administrator: %s" % (user.Name in admins))
    print("Disabled: %s" % user.Disabled)
    print("Local: %s" % user.LocalAccount)
    print("Password changeable: %s" % user.PasswordChangeable)
    print("Password expires: %s" % user.PasswordExpires)
    print("Password required: %s" % user.PasswordRequired)
    print("\n")

print("Password Policy: ")
print(os.system("net accounts"))