s1 = "hello world"
print(s1)
print(s1[0], s1[1], s1[2])
print(s1[3], s1[4])
print(s1[6], s1[7])

s1 = "hello"
s2 = "world"

print(s1+ " " + s2 + "!")

if "bob":
    print("bob is")
else:
    print("bob is not")
if "":
    print("empty string is true")
else:
    print("empty string is false")

s = "abcdefghijklmnop"
print(len(s))
for character in s:
    print(character, end=" ")

i = 0 #the beginning index
while i < len(s):
    print(s[i], end=" ")
    i += 1


i = 0 #the beginning index
while i < len(s):
    print(s[len(s) - i - 1], end=" ")
    i += 1

    #slice is like a fancy index, with [], but also using multiple elements
s = "0123456789"
print(s)
print(s[2:3])
print(s[4:6])
print(s[:3])
print(s[3:])
print(s[1:7:2])
print(s[::-1])

