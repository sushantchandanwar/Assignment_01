 # Python program to print negative numbers in a list
# method-1
 list1 = [11, -21, 0, 45, 66, -93]

 # iterating each number in list
 for num in list1:

     # checking condition
     if num < 0:
         print(num, end=" ")

# method=2

 list1 = [-10, 21, -4, -45, -66, 93]
 num = 0
 while (num < len(list1)):
     if list1[num] < 0:
         print(list1[num], end=" ")
     num += 1
     

