from Crypto.Cipher import DES
from Crypto.Util.Padding  import pad

flag = b'CryptoCSG{4his_k3y_15_s0_w34k}'
flag = pad(flag,8)
key = b'\xE0'*4+b'\xF1'*4       


cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(flag)
