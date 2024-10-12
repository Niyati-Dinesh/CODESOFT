
import random as r
letters='abcdefghijklmnopqrstuvwxyz'
letterc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char='-_=+.,<>?/!@#$%^&*'
numb='1234567890'
types=[letters,letterc,char,numb]

while True:
    password=''
    try:
        length=int(input("Enter length of password:"))
        if length>=5:
            while (length):
                c=r.choice(types)
                c1=r.choice(c)
                password+=c1
                length-=1
            print("Your password is :"+password)
            break
        else:
            print("Password should be atleast 5 characters long")
    except ValueError:
        print("Enter valid password length!!")
