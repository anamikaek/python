n=input("Enter a sentence ")
a=['a','e','i','o','u']
digits=1,2,3,4,5,6,7,8,9,0
vowel=0
digit=0
space=0
for i in (n):
    if i in a:
        vowel+=1
    elif i in digits:
        digit+=1
    elif i==" ":
        space+=1
print("no.of vowels=",vowel)
print("no.of digits=",digit)
print("no.of space",space)


