from cryptography.fernet import Fernet #allow you encrypt text

def write_key():
    key=Fernet.generate_key()
    with open ("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    file= open ("key.key","rb")
    key=file.read()
    file.close()
    return key 
        
# master_pwd=input("What is the master password ?")
key=load_key()
fer=Fernet(key)



def view():
    with open ("password.txt","r") as f:
       for line in f.readlines():
           data=line.rstrip()
           user,password=data.split("|")
           print(" User:",user," and Passwrod : ",fer.decrypt(password.encode()).decode())

def add():
    name=input("Account username:")
    pwd=input("Password : ")

    with open ("password.txt","a") as f:
        f.write(name+ "|" + fer.encrypt(pwd.encode()).decode() +"\n")


while True:
    mode=input("Would you like to add a new password or view password?(view,add), press q to quit. \n").lower()
    if mode=="q":
        break
    elif mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode")
        continue


 

