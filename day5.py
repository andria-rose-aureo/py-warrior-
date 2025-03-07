"""Multiplication table"""

num = int(input("enter a number:  "))
if type(num) ==  int :
    for i in range (1,11):
        value = num * i
        print(f"{num}*{i} = {value}")
else :
    print("INVAILD INPUT, ENTER A INTEGER: ")