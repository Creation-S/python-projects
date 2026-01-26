import math
name1=input("who do you want to compare your age with?")
age1=int(input("input the age of the person"))
name2=input("name of the second person")
age2=int(input("age of the second person"))
if(age1>age2):
    print(f"{name1} is greater than {name2}")
else:
    print(f"{name2} is greater than {name1}")
print(max(age1,age2))
reverse=input("print name to reverse it")
river=reverse[::-1]
print(river)