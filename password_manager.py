from cryptography.fernet import Fernet


# step-5
def load_key():
    file = open("key.key", "wb")
    key = file.read()
    file.close()
    return key


# key = load_key() + master_pwd.encode()
key = load_key()
fer = Fernet(key)
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''

# step1
master_pwd = input("What is the master password? ")


# step-4
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


#            print("User:", user, "| Password: ", passw)


# step-3
def add():
    name = input("Account Name: ")
    pwd = input("password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode())


#          f.write(name + " | " + pwd + "\n")


# step-2
while True:
    mode = input("Would you like tp add a new Password or view existing ones (view, add), pres q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
