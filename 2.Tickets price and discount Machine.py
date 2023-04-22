# Tickets price with discount Machine
# The cost of each ticket is 100 INR
# Discount on ticket is 20% if tickets purchased are more than 10
# Discount on ticket is 25% if tickets purchased are more than 20
# No can purchase more than 25 tickets
# No discounts on tickets, if number of tickets are less than 11

print("ticket price with discount calculator")
tickets=int(input("enter the number of tickets you want to buy\n"))
print("the number of tickets: ",tickets)
if tickets<11:
  price=tickets*100
  print("Price: ",price)
elif(tickets>10 and tickets<21):
  price=tickets*80
  print("You will get 20 percent discount, Price: ", price)
elif(tickets>20 and tickets<26):
  price=tickets*75
  print("You will get 20 percent discount, Price: ", price)
elif tickets>26:
  print("Lower the number of tickets")
else:
  print("invalid inputs")