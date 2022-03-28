


# val = "This is a string"

# string concatination
# a = "2"
# b = "2"
# print(2 +2)

# string indexing
# val = "My name "
# val2 = "is Daniel"
# print(val + val2)
# print(val[3])

# string slicing
# name = "Harry maguire"
# print(name[3:8])
# print(name[5])
# print(name[4:9:2])

#string formatting
# a = 14
# b = 35
# print(f"The sum of{a} and {b} is {a + b}")

#escape characters
# print('I am my mother\'s son')
# print("Joseph said, \"I cannot do this anymore\".")

#string method
#title method


#only first letters
import string


my_string = "this is a string"
print(my_string.title())

#upper method
my_string = "this is a string"
print(my_string.upper())

#loweremethod
my_string = "this is a string"
print(my_string.lower())

print(my_string.rindex("s",3,7))
print(my_string.rfind("z",3,4))

num = True
print(int(num))
ans = 0
print(bool(ans))

girl = 'adim'
print(string.format())
#Write a program that calculates the
#  area of a square. Allow the program to take thedimensions from the user

# lenght = int(input("Enter the length of a square\n"))
# print(f"The area of a square with length of {lenght}cm is {lenght**2}cm²")

# #write a programthat calculates the simple interest. Tell the user to give the you the details
# p = int(input("Initial capital:\n>"))
# r = int(input("Rate (in percentage e.g 80 for 80%):\n"))
# t = int(input("Time in years:\n"))

# r/=100

# interest = p*r*t
# print(f"Investing ${p} at a rate of {r*100}% would give an interest of {interest} after {t} years")


#Write a program that takes in the first name and the last name of an individual and creates s new username for him/her
# name = (input("Enter you first name\n"))

# name2 = (input("Enter your last name\n"))

# firstname = (name[0:3])
# lastname = (name2[0:3])

# username = (firstname + lastname)
# username = username.lower()
# print(f"Your username is {username}")

loving = ['heart' ,'soul' ,'mind']
'heart' in loving