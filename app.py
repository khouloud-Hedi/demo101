import hashlib
msg = hashlib.shamd5(b"Hello World").digest()
print(msg)