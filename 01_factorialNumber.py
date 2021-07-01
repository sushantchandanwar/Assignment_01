# # 1. Python Program for factorial of a number with and without recursion
# # without recursion
#
# n=int(input("Enter number:"))
# fact=1
# while(n>0):
#     fact=fact*n
#     n=n-1
#
# print(fact)


# # with recursion
#
# def factorial(n):
#     if(n <= 1):
#         return 1
#     else:
#         return(n*factorial(n-1))
# n = int(input("Enter number:"))
# print("Factorial:")
# print(factorial(n))
#

# By using for loop

# n=6
# fact=1
# for i in range(1,n+1):
#     if n>0:
#         fact=fact*n
#         n=n-1
# print(fact)