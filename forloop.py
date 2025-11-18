n=input("Enter a word")
print(n)
d={}
for ch in n:
    d[ch]=d.get(ch)+1
print(d)
for key, value in d.items():
    print(key,"occured",value,"times")

