
# 1.	Sum of Elements: Calculate the sum of all numbers in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(my_list)
sum_of_numbers = 0

for i in range(n):
    sum_of_numbers += my_list[i]

print(f"Sum of numbers in the list = {sum_of_numbers}")

# 2. Reverse a list
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(f"Reversed list = {reversed_list}")

# 3.	Find Duplicates: Identify duplicate elements in a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 5, 7]
n = len(my_list)
duplicate_elements = []

for i in range(n):
    for j in range(i + 1, n):
        if my_list[i] == my_list[j] and my_list[i] not in duplicate_elements:
            duplicate_elements.append(my_list[i])
            print(f"duplicate element = {my_list[i]}")
