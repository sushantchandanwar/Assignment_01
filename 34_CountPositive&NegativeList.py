# Python program to count positive and negative numbers in a List

# list of numbers
list1 = [10, -21, 4, -45, 66, -93, 1]

pos_count, neg_count = 0, 0

# iterating each number in list
for num in list1:

    # checking condition
    if num >= 0:
        pos_count += 1

    else:
        neg_count += 1

print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)


# method-2

# Python program to count positive
# and negative numbers in a List

# list of numbers
list1 = [-10, -21, -4, -45, -66, -93, 11]

only_pos = [num for num in list1 if num >= 1]
pos_count = len(only_pos)

print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", len(list1) - pos_count)
