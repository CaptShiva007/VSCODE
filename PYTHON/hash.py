import hashlib
import uuid

def hash_func(passwd):
    id = uuid.uuid4().hex
    return hashlib.sha256(id.encode()+passwd.encode()).hexdigest()+":"+id

def chk_passwd(hash_pass,user_pass):
    passwd, s=hash_pass.split(":")
    return passwd==hashlib.sha256(s.encode()+user_pass.encode()).hexdigest()

new_pass=input("Enter the old password: ")
hash_pass=hash_func(new_pass)
print("The hash string to store in database is: ",hash_pass)