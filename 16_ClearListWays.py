# 16. Different ways to clear a list in Python
# method-1

# GEEK = [6, 0, 4, 1]
# print('GEEK before clear:', GEEK)
#
# GEEK.clear()
# print('list clear:', GEEK)

# method-2

# list = [{1, 2}, ('a'), ['1.1', '2.2']]
#
# # clearing the list
# del list[:]
#
# print('List:', list)

# method-3

list = ['Mon', 'Tue', 'Wed', 'Thu']
print("Existing list\n",list)
# Removing all elements
list *= 0
print("After deleting all elements\n")
print(list)