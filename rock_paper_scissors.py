# rock paper scissors game

import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors \n" )
    computer = random.choice(['r','p','s'])
    if user == computer:
        return 'It\'s tie! Both of you selected same'
    
    if is_win(user,computer):
        return f'you won! Because computer selected {computer}'
    return f'you loss! Because computer selected {computer}'
    

def is_win(user,computer):
    #  r > s, s > p, p > r
    if(user == 'r' and  computer == 's') or (user == 's' and  computer == 'p') or (user == 'p' and  computer == 'r'):
        return True
    

print(play())