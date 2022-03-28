# length = int(input("Enter the length of the square\n"))

# print(f"The area of the square with {length}cm is {length**2}cm²")

P = int(input("Enter the principal given:\n"))
R = int(input("Enter the rate given:\n"))
T = int(input("Enter the time given:\n"))

R/=100

interest = P*R*T
print(f"Investing with ${P} at {R}% will yield {interest} within {T}years")

name = (input("Enter you first name\n"))

name2 = (input("Enter your last name\n"))

firstname = (name[0:3])
lastname = (name2[0:3])

username = (firstname + lastname)
username = username.title()
print(f"Your username is {username}")