import random

attempts_list = []


def show_score():

    return

def start_game():
    attempts = 0
    rand_num = random.randint(1,10)
    print("Hello! Welcome to the game of Number guessing....")
    player_name = input("Please Enter your name? ")
    wanna_play = input(
        f'Hi, {player_name}, would you like to play '
        f'the guessing game? (Enter Yes/No): ')
    
    if wanna_play != 'yes':
        print("That's cool! Thanks")
    else:
        show_score()

    while wanna_play.lower() == 'yes':
        try:
            guess = int(input("Pick a number between 1 to 10: "))
            if guess < 1 or guess > 10:
                raise ValueError('Please Guess a number between the given range')
            
            attempts += 1
            attempts_list.append(attempts)

            if guess == rand_num:
                print("Nice! you got it")
                print(f"It tooks you {attempts} attempts")
                wanna_play = input("Would you like to play again? (Enter yes/no): ")

                if wanna_play.lower() != 'yes':
                    print("That's cool! Have a good one!")
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1,10)
                    show_score()
                    continue
            else:
                if guess > rand_num:
                    print("It's lower")
                elif guess < rand_num:
                    print("It't higher")

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)




if __name__ == '__main__':
    start_game()
