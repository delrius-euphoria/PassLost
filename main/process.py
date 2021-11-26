from Crypto.Cipher import AES
from Crypto import Random
from base64 import b64encode, b64decode
from hashlib import pbkdf2_hmac, sha256
from os import urandom
import sqlite3

def encryptor(key,password):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key,AES.MODE_EAX,iv)
    encrypted = cipher.encrypt(password)
    enc = b64encode(iv+encrypted)
    
    return enc

def decryptor(key,encrypted):
    dec = b64decode(encrypted)
    dec_hash = dec[16:]
    iv = dec[:16]
    cipher = AES.new(key,AES.MODE_EAX,iv)
    decrypted = cipher.decrypt(dec_hash)
    
    return decrypted

def pbkdf(password,salt=None):
    if salt == None:
        salt = urandom(16)
    dk = pbkdf2_hmac('sha256', password, salt, 100000, dklen=32)
    
    return dk, salt

def hasher(pw):
    hashed = sha256(pw)
    
    return hashed.digest()

if __name__ == '__main__':
    pass 