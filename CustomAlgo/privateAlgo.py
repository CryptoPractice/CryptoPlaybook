from random import randint


a = 288260533169915
p = 1007621497415251

FLAG = b'CryptoCSG{p1uS_4Nd_Minu5_0ne5_AnD_z3r0}'

def xor(a,b):
    if a == b:
        return '0'
    else:
        return '1'
def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    prev = '0'
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        orig_b = b
        b = xor(prev,b)
        prev = orig_b
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    print(plaintext)
    print(ciphertext)
    return ciphertext


print(encrypt_flag(FLAG))