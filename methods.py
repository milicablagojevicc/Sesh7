#methods are built in (pre-defined) operations that cna be performed (eg. "find")
methods = dir("Hi")
useful_methods = []
for method in methods:
    if "__" in method:
        continue
    useful_methods.append(method)
print(useful_methods)

print(help("hi".capitalize()))
s = 'i go to school every day'
print(s.capitalize())

print(help("".casefold))
print("I LiKE CakE".casefold())

print("hello".center(30, "_"))
print("banananananananana".count("ana"))

print("Ana ana banana".find("ana")) #Result is 0 because the first "ANA" is at position ZERO
print("Ana ana banana".find("ana", 5))
print("Ana ana banana".find("ana", 10))

print("abcdefg".index("b", 1))

words = ["i", "like", "to", "sing"]
print(" ".join(words))

#lower is the same as casefold

s = "I like to go hiking"
print(s.replace(" ", " !"))

s = "I like to go hiking!"
print(s.split())
s = "I like to go hiking!"
print(s.replace("!", " ").split())

print(s.upper())

punctuation = "!,?-/;:,"
sentence = "How , are you??, I dont like, this::?"
for p in punctuation:
    sentence = sentence.replace(p, "")
    print(sentence)

    ###Strings are inmutable
    #But can create new strings that uses the old string as a base
    #slicing creates a copy rather than changing the old
    