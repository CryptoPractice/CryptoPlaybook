from Crypto.Cipher import AES
from flask import Flask, request, render_template,url_for,redirect
from binascii import hexlify,unhexlify
from cryptography.hazmat.primitives import padding
from forms import RegisterForm
import json

#AESpip
key = 'zz4zDXRqvUpZa944'
BLOCK_SIZE = 128

app = Flask(__name__)
app.config["SECRET_KEY"] = b'o5Dg987*&G^@(E&FW)}'

def Aes_encrypt(plaintext):
    plaintext = bytes(plaintext,'utf-8')
    cipher = AES.new(key=key.encode(),mode=AES.MODE_CBC)
    padder = padding.PKCS7(BLOCK_SIZE).padder()
    padded_text = padder.update(plaintext) + padder.finalize()
    ciphertext = cipher.encrypt(padded_text)
    iv = cipher.iv
    return iv+ciphertext
    
def Aes_decrypt(ciphertext):
    try:
        ciphertext = unhexlify(ciphertext)
        iv = ciphertext[:16]    
        cipher = AES.new(key=key.encode(), mode=AES.MODE_CBC, IV=iv)
        decrypted_text = cipher.decrypt(ciphertext[16:])
        unpadder = padding.PKCS7(BLOCK_SIZE).unpadder()   
        return unpadder.update(decrypted_text) + unpadder.finalize()   
    except:    
        return None


def ValidateAdmin(payload):    
    role = payload.get('role')
    if role is None:
        return False
    else:
        if role=='admin':
            return True
        else:
            return False


@app.route("/",methods=["GET","POST"])
def index():
    form = RegisterForm(request.form)
    value = request.cookies.get('Session')

    # if the decryption fail mostly due to invalid padding
    if value:
        plaintext = Aes_decrypt(value)
        if plaintext is None:
           return "Decryption Failed!"

        # if the padding is valid but not in json format
        try:
            json.loads(plaintext)
            return redirect(url_for('portal'))        
        except:
            return "Invalid JSON Format!"            
        

    # Compute the encrypted cookie after submit the username
    if request.method == "POST" and form.validate():        
        res = redirect(url_for('portal')) 
        res.set_cookie(
            'Session',
            hexlify(Aes_encrypt('{{"username":"{}","role":"user"}}'.format(form.Name.data)))
        )
        return res
    return render_template('home.html', form=form)


@app.route("/portal",methods=["GET","POST"])
def portal():
    value = request.cookies.get('Session')

    # if the decryption fail mostly due to invalid padding
    if value:
        plaintext = Aes_decrypt(value)

        if plaintext is None:
           return "Decryption Failed!"

        # if the padding is valid but not in json format
        try:
            payload = json.loads(plaintext)        
        except:
            return "Invalid JSON Format!"        

        # validate whether the user has admin role
        if ValidateAdmin(payload):            
            return render_template('admin.html')
        else:
            return render_template('user.html')          
    return redirect(url_for('index'))        


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")