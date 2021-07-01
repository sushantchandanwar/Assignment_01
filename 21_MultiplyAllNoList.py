# 21. Python | Multiply all numbers in the list

# method-1

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))

# method-2

# Python3 program to multiply all values in the
# list using lambda function and reduce()

from functools import reduce
list1 = [1, 2, 3]
list2 = [3, 2, 4]


result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)
