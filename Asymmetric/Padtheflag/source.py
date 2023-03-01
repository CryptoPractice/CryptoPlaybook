import socketserver
import signal
import rsa
from Crypto.Util.number import bytes_to_long, long_to_bytes
from secret import FLAG

ENCRYPTED_FLAG = "AAC249B3678C794D115E35E895966E69EE110F9483733602FE27075DB677EA616A5FF69FA22B7E303A4EC7D4FC39E9E62DFF1BDC7A386480F7AD1248D66061D14179B0C5455C48B329D338A9637818794532813940614F367466B49CBECB0A19E74E056170E7049F5F627ABEFB0915CDBDB9E1A5AC5AFFD2F0BE5826A0A9D0C2336CCADDC119CC64B97AF203DCF0E27D3F544A5944485BB9EE935B432BEB39B18410A78B2BC0F5585D6058B2DD3516E6B2F6375B885E6339FED7E7DCD89476D221C7C5A0EB14351373882768894FC154FAB68C45B16047AB85801198CC8050EAD6ABFC30E125A34951DDE958B1054CAE9240A52AF77A59445C20182C1FD5B601"
PADDING = b"\x00\x04"

with open("keys/private_key.pem", "rb") as f:
    PRIVATE_KEY = rsa.PrivateKey.load_pkcs1(f.read())

with open("keys/public_key.pem", "rb") as f:
    RSA_PUBLIC_KEY = rsa.PublicKey.load_pkcs1(f.read())


class RSA():

    def __init__(self):
        self.private_key = PRIVATE_KEY
        self.padding = PADDING

    def rsa_decrypt(self, ciphertext, priv_key) -> bytes:
        encrypted = bytes_to_long(ciphertext)
        decrypted = priv_key.blinded_decrypt(encrypted)
        cleartext = long_to_bytes(decrypted,256)
        return cleartext

    def unpad(self, padded):
        padded = padded[2:]
        idx = padded.find(b'\x00')
        if (idx == -1):
            return b""
        else:
            message = padded[idx + 1:]
            return message

    def valid(self, plaintext):
        if len(plaintext) < 11:
            return False

        return plaintext[:2] == self.padding

    def decrypt(self, ciphertext):
        try:
            return self.rsa_decrypt(bytes.fromhex(ciphertext), self.private_key)
        except Exception as e:
            #print(e)
            return None


def challenge(req):
    rsa = RSA()

    while True:
        req.sendall(b"option: ")        
        option = int(req.recv(4096).strip())

        if option == 1:
            req.sendall(f'n: {RSA_PUBLIC_KEY.n}\n'.encode())
            req.sendall(f'e: {RSA_PUBLIC_KEY.e}\n'.encode())
        elif option == 2:
            req.sendall(f'Encrypted Flag: {ENCRYPTED_FLAG}\n'.encode())
        elif option == 3:
            req.sendall(b"Enter Encrypted Flag: ") 
            encrypted = req.recv(4096).strip().decode()

            plaintext = rsa.decrypt(encrypted)

            if plaintext is None:
                req.sendall(b"Decryption Failed!\n")
                continue

            if not rsa.valid(plaintext):
                req.sendall(b"Invalid Padding!\n")
                continue

            plaintext = rsa.unpad(plaintext)

            if plaintext == FLAG:
                req.sendall(b"The flag is correct!\n")
            else:
                req.sendall(b"The flag is incorrect!\n")
        else:
            req.sendall(b"Goodbye")
            exit(1)


class incoming(socketserver.BaseRequestHandler):
    def handle(self):
        signal.alarm(6000)
        req = self.request
        challenge(req)

class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

def main():
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 9000), incoming)
    server.serve_forever()

if __name__ == "__main__":
   main()