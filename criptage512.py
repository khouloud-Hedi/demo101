import hashlib
msg = hashlib.512(b"Hello World").digest()
print(msg)