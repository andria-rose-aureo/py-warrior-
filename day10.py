#Set Operations: Demonstrate basic operations like adding, removing, and checking membership.
 #adding
set = {1,2,3}
set.add(4)
print(set)

#removing
set1 = {1,2,3}
set1.remove(2)
print(set1)

#checking_membership
set2= {10, 20, 30, 40, 50}
element = int(input("enter a element exists :  "))

if element in set2:
    print(f"{element} is in the set2.")
else:
    print(f"{element} is not in the set2.")
