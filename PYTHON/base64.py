import base64

def encrypt(msg):
    enc_msg=base64.b64encode(msg.encode()).decode()
    return enc_msg

def decrypt(enc_msg):
    dec_msg=base64.b64decode(enc_msg).decode()
    return dec_msg

msg=input("Enter message to encrypt: ")
enc_msg=encrypt(msg)
print("Original Message: ",msg)
print("Encrypted Message: ",enc_msg)
encrypted_msg=input("Enter the message to decrypt: ")
dec_msg=decrypt(encrypted_msg)
print("Decrypted Message: ", dec_msg)