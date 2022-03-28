#Write a program that takes the score of the students as an input from the teacher seperated by comma



# from cmath import sqrt


# num = input("write your score\n")
# b = num.split(",")
# mapped = list(map(int,b))
# print(mapped)
# #average or mean score
# avr = sum(mapped)/len(mapped)
# print(f"Average: {avr}")
# #range
# ran = max(mapped) - min(mapped)
# print(f"Range: {ran}")
# #standard deviation
# x_mean  = map(lambda x : (x-avr)**2, mapped)
# std = sqrt(sum(x_mean)/len(mapped))
# print(f"Standard deviation: {std}")
# #variance
# variance = std**2
# print(variance)

#Write a program that takes the age from the user and tells him what year they were born
# age = int(input("what's your age\n"))
# current_year = 2022
# year = current_year - age
# print(f"The year you were born is {year}")

#FRUITFUL FUNCTIONS
#A fruitful function is a function that returnsa value
def add_num(a,b):
    print(a+b)
    return a+b
x = add_num(4,6)
print(x)

#recursive function
#This is a function that uses it's output as an input and kepp onrunning it over and over again
def factotial(n):
    if n == 1:
        return 1
    
    return n* factotial(n-1)

print(factotial(5))

#Asignment is to read chapter three and eight
















