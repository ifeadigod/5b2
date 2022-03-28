# v = ['n', 'C', 'B', 's', 'r', 'A']
# print(list(filter(lambda x:x.isupper(),v)))

# odd_num = input('write some odd numbers\n').split(",")
# num = map(int,odd_num)
# odd_int =filter(lambda x: x%2==1, num)
# print(list(odd_int))

# a = 'banana'
# b = 'banana'


# print(a==b)
# print(a is b)

# v = ['1','2','3']
# w = ['1','2','3']
# print(v==w)
# print(v is w)

# a = [4,7,9]
# b = a
# c = a.copy
# print(b is a)
# print(c is a)

# def middle(arr):
#     return arr[1:-1]

# a = [1,2,3,4,5,6,7]
# print(middle(a))


# def median(arr):
#     return arr[2:-2]

# v = [1,2,3,4,5,6,7]
# mid = median(v)
# print(sum(mid)/2)

# def median(arr):
#     arr.sort()
#     mid_point = len(arr)//2
#     if len(arr)%2==0:
#         return (arr[mid_point] + arr[mid_point-1]/2)

#     return arr[mid_point]

# a = [1,2,3,4,5]
# print(median(a))
#conditionals
#we normally make us of the if and else statement
#its a way of controling how a block of code will run
#with conditions a particular block of code will runif a particular condition is met

#boy = 'Daniel'
#name  = boy
# if boy == 'Daniel':
#     print('Daniel')
# else:
#     print('Not correct')

# score = 'win'
# if score > 100:
#     print('excellent')
# elif score == 100:
#     print('good')
# elif score < 100:
#     print('poor')
# else:
#     print('No score')


# score = input(int('Write your score\n'))

# if score <= 39:
#     print("f")
# elif score <=49:
#     print('E')
# elif score <= 59:
#     print('D')
# elif score <=69:

import random
a = [3,2,5,6,8,7]
while True:
    print(f"select any number from {a}.\nWe hope it doesn't end in tears.")
    com_choice = random.choice(a)
    random.shuffle(a)
    print('Guess the number:')
    user_choice = int(input(">"))
    
    if user_choice in a:
        if user_choice == com_choice:
            print("All power belongs to you comrade.")
        else:
            print("Arhh, comrade. Be like say you go try again o.")

    else:
        print("comrade no be so!")
    c = input("Do you want to continue\n").lower()
    if c == 'yes':
        continue
    else:
        break





# classwork
# Create a simple text search engine. It searches for a sub-string in a string and returns how many of that sub strings was found. Also it returns the whole string with the search keywords written in uppercase
# E.G  TEXT: "I am a boy"
#       SEARCH FOR:"am"

# Example output : 1 return was found
#                   I AM a very good boy

# SOLUTION

# text = 'this life no balance'
# sub_text = input("enter text to search for:\n").lower()

# lowercase_text = text.lower()
# found = lowercase_text.find(sub_text)
# count = lowercase_text.count(sub_text)

# if found  != -1:
#     print(f"{count} result(s) found!")
#     new_text = text.replace(sub_text,sub_text.upper())
#     print(new_text)
# else:
#     print(f"{count} result(s) found!")

# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)
# print(countdown(100))        


