
# Python program to find smallest
# method-1

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the first element
print("Smallest element is:", *list1[:1])

# method-2


# list of numbers
list1 = [10, 20, 1, 45, 99]


# printing the maximum element
print("Smallest element is:", min(list1))
