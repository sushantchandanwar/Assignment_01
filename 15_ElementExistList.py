# 15. Python | Ways to check if element exists in list
# method-1

mylist=[2,3,4,5,6,7,8,9]
x=int(input("Enter value to check:"))
if x in mylist:
    mylist[mylist.index(x)] #do something to it
    print("Found")
else:
    print("Not found")

# method-2

test_list = [ 1, 6, 3, 5, 3, 4 ]

print("Checking if 4 exists in list ( using loop ) : ")

for i in test_list:
    if(i == 4) :
        print ("Element Exists")

print("Checking if 4 exists in list ( using in ) : ")

if (4 in test_list):
    print ("Element Exists")
