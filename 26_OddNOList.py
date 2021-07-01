# 25. Python program to print odd numbers in a list

# method-1

list1 = [11,23,45,23,64,22,11,24]
# iteration
for num in list1:
   # check
   if num % 2 != 0:
      print(num, end = " ")

# method-2

list1 = [11,23,45,23,64,22,11,24]
# lambda exp.
odd_no = list(filter(lambda x: (x % 2 != 0), list1))
print("Even numbers in the list: ", odd_no)


# method-3

list1 = [11,23,45,23,64,22,11,24]
#list comprehension
odd_nos = [num for num in list1 if num % 2 != 0]
print("Even numbers : ", odd_nos)