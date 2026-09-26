'''
uses
1-Dictonary
2-loops
3-conditional
4-Module: random
5- File handeling

websit : password

random module
file read/write
real world
'''



import random
import string

password={}

try:
    with open("password.txt", "r") as file:
        for line in file:
            website, pwd= line.strip().split(":")
            password[website]= pwd
except:
    pass

def generate_password():
    chars= string.ascii_letters + string.digits + "!@#$%^&*()<>?"
    password ="".join(random.choice(chars) for _ in range(8))
    return password
while True:
    print("---personal password manager----")
    print("1. Save password")
    print("2. view password")
    print("3. generate password")
    print("4, Exit")

    choice= input("enter your choice ")
    if choice=="1":
        site = input("enter website: ")
        pwd = input("enter password: ")

        password[site] = pwd
        with open("password.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")
        print("saved")
    elif choice=="2":
        if not password:
            print("no data")
        else:
            for site, pwd in password.items():
                print(site,":", pwd)
    elif choice =="3":
        print(generate_password())
    elif choice =="4":
        print("ok bye...")
        break


    else:
        print("in-valid input")




        


