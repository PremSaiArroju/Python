import random

def rock_paper_scissors():

    user = input("R for Rock, P for Paper, S for Scissors: ")
    if user not in ['R','S','P']:
        return "Play Fair! Bro"

    computer =  random.choice(['R','P','S'])
    print("User's choice is: ",user)
    print("Computer's choice is: ",computer)

# r > s, s > p, p > r are winning choices in the game

    if(user==computer):
        return "Ooohh!! It's Tie"
    
    if is_win(user,computer):
        return "Yaaayyy! You Won!"
    
    return "Oh Looooser!"
    

def is_win(player,opponent):
    if(player=='R' and player=='S') or (player=='S' and player=='P') or (player=='P' and player=='R'):
        return True

print(rock_paper_scissors())
