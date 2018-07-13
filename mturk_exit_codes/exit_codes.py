from otree.models import Session
from otree.api import safe_json
# from Crypto.Cipher import AES
# from Crypto.Hash import SHA
import hashlib
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
	IN "encrypt_participant_codes" and in views.py vars_for_tempalte!
"""
ENCRYPTION_KEY = b'This is a key124' # ENCRYPTION_KEY should be 16 characters in length
folder = '__access-exitcodes/'
date = datetime.now().strftime("%Y-%m-%d")

def hash_and_save_csv(participants, session_code, url):
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
	hashed = hash_participant_codes(codes)
	try:
		if not os.path.exists(folder):
			os.makedirs(folder)
		with open(folder+date +"_"+ session_code + ".csv", 'x') as out:
			print(out.name, 'does not yet exist')

			out.write('AccessCode,ExitCode'+'\n')     
			for code_exit_code in hashed:
				out.write(code_exit_code['AccessCode']+','+code_exit_code['ExitCode']+'\n')
	except:
		print(folder+date +"_"+ session_code + ".csv", 'does already exist')


def hash_and_save_json(participants, session_code, url=""):
	"""
	participants is the participants list
	session_code is the current session code
	see above
	"""
	codes = [participant.code for participant in participants]
	# Choose Hashing or Encrypting here
	hashed = hash_participant_codes(codes)
	try:
		if not os.path.exists(folder):
			os.makedirs(folder)
		with open(folder+date +"_"+ session_code + ".json", 'x') as out:
			print(out.name, 'does not yet exist')

			json.dump(hashed, out, indent=4)
			safe_json(hashed)
	except:
		print(folder+date +"_"+ session_code + ".json", 'does already exist')

	return hashed

def encrypt_participant_codes(codes):
	"""
	Encrypt the participants codes
	"""
	return [{code: aes_encrypt(code)} for code in codes]

def hash_participant_codes(codes):
	"""
	Hash the participants codes
	"""
	return [{'AccessCode': code,
			 'ExitCode': sha_hash(code)} for code in codes]


# def aes_encrypt(string):
# 	"""
# 	A method to encrypt the string
# 	string length must be a multiple of 8 always
# 	"""
# 	string = (string+string).encode() # Make the string 16 letters
# 	if len(string) % 16 == 0:
# 		obj = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, b'This is an IV456') # This is an IV
# 		ciphertext = obj.encrypt(string)
# 		cipher_base64_encoded = base64.b64encode(ciphertext).decode('utf-8')
# 		# b: Specify the length of the codes here
# 		return cipher_base64_encoded[0:8]
# 	else:
# 		return None

def sha_hash(string):
	# b: Specify the length of the codes here
	# return SHA.new(string.encode()).hexdigest()[:8]
	return hashlib.sha256(string.encode()).hexdigest()[:8]