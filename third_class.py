# def add_numbers():
#     print(5+5)

# add_numbers()

# print(type("5"))

# from ast import Lambda
# from calendar import c
# from math import sqrt
# from re import A, X
# print(sqrt(25))
#the function called (len) tells us the length of a string
#With (lambda) we can represent a single line of function

# a = lambda x : 4*x -3
# b = lambda x : 3*x + 4

# c = a(b(-2))
#print(c)
# pi = 3.142
# A = lambda r : pi*r**2
# print(A(2))

# pi = 3.142
# volume = lambda r : pi*r**3
# print(volume(12))

# A = lambda c = (3*(c**2))
# print(A(3))

#A global variable is the variable that is usaually asigned anywhere and can be located anywhere
# def test_func():
#     global x
#     x = 5
# test_func()
#     print(x)


#A local variable is the variable that is within the scope
# def test_func():
     
#     x = 5

# print(x)

#parameters are used when you are defining your function
#Arguements are used when you are calling the function

# def add_num(a,b):
#     print(a+b)
# add_num(12,13)  

# def file(name, age):
#     print(name,age)

# file("Daniel",18)

# show_emoloyee1 = (input("Emter your any employee name\n"))
# show_emoloyee2 = (input("Enter your salary\n")) 

# show_emoloyee = show_emoloyee1 + show_emoloyee2
# print(show_emoloyee)

# def show_employee(name, salary=9000):
#     print("Name:" + name + "Salary:" + salary)

# show_employee("Ben",1200)
# show_employee("harry")

#Types of arguement
# positional arguement
# def print_twice(bruce, alex):
#     print(bruce)
#     print(alex)
# print_twice("star")

#keyword arguements 
# def print_twice(bruce, alex):
#     print(bruce)
#     print(alex)
# print_twice(alex="a")

#string methods
# def minus(a, b=3):
#     print(a-b)
# minus(8)    
#split
#a = "Ada is a dog"
#print(a.split(","))
#join
# a = ['a','quick','brown','fox','just','died.']
# b = " ".join(a)
# #replace
# print(b.replace("brown","white"))


# arr = [1,2,3,4,5,6]

# mapped = map(lambda y : y**2, arr)
# print(min(mapped))

#Write a function with a list of numbers and let it find the average and the range
#average
arr = [1,2,3,4,5,6]
vibe = sum(arr)
print(vibe/6)
#range
ran = max(arr) - min(arr)
print(ran)

#write a program that takes the input from the user(numbers)...get them into a list
num = input("write some numbers\n")
b = num.split(",")
mapped = list(map(int,b))
print(mapped)
