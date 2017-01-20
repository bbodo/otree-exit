from otree.models import Session
from Crypto.Cipher import AES
import base64
from pprint import pprint
from datetime import datetime
"""
IMPORTANT: Make sure to install pycrypto python package
"""
ENCRYPTION_KEY = 'This is a key124' # ENCRYPTION_KEY should be 16 characters in length

def encrypt_and_save(participants, session_code, url):
    """
    participants is the participants list
    session_code is the current session code
    url is the participant start url
    for example:
        http://192.168.99.100:3000/InitializeParticipant/
        or
        http://example.com/InitializeParticipant/
    """
    codes = [participant.code for participant in participants]
    encrypted = encrypt_participant_codes(codes)
    with open(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+"_"+ session_code+".csv", 'w') as out:
        out.write('URL, Exit_Code\n')               
        for code_exit_code in encrypted:
            for key, value in code_exit_code.items():
                 out.write(url.strip()+""+key+", "+value+"\n")


def encrypt_participant_codes(codes):
    """
    Encrypt the participants codes
    """
    return [{code: aes_encrypt(code)} for code in codes]


def aes_encrypt(string):
    """
    A method to encrypt the string
    string length must be a multiple of 8 always
    """
    string = string+string # Make the string 16 letters
    if len(string) % 16 == 0:
        obj = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, 'This is an IV456') # This is an IV
        ciphertext = obj.encrypt(string)
        cipher_base64_encoded = base64.b64encode(ciphertext).decode('utf-8')
        return cipher_base64_encoded
    else:
        return None