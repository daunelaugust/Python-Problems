import random
import time

game = input("To start the game enter 1, to end game enter 0: ")
score = {"User": 0, "Computer": 0, "Tie": 0 }
while (game != "1") and (game != "0"):
    #Invalid input doesnt start game only works for integers as of now
    # this code breaks when game is not int, need to work a try except into here
    print("PLEASE TRY AGAIN INVALID INPUT")
    game = input("To start the game enter 1, to end game enter 0: ")
else:
    
    while bool(int(game)):
        #starts game if user enters 1
        user = " "
        user = input("Enter your choice (rock/paper/scissors): ")
        
        # Computer selects random integer between 1 and 3
        Computer = random.randint(1,3)
        
        # Sets 1 to Rock, 2 to Paper, 3 to Scissors
        if Computer == 1:
            comp_status = "rock"
        elif Computer == 2:
            comp_status = "paper"
        if Computer == 3:
            comp_status = "scissors" 
        
        # Sets condtions of game results depending on user inputs and computer random selection
        if user == comp_status:
            status = "Bruh a Tie!"
            score["Tie"] +=1
        elif (user == "rock" and comp_status == "scissors") or (user == "scissors" and comp_status == "paper") or (user == "paper" and comp_status == "rock"):
            status = "User wins !"
            score["User"] +=1
        else:
            status = "Computer wins!!!"
            score["Computer"] +=1
        
        # Delays  Printing Computer selection for nice effect
        time.sleep(0.5) 
        print(" ")
        print("Computer selects "+comp_status)
        print(" ")
        time.sleep(0.5) 
        # Delays Printing result for nice effect
        print("The result:  " + status)
        print(" ")
         # Delays Printing score for nice effect
        time.sleep(0.25) 
        print(score)
        print(" ")
        game = input("To start a new game enter 1, to end game enter 0: ")
        print(" ")
    else:
        # prints score and ends game if user inputs 0
        time.sleep(1)
        print(" ")
        print("The game has ended the final score is:")
        print(score)
        print(" ")
        #Picks winner of game depending on final score
        if score["User"] == score["Computer"] or (max(score, key=score.get) == "Tie"):
            print("The Game ends in a Tie")
        else:
            print(max(score, key=score.get)+ " Wins the Game!!!")
    


    
        
    
    
