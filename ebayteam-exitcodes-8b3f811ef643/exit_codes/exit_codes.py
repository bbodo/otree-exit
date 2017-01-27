from otree.models import Session
from Crypto.Cipher import AES
from Crypto.Hash import SHA
import base64
from pprint import pprint
from datetime import datetime
import csv
import json
import os
import re

"""
IMPORTANT: Make sure to install pycrypto python package
bobrae: pycrypto has been replaced by pycryptodome.
    now the problem is that this code is written entirely using utf-8 strings
    we need byte strings - b'' or .encode() - namely the ENCRYPTION_KEY and the 
    "InitializationVecor" - "IV" below.
    TO CHANGE FROM ALPHANUM TO COMPLEXER CODES, SWITCH "sha_hash" to "aes_encrypt"
    IN "encrypt_participant_codes"
"""
ENCRYPTION_KEY = b'This is a key124' # ENCRYPTION_KEY should be 16 characters in length

def encrypt_and_save_csv(participants, session_code, url):
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
        out.write('AccessCode, ExitCode\n')               
        for code_exit_code in encrypted:
            for key, value in code_exit_code.items():
                 out.write(url.strip()+""+key+", "+value+"\n")

# def csv_to_json():
#     """ 
#         bobrae: Converting CSV to JSON instead of direct JSON, just in case CSV is better
#         solution after all.
#     """
#     path = os.path.abspath(os.path.dirname(__file__))
#     for filename in os.listdir(path):
#         if re.match('.+csv', filename):
#             with open(os.path.join(path, filename), 'r') as csvfile:
#                 with open('test.json', 'w') as jsonfile:
#                 #csvfile = open('file.csv', 'r')
#                     fieldnames = ("AccesCode","ExitCode")
#                     reader = csv.DictReader(csvfile, fieldnames)
#                     for row in reader:
#                         json.dump(row, jsonfile)
#                         jsonfile.write('\n')

def encrypt_and_save_json(participants, session_code, url):
    """
    see above
    """
    codes = [participant.code for participant in participants]
    encrypted = encrypt_participant_codes(codes)
    with open(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+"_"+ session_code+".json", 'w') as out:
        for code_exit_code in encrypted:
            out.write(json.dumps(code_exit_code, out, indent=4))

"""
    bobrae : I used .encode on the codes below, to make the code work. 
"""

def encrypt_participant_codes(codes):
    """
    Encrypt the participants codes
    """
    return [{code: sha_hash(code)} for code in codes]


def aes_encrypt(string):
    """
    A method to encrypt the string
    string length must be a multiple of 8 always
    """
    string = string+string # Make the string 16 letters
    if len(string) % 16 == 0:
        obj = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, b'This is an IV456') # This is an IV
        ciphertext = obj.encrypt(string)
        cipher_base64_encoded = base64.b64encode(ciphertext).decode('utf-8')
        # b: Specify the length of the codes here
        return cipher_base64_encoded[0:8]
    else:
        return None

def sha_hash(string):
    return SHA.new(string.encode()).hexdigest()[:8]