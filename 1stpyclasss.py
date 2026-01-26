# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# d=int(input("enter a number"))
# e=int(input("enter a number"))
# choice=int(input("enter your choice for addition(1),subtraction(2),multiplication(3),division(4),logical(5),comparison(6)"))
# match choice:
#     case 1:
#         print("ADDITION IS:",a+b+c+d+e)
#     case 2:
#         print("SUBSTRACTION IS:",a-b-c-d-e)
#     case 3:
#         print("MULTIPLICATION IS:",a*b*c*d*e)
#     case 4:
#         if y==0:
#             print("ERROR")
#         else:
#             print("DIVISION IS:",a/b)
#     case 5:
#         print("Logical operation AND",a == b and b == c)
#         print("Logical operation OR:",a<=b or a>=b)
#         print("Logical operation NOT:",not a)
#         print("Logical operation NOT:",not b)
#     case 6:
#         print("Comparison Operator")
#         if a==b:
#             print("a=b")
#         elif a>=b:
#             print("a>=b")
#         elif a<=b:
#             print("a<=b")
#         elif(a!=b):
#             print("a!=b")


# DAY 2


# LOGIN AUTHENTICATION SYSTEM #2
# y=input("Do you want to sign in or sign up?")
# if y=="sign in":
#     bc=input("Enter your username:")
#     bd=input("Enter your password:")
#     cd=input("Confirm your password")
#     if bd==cd:
#         print("login successfully")
#     else:
#         print("Try again!!")

# else:
#     new=input("Enter your username:")
#     newpw=input("Enter your password:")


# a=input("Confirm your username:")
# b=input("Confirm your password")

# if new==a and newpw==b:
#     print("Signed up successfully")
# elif new==a and newpw!=b:
#     print("Invalid password")
# elif new!=a and newpw==b:
#     print("Invalid Username")


# Income tax calculator
# a=int(input("Enter your ANNUAL INCOME"))
# if a<250000:
#     print("no tax needed")
# elif a>250000 and a<500000:
#     print("5% tax included")
#     print("your tax included is:", tax = (a - 250000) * 0.05)
# elif a>500000 and a<1000000:
#     print("tax 20% included")
#     print("your tax included is:", (250000 * 0.05) + (a - 500000) * 0.20)
# elif a>1000000:
#     print("tax 30% included")
#     print("your tax included is:",(250000 * 0.05) + (500000 * 0.20) + (a - 1000000) * 0.30)


# day 3
# total=0
# for i in range(1,31,2):
#     print(i)
# for i in range(2,31,2):
#     print(i)

# n = 3
# for i in range(1, 11):
#     mul = n * i
#     print(f"{n} x {i} = {mul}")

# print("hello world")


# cpin = 2598
# i = 0
# while i != 3:
#     pin = int(input("enter your pin"))
#     if pin == cpin:
#         print("Access granted")
#         break
#     else:
#         print("Try again")
#         if i == 2:
#             print("!!Card blocked!!")

#     i += 1


# def add(a, b, *args):
#     total = 0
#     for num in args:
#         total = total + num + a + b
#     return total


# x = add(1, 2, 3, 4)
# print(x)

# name = ["anuj", "creation", "pragyan", "aryan"]
# print(name)
# name.append("thecho")
# caste = ("maharjan", "shrestha")
# username = "Creation,Shrestha"
# print(username.split(","))


# order_list = {"order_name": []}
# print("1.momo\n2.chowmein\n3.fried rice\n")
# while True:

#     choice = int(input("Enter your choice:"))
#     match choice:
#         case 1:
#             print("you have ordered momo")
#             order_list["order_name"].append("momo")
#         case 2:
#             print("you have ordered chowmein")
#             order_list["order_name"].append("chowmein")
#         case 3:
#             print("you have ordered fried rice")
#             order_list["order_name"].append("fried rice")
#         case 4:
#             print("Thank you!!")
#             print("your order is:")
#             for i, value in enumerate(order_list["order_name"]):
#                 print(f"{i+1}.{value}")
#             break

# inventory = ["laptop", "mouse", "keyboard"]
# inventory.insert(1, "webcam")
# inventory.sort()
# inventory.remove("mouse")
# print(inventory.pop())

cafeteria_menu = {"snacks": ["panipuri"], "drinks": ["coke"]}

cafeteria_menu["drinks"].append("chiya")
print(cafeteria_menu)
# creation shrestha
