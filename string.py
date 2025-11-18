n=input("Enter a word: ")
d={}
for ch in n:
    d[ch] = n.count(ch)
print(d)
print(id(n))