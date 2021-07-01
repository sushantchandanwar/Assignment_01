# 28 Python program to print Even Numbers in given range


# start = int(input("Enter the start of range: "))
# end = int(input("Enter the end of range: "))
#
# # iterating each number in list
# for num in range(start, end + 1):
#     if num % 2 == 0:
#         print(num)


# Python3 program to print
# even length words in a string

def printWords(s):
    # split the string
    s = s.split()

    # iterate in words of string
    for word in s:

        # if length is even
        if len(word) % 2 == 0:
            print(word)


# Driver Code
s = "i am muskan"
printWords(s)
