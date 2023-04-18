# Block Cipher Attack on ECB Mode

## Introduction

The Electronic Code Book (ECB) Mode for block cipher is not secure as it encrypts each block separately which is highly deterministic.
The same plaintext will always encrypt into the same ciphertext. If attacker is able to perform the choosen plaintext attack, he might be
able to recover the unknown ciphertext.

## Setup Instruction
1. pip install -r requirements.txt
2. python cbcPaddingOracle.py

## Writeup

<details>
  <summary>Spoiler for Solution</summary>

  ## Proposed Solution 
  
  1. Navigate to the page at URL http://localhost. Key in any guess character and the server will return the ciphertext.
  1. Examine the provided `server.py`.
  2. Notice there is a custom padding which consist of a SECRET we would like to recover.
  3. Realise that the problem the use of ECB mode which resulting the fixed ciphertext is being returned.
  4. [Full explanation of the vulnerability.](https://web.archive.org/web/20220713023815/https://derekwill.com/2021/01/01/aes-cbc-mode-chosen-plaintext-attack/)
  5. Exploit using the script below.

```python
import requests
import json
import urllib.parse
from string import printable as ALPHANUMERIC

def encryption(plaintext):
    encrypted_string=""        
    url = "http://localhost/api/compare?guess={}".format(urllib.parse.quote(plaintext))    
    response = requests.post(url)
    result = json.loads(response.text)

    for rec in result:        
            encrypted_string += rec['letter']
    
    return encrypted_string


secret=""
secret_len = 18
guess = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

for i in range(0,secret_len):    
    actual = encryption(guess[:31-i])
    for c in ALPHANUMERIC:    
        compute = encryption(guess[:31-i] + secret + c)
        if(compute == actual):
            secret += c
            print(secret)
            break           
            

print("The secret is: " + secret)
```
 ## Analysis 
 ```python
 def encrypt(bstring):
    padded_data = pad(bstring)
    cipher = Cipher(algorithms.AES(KEY), modes.ECB())
    encryptor = cipher.encryptor()
    return encryptor.update(padded_data) + encryptor.finalize()
 ```
 By looking at the code snippets of server.py as shown above, the encryption is using the AES ECB mode.
 Since the ciphertext is fixed, by performing the choosen plaintext attack, it allows us to manipulate the plaintext
 and bruteforce each individual byte which eventually lead to a complete recovery.
 
 As a mitigation, ECB mode should never be used. Developer should choose a more secure cipher block mode such as Galois Counter Mode (GCM)
</details>
