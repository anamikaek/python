n=input("Enter a sentence ")
a=['a','e','i','o','u']
list_1=[]
for i in (n):
    if i in a and i not in list_1:
        list_1.append(i)
print(len(list_1))