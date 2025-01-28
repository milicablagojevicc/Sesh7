s1 = "banana"
s2 = "banana"

print(s1 == s2) #True

s2 = "Banana"
print(s1 == s2) #False

print(s1 > s2) #True cuz b > B

s1 = "banana"
s2 = "banany"
print(s1 > s2) #False cuz a is not > y

s1 = "I went to see Jane"
s2 = "went"
print(s2 in s1) #True

print("ana" in "banana") #True
print("ANA" in "banana") #False