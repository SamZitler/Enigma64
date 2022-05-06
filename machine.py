from Enigma64 import *

# settings = getSettings()

encryptor = Enigma(settings)

# text = input("Enter anything here >>> ")
# print(Encrypt(text, encryptor))

# fileEncrypt("image.jpg", "encrypted", encryptor)

# encryptor = Enigma(settings)
fileDecrypt("encrypted", "decrypted.jpg", encryptor)