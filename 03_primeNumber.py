# To take input from the user
# num = int(input("Enter a number: "))
#
# # define a flag variable
# flag = False
#
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break
#
# # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")

# method-2

n=int(input("Enter the number"))
if n%2 != 0 and  n%3!= 0 and  n%5 != 0 and  n%7 != 0 :
    print("Given no. is prime no.")
else:
    print("No.is not prime no.")


# method-3

