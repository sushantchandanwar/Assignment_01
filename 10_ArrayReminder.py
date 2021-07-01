# 10. Python Program for Find reminder of array multiplication divided by n
#
def findremainder(arr, lens, n):
    mul = 1

    for i in range(lens):
        mul = (mul * (arr[i] % n)) % n

    return mul % n


# Driven code
arr = [100, 10, 5, 25, 35, 14]
lens = len(arr)
n = 9

# print the remainder
# of after multiple
# all the numbers
print(findremainder(arr, lens, n))

# This code

