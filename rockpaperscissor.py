
def game(player1,player2):
    while(player1 and player2) == "yes":
        player1 = input("%s choose your option % player1")
        player2 = input("%s choose your option % player2")
        if player1 == player2:
            print("draw")
        elif player1  == "rock":
           if player2  == "scissors":
                print("%s congratulations you won"%p2)
           else:
                print("%s congratulations you won"%p1)
        elif player1  == "paper":
           if player2== "rock":
                print("%s congratulations you won"%p2)
           else:
                print("%s congratulations you won"%p1)
        elif player1  == "scissor":
           if player2 == "paper":
                print("%s congratulations you won"%p2)
           else:
                print("%s congratulations you won"%p1)
        else:
            print ("invalid game")
        print("you want to continue the game?")
        player1 = input("%s enter your choice yes or no" %p1)
        player2 = input("%s enter your choice yes or no" %p2)


p1= input("enter your name")
p2= input("enter your name")
print("you want to play the game?")
player1 = input("%s enter your choice yes or no" %p1)
player2 = input("%s enter your choice yes or no" %p2)
print (game(player1,player2))
