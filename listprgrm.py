list=['apple','orange','banana','grape','kiwi']
print(list)
a=int(input("choose from 1 to 6"))
if a==1:
    n=input("element to be append")
    list.append(n)
    print(list)
    print(list.append(input("enter the element")))
elif a==2:
    position=int(input("position to be inserted;"))
    if position<=len(list):
       b=input("element to be inserted")
       list.insert(position,b)
       print(list)
    else:
        print("invalid option")
elif a==3:
    list.sort()
    print(list)
elif a==4:
    list.pop()
    print(list)
elif a==5:
    c=input("element to be deleted")
    list.remove(c)
    print(list)
elif a==6:
    print(list[::-1])
elif a>8 or a<1:
    print("Invalid opyion")
elif a==7:
    exit()


