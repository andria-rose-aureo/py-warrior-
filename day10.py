#comment other prgms to excute one :) SET QUESTIONS 

#Set Union and Intersection: Perform union and intersection operations between two sets.
my_set = {1,2,3,4}
my_set2 = {5,6,7,8}
res = my_set.union(my_set2)
print(res)
 

#Unique Elements: Use a set to extract unique elements from a list.
my_list = [1,2,3,4,5,6,7,8,9,10]
unique_elements = list(set(my_list))
print("Original List:", my_list)
print("Unique Elements:", unique_elements)
 

#Symmetric Difference: Find elements present in either of two sets but not both.
set1 = {1,2,3}
set2 ={3,4,5}
print(set1^set2)
   
#Subset Check: Check if a set is a subset of another.
set1 = {1,2,3,4,5}
set2={3,4}
res = set2.issubset(set1)
print(res)
 
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
 

#Set Difference: Find elements present in one set but not another.
set1 = {1,2,3,4}
set2={3,4}
res = set1 - set2
print(res)
 
#Set to List: Convert a set into a list and sort it.
set1 = {"apple", "cat","egg","ball","dog"}
res =list(set1)
res.sort()
print(res)




