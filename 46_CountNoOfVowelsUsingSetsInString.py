# Python3 code to count vowel in
# method-1

# Function to count vowel
str = "sushant"
def vowel_count(str):
    count = 0
    vowel = set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
    print("No. of vowels :", count,)
vowel_count(str)

# method-2

word=input("Enter a word: ")
vowels={'a','e','i''o','u'}
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print(f'{k} occurred {v} times')


