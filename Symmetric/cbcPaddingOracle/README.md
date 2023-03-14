# CBC Padding Oracle Attack

## Introduction

The CBC padding oracle vulnerability has been made known for some times but can unfortunately still be found in many modern applications.
It is easily overlooked when developers implement the padding algorithm or utilize the cryptographic functions.
This challenge demonstrated even a secure cryptosystem can be broken easily due to insecure implementation on PKCS#7 padding.

## Setup Instruction
1. pip install -r requirements.txt
2. python cbcPaddingOracle.py

## Writeup and Analysis

<details>
  <summary>Spoiler for Solution</summary>

  ## Proposed Solution   
  1. Browse to the URL http://localhost:5000 and notice the page allows the user to input their name for registration.
  2. After input the name and click the register button, we successfully login as a user and the server return us the encrypted cookie `Session`.
  3. The challenge can be solved easily by using the [Padding Oracle Hunter Burp Extender](https://portswigger.net/bappstore/0efabfee59404068a8c4071fa18a2e00)
  4. First, intercept and pipe the request through `Extensions -> Padding Oracle Hunter -> PKCS#7`
  5. Select the `Session` cookie in the Request window, click `Select Payload` with `Hex` format, and uncheck `Url Encoded`. The payload will be enclosed within the `§` symbol. 
  6. Click the `Test` button and it will provide a summary which indicate the server is vulnerable to the padding oracle attack with its corresponding invalid/valid padding payload and response.
  7. Copy either part or full of the valid (Invalid JSON Format!) or invalid (Decryption Failed!) padding response from the `Output` window and put it in the `Padding Response` textbox.
  8. Click the `Decrypt` button to recover the plaintext.
  9. Modify the `role` in the plaintext from `user` to `admin` and convert the plaintext to hexadecimal.
 10. Input the hexadecimal value into the `Plaintext` field and click the `Encrypt` button to compute the encrypted `Session` cookie.
 11. Copy the encrypted `Session` cookie and replace the original `Session` in order to login as admin.

 ## Analysis 

 ```python
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
 ```
 By looking at the code snippets of cbcPaddingOracle.py as shown above, the server is returning different response when there is an invalid padding (Decryption Failed!) compare to a valid padding (Invalid JSON Format!)
 Hence, attacker is able to make use of this side channel information to perform the padding oracle attack.
 
 As a mitigation, the developer should ensure the code always return the same response when decrypting packets for either valid or invalid padding.
</details>