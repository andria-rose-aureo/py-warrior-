#comment other prgms to excute one :) LIST QUESTIONS

#Sum of Elements: Calculate the sum of all numbers in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(my_list)
sum_of_numbers = 0

for i in range(n):
    sum_of_numbers += my_list[i]

print(f"Sum of numbers in the list = {sum_of_numbers}")

#Reverse a list
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(f"Reversed list = {reversed_list}")

#Find Duplicates: Identify duplicate elements in a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 5, 7]
n = len(my_list)
duplicate_elements = []

for i in range(n):
    for j in range(i + 1, n):
        if my_list[i] == my_list[j] and my_list[i] not in duplicate_elements:
            duplicate_elements.append(my_list[i])
            print(f"duplicate element = {my_list[i]}")

#Sort a List: Sort a list in ascending and descending order.
my_list = ["apple", "banana", "dog", "egg", "cat"]
my_list.sort()
print(f" ascending order : {my_list}")
print(f"descending order : {my_list[::-1]}")

#Remove Duplicates: Remove duplicate elements while maintaining the original order.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 5, 7]
temp = my_list[:]
n =len(temp)
for i in range(n):
    for j in range(i + 1, n):
        if my_list[i] == my_list[j] :
            my_list.pop(j)
            n = len(my_list)
            break
print(f"original list ={temp}")
print(f"list after duplicates removed = {my_list}")

# Intersection of Two Lists: Find common elements between two lists.
common_element = []
my_list =[1,2,3,4]
my_list2=[5,2,6,4,5,1,2,]
n = len(my_list)
m = len(my_list2)
for i in range (n):
     for j in range(m):
       if my_list[i] == my_list2[j] and my_list[i] not in common_element:
        common_element.append(my_list[i])
        print(f"common elements :{common_element}")


#Rotate List: Rotate the elements of a list left or right by a given number of steps.
my_list = [1, 2, 3, 4, 5]
steps = int(input("enter no of steps = "))
for _ in range(abs(steps)):
    my_list.append(my_list.pop(0))
print(my_list)  # Output: [3, 4, 5, 1, 2]

#Largest and Smallest Elements: Find the largest and smallest elements in a list.
my_list = [10,5,55,7,14]
maxi = max(my_list)
mini = min(my_list)
print(f"Smallest = {mini}")
print(f"Largest = {maxi}")
