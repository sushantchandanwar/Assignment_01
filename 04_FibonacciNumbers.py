 # 4. Python Program for Fibonacci numbers
# Function for nth Fibonacci number 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

num=int(input("Enter the number"))

def Fibonacci(n):

# Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

# Check if n is 1,2
# it will return 1
    elif n == 1 :
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(num))


# method-2

 def fibonacci(n):
     a = 0
     b = 1

     # Check is n is less
     # than 0
     if n < 0:
         print("Incorrect input")

     # Check is n is equal
     # to 0
     elif n == 0:
         return 0

     # Check if n is equal to 1
     elif n == 1:
         return b
     else:
         for i in range(1, n):
             c = a + b
             a = b
             b = c
         return b

 # Driver Program
 print(fibonacci(9))
