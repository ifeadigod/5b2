import random
from secrets import choice
from unittest import result
# a = [3,2,5,6,8,7]

# print(f"select any number from {a}.\nWe hope it doesn't end in tears.")
# com_choice = random.choice(a)
# random.shuffle(a)
# print('Guess the number:')
# user_choice = int(input(">"))

# if user_choice in a:
#     if user_choice == com_choice:
#         print("All power belongs to you comrade.")
#     else:
#         print("Arhh, comrade. Be like say you go try again o.")
# else:
#     print("comrade no be so!")


# items = ['rock','paper','sissors']

# print("let's play a game of rock, paper & sissors")
# com_choice = random.choice(items)
# random.shuffle(items)
# print("Game on!!")
# user_choice = input(">")

# if user_choice == com_choice:
#         print("Its a tie")
# elif user_choice == 'rock' and com_choice == 'paper':
#         print('paper covered rock...You loose')
# elif user_choice == 'paper' and com_choice == 'rock':
#         print('You win...Nice work ')
# elif user_choice == 'scissors' and com_choice == 'paper':
#         print('You win...nice work')
# elif user_choice == 'paper' and com_choice == 'scissors':
#         print('scissors cuts paper...You loose')
# elif user_choice == 'rock' and com_choice == 'scissors':
#         print('You win...Nice work')
# elif user_choice == 'scissors' and com_choice == 'rock':
#         print('Rock smashes scissors...You loose')


def check_winner(player_choice, com_choice):
    if player_choice == "rock" and com_choice == "scissors":
        return "You win"
    elif player_choice == "paper" and com_choice == "rock":
        return "You win"
    elif player_choice == "scissors" and com_choice == "paper":
        return "You win"
    elif player_choice == "paper" and com_choice == "scissors":
        return "computer wins"
    elif player_choice == "scissors" and com_choice == "rock":
        return "computer wins"
    elif player_choice == "rock" and com_choice == "paper":
        return "computer wins"
    else:
        return "It's a  tie"

choices = ['rock', 'paper', 'scissors']
print("let's play a game of rock, paper & sissors.\nGame on!!")
com_choice = random.choice(choices)
player_choice = input(">").lower()

if player_choice in choices:
    result = check_winner(player_choice, com_choice)

    print(result)
    print(f"Computer selected {com_choice}")
else:
    print('Invalid input')

