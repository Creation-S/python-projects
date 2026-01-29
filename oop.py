class Dog:
    species = "Mammal"

    def bark(self):
        return f"Dog barks"


d = Dog()
print(d.bark())


# Constructor
# __init__
# class student:
#     def __init__(self):
#         print("constructor is called")

# s1 = student()


# class Student:
#     def __init__(self, name, age, phone):
#         self.name = name
#         self.age = age
#         self.phone = phone


# s2 = Student("Creation", 19, 9848754388)
# print(s2.name, s2.age, s2.phone)


class Studata:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone


students = []
for i in range(3):
    a = input("Enter a student name")
    b = int(input("Enter age:"))
    c = int(input("Enter phone:"))

    students.append(Studata(a, b, c))

for s in students:
    print(s.name, s.age, s.phone)
