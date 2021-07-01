35. Remove multiple elements from a list in Python
# method-1

# creating a list
list1 = [11, 5, 17, 18, 23, 50]

# Iterate each element in list
# and add them in variale total
for ele in list1:
	if ele % 2 == 0:
		list1.remove(ele)

# printing modified list
print("New list after removing all even numbers: ", list1)

# method-2

# Python program to remove multiple
# elements from a list

# creating a list
list1 = [11, 5, 17, 18, 23, 50]

# will create a new list,
# excluding all even numbers
list1 = [ elem for elem in list1 if elem % 2 != 0]

print(*list1)


# method-3

# Python program to remove multiple
# elements from a list

# creating a list
list1 = [11, 5, 17, 18, 23, 50]

# removes elements from index 1 to 4
# i.e. 5, 17, 18, 23 will be deleted
del list1[1:5]

print(*list1)
