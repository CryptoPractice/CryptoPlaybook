from Crypto.Cipher import DES
from Crypto.Util.Padding  import pad

flag = b'CryptoCSG{###########}'
flag = pad(flag,8)
key = ###########   


cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(flag)
