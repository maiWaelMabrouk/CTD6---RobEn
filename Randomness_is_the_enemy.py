from CTD6 import*
print(''' Welcom to the game!
Remember, you have 3 bags and you can only remove from 1 to 5 objects each turn.
The computer will not let you to win!
LETS GO!''')

def Game(username):
    bags=[[1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0]]
    bag1=bags[0]
    bag2=bags[1]
    bag3=bags[2]
    while True :
        BagesLength(bag1,bag2,bag3)
        Human(bags)
        if bags == [[],[],[]]:
            BagesLength(bag1,bag2,bag3)
            GameWin(username)
            break
        BagesLength(bag1,bag2,bag3)
        Computer(bags)
        if bags == [[],[],[]]:
            BagesLength(bag1,bag2,bag3)
            GameLost(username)
            break
    
    
Game(input("Username: "))

