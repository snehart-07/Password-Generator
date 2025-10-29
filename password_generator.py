import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['*','@','$','^','&','#','!','~','_']
numbers = ['1','2','3','4','5','6','7','8','9','0']
print("Welcome to password generator")

l = int(input("Enter number of letters in password\n"))
s = int(input("Enter number of symbols in password\n"))
n = int(input("Enter count of numbers in password\n"))

password = []
for char in range(1,l+1):
    password += random.choice(letters)
for char in range(1,s+1):
    password += random.choice(symbols)
for char in range(1,n+1):
    password += random.choice(numbers)
random.shuffle(password)
p = ""
for char in password:
    p += char
print(f"your password is {p}\n")

print("THANK YOU!!!")
