
from email.generator import DecodedGenerator
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)

plaintext = "*********".encode()
token = fernet.encrypt(plaintext)
output = token.decode()
decrypted_token = fernet.decrypt(token)
print(output)


def add():
    name = input ('Account Name : ')
    pwd = input ('Password : ')
    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + str(decrypted_token) + "\n")

def view ():
     with open('passwords.txt', 'r') as f:
         for line in f.readlines():
           print(line.split())
        

while True:
    mode = input ("Would you like to add a new passwor or view existing ones(view,add),press q to quit : ")
    if mode == "q":
        break 
    if mode == "view":
        view()

    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

