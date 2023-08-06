import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols="!@#$%^&*(){}."
numbers="0123456789"

string=lower+upper+symbols+numbers

length=int(input("enter your pass word length:"))
password="".join(random.sample(string,length))

print("Your New Password is \U0001F600  =" +  password)