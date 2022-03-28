# num1 = int(input("Enter a number:\n"))
# num2 = int(input("Enter another number:\n"))

# solution = num1*num2
# print(f"The multiplication result of {num1} and {num2} is {solution}")

#Use the print() funtion to format thegiven words in the mentionedformat. Display the ** seperator between them
# name1 = 'Name'
# name2 = 'Is'
# name3 = 'James'
# print(f"{name1}**{name2}**{name3}")


# my_string = "this is a string"
# print(my_string.lower())

# print(my_string.rindex("s",2,4))

# name = "Hello world"
# print(name)
# x = 1
# print(x + 5)

# r = 5
# pi = 3.142
# print(((3/4)*pi*r)**3)

# bookprice = 24.95
# print(60 * bookprice)



# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
#tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home?
# start_time = ((6*60)+52)*60
# easy_time = ((8*60)+15)*2
# tempo_time = ((7*60)+12)*3

# food_hour = (start_time + easy_time + tempo_time) / 3600

# food_hour_int = int(food_hour)
# food_min = (food_hour - food_hour_int)*60
# print(f"breakfast time is {food_hour_int}:{int(food_min)}am")

# def add_numbers():
#     print(5+5)

# add_numbers()

# print(type("5"))

# from math import sqrt
# print(sqrt(25))
#the function called (len) tells us the length of a string
#With (lambda) we can represent a single line of function

#Write a program that takes the score of the students as an input from the teacher seperated by comma...
#Use the information to calculate the standard deviation, the mean average, the variance and the range



num = input("write your score\n")
b = num.split(",")
dust = list(map(int,b))
print(dust)
#mean
mean_avr = sum(dust)/len(dust)
print(f"Mean average: {mean_avr}")
#Rnage
ran = max(dust) - min(dust)
print(f"Range: {ran}")
#standard deviation
x_mean = map(lambda x : (x-mean_avr)**2, dust)
stan_dev = (sum(x_mean)/len(dust))**1/2
print(f"Standard deviation: {stan_dev}")
#Variance
var = stan_dev**2
print(f"Variance: {var}")
