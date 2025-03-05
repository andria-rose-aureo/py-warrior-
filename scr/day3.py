"""Create a Simple Grade Checker App 📄"""
marks = int(input("enter the marks scored : "))
if (marks>=90):
    print("A garde")
elif(marks>=75):
    print("B garde")
elif (marks>=50):
    print("C grade")
else:
    print("Failed")