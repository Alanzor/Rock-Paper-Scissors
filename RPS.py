import random
import sys





    
    
def get_robot_answer(): 
    return random.choice(["r","p", "s"]) # Returns a random choice of rock paper sciscors 


def get_user_answer():
    while True:
        userAnswer = input().lower()
        if userAnswer in ["r", "p", "s"]: #ensure user answer is valid and forces lowercase
            return userAnswer
        print("Please select r for rock, p for paper, or s for scissors: ")
        
def get_win_num():
  """Returns an integer value entered by the user."""
  while True:
    win_num = input("Enter a number: ")
    try:
      win_num = int(win_num)
      return win_num
    except ValueError:
      print("Please enter a valid integer.")
            

def get_user_input(): # handles if the user wants to play
  while True:
    userInswer = input()
    if userInswer in ("Y", "y"):
      return True
    elif userInswer in ("N", "n"):
      sys.exit()

    print("Please choose Y for yes or N for no")
    
 

def main():
    print("Welcome to Rock Paper Scissors! Would you like to play? Y/N? ")



    userInput = get_user_input() #checks if want to play or keep playing
    
    while True:
        
        print("How many points to win?")
        
        games_to_win = get_win_num()
        
        player_score = 0
        robot_score = 0
        
        
        while True: #keeps playing until user or robot have games to win
            robotChoice = get_robot_answer()
            print("Press r for rock, p for paper, or s for scissors:")
            userChoice = get_user_answer() 
                                            # We check for user Tie win lose 
            if userChoice == robotChoice:
                print("TIE! You both chose: " + userChoice)
            
            elif userChoice == "r":
                if robotChoice == "s":
                    print("You Win!")
                    player_score += 1
                else:
                    print("You Lose!")
                    robot_score += 1
            
            elif userChoice == "s":
                if robotChoice == "p":
                    print("You Win!")
                    player_score += 1
                else:
                    print("You Lose!")
                    robot_score += 1
            
            else:
                if robotChoice == "r":
                    print("You Win!")
                    player_score += 1
                else:
                    print("You Lose!")
                    robot_score += 1
                    
                # Print the current scores.
            print(f"Your score is: {player_score}. The Robot's score is: {robot_score}.")
            
            if player_score == games_to_win:
                print(f" You won the best of series! Your score was: {player_score}. The Robot's score was: {robot_score}")
                break
            if robot_score == games_to_win:
                print(f" You lost the best of series! Your score was: {player_score}. The Robot's score was: {robot_score}")
                break
                
        
        
        print("Would you like to play again?")

        playAgainInput =  get_user_input()
        

     
     
if __name__ == "__main__":
  main()