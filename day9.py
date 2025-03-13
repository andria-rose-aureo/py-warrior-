#comment other prgms to excute one :) TUPLE QUESTIONS 

#Unpack a Tuple: Unpack elements of a tuple into variables.
my_tuple = (1,2,3)
a,b,c = my_tuple
print(a,b,c)

#Immutable Test: Demonstrate that tuples are immutable by attempting to change an element.
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)
try:
    my_tuple[1] = 10
except TypeError as e:
    print("Error:", e)
 
# Count Elements: Count the occurrences of a specific element in a tuple.
my_tuple =[10,20,30,20,40]
print(my_tuple.count(20))
 
#Index of Element: Find the index of an element in a tuple.
my_tuple =[10,20,30,20,40]
print(my_tuple.index(20))
 

#Concatenate Tuples: Concatenate two or more tuples.
tuple1 = (1,2,3)
tuple2 = (4,5,6)
res = tuple1+tuple2
print(res)
 

#Tuple to List: Convert a tuple into a list and vice versa.
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print("List:", my_list)

new_tuple = tuple(my_list)
print("Tuple:", new_tuple)
 
#Check Membership: Check if an element exists in a tuple.
my_tuple = (10, 20, 30, 40, 50)
element = int(input("enter a element exists :  "))
if element in my_tuple:
    print(f"{element} is in the tuple.")
else:
    print(f"{element} is not in the tuple.")
 
#Tuple as Dictionary Key: Use tuples as keys in a dictionary for storing coordinates or data.
tup1 = 1,2,3
tup2 = 4,5,6
tup3 = 7,8,9,
dict ={ 1: tup1, 2:tup2, 3:tup3}
print(dict)
 

#Slice a Tuple: Extract specific elements or sub-tuples using slicing.
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
slice1 = my_tuple[1:5]
slice2 = my_tuple[:4]
print("Original Tuple:", my_tuple)
print("Slice1 (1 to 4):", slice1)
print("Slice2 (First 4):", slice2)
