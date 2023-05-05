row1=["📦","📦","📦"]
row2=["📦","📦","📦"]
row3=["📦","📦","📦"]
map=[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
place=input("enter the row and column number of the box where you want to hunt for the treasure: ")
vertical=int(place[0])
horizontal=int(place[1])
map[vertical-1][horizontal-1]="X"
print(f"{row1}\n{row2}\n{row3}")
