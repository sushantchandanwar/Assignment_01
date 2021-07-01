# Python program to print positive Numbers in a List
# method-1

list1 = [11, -21, 0, 45, 66, -93]
for num in list1:
    if num >= 0:
        print(num, end=" ")

# method-2


# list1 = [-10, -21, -4, 45, -66, 93]
#
# # using list comprehension
# n = [x for x in list1 if x >= 0]
#
# print("Positive numbers in the list: ", *n)
