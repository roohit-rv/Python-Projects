import random
name=input("enter everybody's name: ")
names=name.split(",")
l=len(names)
length=l-1
number=random.randint(0,length)
payer=names[number]
print(payer, " will pay today's bill boiiii")

