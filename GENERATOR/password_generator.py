import random
inints = range(32, 127)

password = ''

for i in range(10):
    password += chr(random.choice(inints))

print("password is :", password)
