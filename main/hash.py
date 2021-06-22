from Crypto.Cipher import AES
from Crypto import Random
import base64
from hashlib import pbkdf2_hmac
import os

def hasher(key,passw):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key,AES.MODE_EAX,iv)
    encrypted = cipher.encrypt(bytes(passw))
    enc = base64.b64encode(iv+encrypted)
    return enc

def unhasher(key,hash):
    dec = base64.b64decode(hash)
    dec_hash = dec[16:]
    iv = dec[:16]
    cipher = AES.new(key,AES.MODE_EAX,iv)
    decrypted = cipher.decrypt(dec_hash)
    return decrypted

def pbkdf(passw,salt=None):
    if salt == None:
        salt = os.urandom(16)
    dk = pbkdf2_hmac('sha256', passw, salt, 100000, dklen=32)
    return dk,salt

