import random
letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m'", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M'", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers=["0", "1", "2", "3","4", "5", "6", "7","8", "9"]
symbols=["!", "#", "@", "$", "%", "&", "*", "+", "(", ")"]
print("welcome to the password generator")
l=int(input("enter the numbers of letters you like to be in your password "))
s=int(input("enter the numbers of numbers you like to be in your password "))
n=int(input("enter the numbers of symbols you like to be in your password "))
password_list=[]
for i in range(0,l):
    char=random.choice(letters)
    password_list.append(char)
for i in range(0,s):
    char=random.choice(symbols)
    password_list.append(char)
for i in range(0,n):
    char=random.choice(numbers)
    password_list.append(char)
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print("your random password is - ", password)
