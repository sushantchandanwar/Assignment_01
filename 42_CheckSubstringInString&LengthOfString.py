# Method1: Using user defined function.

# function to check if small string is
# there in big string
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")


# driver code
string = "geeks for geeks"
sub_str = "geek"
check(string, sub_str)

# method-2


def check(s2, s1):
    if (s2.count(s1) > 0):
        print("YES")
    else:
        print("NO")


s2 = "A geek in need is a geek indeed"
s1 = "geek"
check(s2, s1)


# method-3

# When you have imported the re module, you can start using regular expressions.
import re

# Take input from users
MyString1 = "A geek in need is a geek indeed"
MyString2 ="geek"

# re.search() returns a Match object if there is a match anywhere in the string
if re.search( MyString2, MyString1 ):
	print("YES,string '{0}' is present in string '{1}' " .format(MyString2,MyString1))
else:
	print("NO,string '{0}' is not present in string {1} " .format(MyString2, MyString1) )
