import random
print("*********Thank You For Chosing My Game To Play*********")
GambleAgain = True
playAgain = True
while(playAgain == True):
    money = 500
    print("You have $500!")
    while(GambleAgain == True):
        amount = input("Enter the amount you want to gamble.")
        GambleAmount = int(amount)
        Decider = random.randrange(0,2)      
        if(0 < GambleAmount <= money):            
            if(Decider == 0):
                print("You Lose!")
                money = money - GambleAmount              
            elif(Decider == 1):
                print("You Win!")      
                money = money + GambleAmount
            else:
                print("There was an error in the program.")
            print("You have " + str(money))
            if(money > 0):          
                answer =input("Would you like to gamble again?").lower()
                if(answer == "yes" or answer == "y"):
                    GambleAgain = True
                else:
                    print("Thank you for playing.")
                    GambleAgain = False
            elif(money <= 0):
                print("You lost!")
                reply = input("Would you like to play again?").lower()
                if(reply=="yes" or reply == "y"):
                      money = 500
                      playAgain = True
                     
                else:
                      playAgain = False
                      GambleAgain = False
        else:
            print("Enter a valid amount")
            GambleAgain = True
print("Thank you for playing!")
playAgain = False
                    
                    
