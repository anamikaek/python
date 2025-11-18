s = "3a4b2c"
output = ""

for i in range(0, len(s), 2):
    num = int(s[i])
    char = s[i+1]
    output += char * num

print(output)



       