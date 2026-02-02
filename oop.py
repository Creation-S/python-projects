# class Dog:
#     species = "Mammal"

#     def bark(self):
#         return f"Dog barks"


# d = Dog()
# print(d.bark())


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


# class Studata:
#     def __init__(self, name, age, phone):
#         self.name = name
#         self.age = age
#         self.phone = phone


# students = []
# for i in range(3):
#     a = input("Enter a student name")
#     b = int(input("Enter age:"))
#     c = int(input("Enter phone:"))

#     students.append(Studata(a, b, c))

# for s in students:
#     print(s.name, s.age, s.phone)

# INHERITANCE


# class Animal:
#     def sounds(self):
#         print("Animal makes sound")


# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")


# d = Dog()
# d.sound()
# d.sounds()


# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def display(self):
#         print(f"{self.name},{self.age},{self.address}")


# class Employees(Person):
#     def __init__(self):
#         x = input("Enter the name")
#         y = input("Enter the age")
#         z = input("Enter the address")
#         super().__init__(x, y, z)


# e = Employees()
# e.display()


# class Member:
#     def __init__(self, name, mem_id):
#         self.name = name
#         self.mem_id = mem_id


# class Students(Member):
#     def __init__(self, name, mem_id, grade):
#         super().__init__(name, mem_id)
#         self.grade = grade

#     def display(self):
#         print(f"{self.name},{self.mem_id},{self.grade}")


# name = input("Enter name")
# mem = input("Enter id")
# grade = input("Enter grade")
# x = Students(name, mem, grade)
# x.display()

# ENCAPSULATION
"""
Access Specifiers
private(__)
protected(_)
Default/public

"""
