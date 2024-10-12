import random as r

print("\nWELCOME TO 'ROCK,PAPER,SCISSORS' GAME !")
print("_______________________________________\n")
print("You are going to play against a computer. Whoever has the highest score at the end of the rounds will win the game.")
print("\nFollowing are the rules of the game:")
print("1. Rock beats Scissors\n2. Scissors beat Paper\n3. Paper beats Rock")
game = ['rock', 'paper', 'scissors']
name = input("\nEnter Your Name: ")
flag = True
while flag:
    user_score = 0
    comp_score = 0
    try:
        rounds = int(input("\nEnter the number of rounds (Enter 0 to exit): "))
        if rounds == 0:
            flag = False
        elif rounds > 0:
            while rounds:
                user_choice = input("\nRock, Paper, or Scissors: ").lower()
                if user_choice not in game:
                    print("Choose a valid option (rock, paper, or scissors)!")
                    continue
                comp_choice = r.choice(game)
                print("Computer chose:",comp_choice)
                if user_choice == comp_choice:
                    print("It's a DRAW!")
                elif (user_choice == 'rock' and comp_choice == 'scissors') or(user_choice == 'scissors' and comp_choice == 'paper') or (user_choice == 'paper' and comp_choice == 'rock'):
                    user_score += 1
                    print(name,"Wins this round!")
                else:
                    comp_score += 1
                    print("Computer Wins this round!")
                print("Score -> ",name,":",user_score,"Computer:",comp_score)
                rounds -= 1
            print("\nFinal Score:")
            print("Score -> ",name,":",user_score,"Computer:",comp_score)
            if user_score > comp_score:
                print("\nCongratulations",name,", You Win the Game!")
            elif comp_score > user_score:
                print("Computer Wins the Game!")
            else:
                print("It's a Draw!")
    
        else:
            print("Please enter a positive number of rounds.")
    
    except ValueError:
        print("Please enter a valid number of rounds!")

print("Thank you for playing!")
