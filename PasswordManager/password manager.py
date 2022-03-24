
from adminAccount import Message
from adminAccount import Admin
from cryptography.fernet import Fernet


def add():
    name = input('User Name : ')
    pwd = input('Password : ')
    key = pwd
    key = Fernet.generate_key()
    f = Fernet(key)
    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + str(key) + "\n")
    with open('decodePassword.txt', 'a') as file:
        file.write(name + "|" + str(key) + '\n')


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "###", "Password", passw)


def view_decode_pwd():
    with open('decodePassword.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User: ", user, "###", "Password", passw)
                


while True:
    mode = input("""Would you like to add a new password or view existing ones(view,add)
or login into Admin account(admin),press q to quit : """.lower())
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "admin":
        Admin()
        answer = input("Would You like see all password ?(y/n)".lower())
        if answer == "y":
            view_decode_pwd()
        else :
            break 

    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
