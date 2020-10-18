#Base64
import base64
import os

text = input("Enter Text ")
b = text.encode("UTF-8")
e = base64.b64encode(b)



print("")
print("Hach: ",e)

input("")
os.system("python3.8 main.py")
