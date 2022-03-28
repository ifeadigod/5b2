#Write a program that takes the score of the students as an input from the teacher seperated by comma...
#Use the information to calculate the standard deviation, the mean average, the variance and the range

num = input("write your score\n")
bast = num.split(",")
lil = list(map(int, bast))
print(lil)
#mean average
avr = sum(lil) / len(lil)
print(f"Mean average: {avr}")
#range
range = max(lil) - min(lil)
print(f"range: {range}")
#standard deviation
mean2 = map(lambda x: (x-avr)**2, lil)
std = sum(mean2) / len(lil)**1/2
print(f"Standard deviation: {std}")
#Variance
from math import sqrt
var = (sqrt(std))
print(f"variance: {var}")