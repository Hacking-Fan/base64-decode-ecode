#Base64decode
import base64
import os

text = input("Enter Text Base64 ")
d = base64.b64decode(text)
s2 = d.decode("UTF-8")



print("")
print("Decode: ",s2)

input("")
os.system("python3.8 main.py")
