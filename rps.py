import random
import time

game = input("To start the game enter 1, to end game enter 0: ")
score = {"User": 0, "Computer": 0, "Tie": 0 }
while (game != "1") and (game != "0"):
    #Invalid input doesnt start game only works for integers as of now
    print("PLEASE TRY AGAIN INVALID INPUT")
    game = input("To start the game enter 1, to end game enter 0: ")
else:
    
    while bool(int(game)):
        user = " "
        user = input("Enter your choice (rock/paper/scissors): ")

        Computer = random.randint(1,3)

        if Computer == 1:
            comp_status = "rock"
        elif Computer == 2:
            comp_status = "paper"
        if Computer == 3:
            comp_status = "scissors" 
    
        if user == comp_status:
            status = " Bruh a Tie"
            score["Tie"] +=1
        elif (user == "rock" and comp_status == "scissors") or (user == "scissors" and comp_status == "paper") or (user == "paper" and comp_status == "rock"):
            status = "User wins !"
            score["User"] +=1
        else:
            status = "Computer wins !"
            score["Computer"] +=1
        time.sleep(1) 
        print(" ")
        print("Computer selects "+comp_status)
        print(" ")
        time.sleep(0.5) 
        print("The result is " + status)
        print(" ")
        print(score)
        print(" ")
        game = input("To start a new game enter 1, to end game enter 0: ")
    else:
        time.sleep(1)
        print("The game has ended the final score is:")
        print(" ")
        print(" ")
        print(score)


    