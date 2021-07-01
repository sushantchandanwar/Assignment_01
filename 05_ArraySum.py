# 5. Python Program to find sum of array (using multiple approach)
# method-1


arr = [1, 2, 3, 4, 5]
sum = 0

#Loop through the array to calculate sum of elements
for i in range(0, len(arr)):
   sum = sum + arr[i]

print("Sum of all the elements of an array: " + str(sum));

# method 2


# arr = [1, 2, 3, 4, 5]
# ans = sum(arr)
# print('Sum of the array is ', str(ans))