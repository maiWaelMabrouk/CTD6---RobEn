#include????? walahy 7aram 3alya
import random
import cv2
import numpy as np


    #the function of human turn
def Human(bags):
    bag=input("select a bag: ") 
    onum=input("select number of objects: ")
    while CheckRules(bag,onum,bags) is False:
        bag=input("select a bag: ") 
        onum=input("select number of objects: ")
    bag = int(bag)-1
    onum = int(onum)
    Turn(bags,bag,onum)
    print("\nyou removed ",onum,"from bag ",bag+1)
    
# check about the general rules and the rubbish inputs
def CheckRules(bag,onum,bags):
    if not bag.isdigit():
        print("Only integer numbers are allowed")
        return False
    elif not onum.isdigit():
        print("Only integer numbers are allowed")
        return False
    elif int(bag) not in [1,2,3]:
        print("Please select a correct number for the bag")
        return False
    elif int(onum) not in [1,2,3,4,5]:
        print("Please select correct object number")
        return False
    elif len(bags[int(bag)-1])<(int(onum)) or bags[int(bag)-1] == []:
        print("There is not enough objects in the bag")
        return False
    else:
        return True


#Computer turn function
def Computer(bags):
    while True:
        bag = random.choice(bags)
        bag = bags.index(bag)
        if bags[bag]==[]:
            continue
        break
    while True:
        onum = random.choice(bags[bag])
        onum = bags[bag].index(onum)+1
        if len(bags[bag])<onum or onum>5:
            continue
        break
    Turn(bags,bag,onum)
    print("The computer removed ",onum,"from bag ",bag+1)


#the game turn function   
def Turn(list,bag,onum):
    i=0
    while i<onum:
        list[bag].pop(-1)
        i+=1

#print the numbers of each bag
def BagesLength(bag1,bag2,bag3):
    print("\n",len(bag1)," - ",len(bag2)," - ",len(bag3),'\n')

#image display win
def GameWin(username):
    img = np.zeros((200,620,3), np.uint8)
    #cv2.imshow('black image', img)      
    # Window name in which image is displayed
    window_name = 'End of Game'
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 100)
    fontScale = 1
    color = (0, 255, 255)
    thickness = 2
    # Using cv2.putText() method
    image = cv2.putText(img,"Congratulations "+username+", you won!!!", org, font,
                    fontScale, color, thickness, cv2.LINE_AA)
    # Displaying the image
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

#image display lose
def GameLost(username):
    img = np.zeros((200,620,3), np.uint8)
    #cv2.imshow('black image', img)      
    # Window name in which image is displayed
    window_name = 'End of Game'
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 100)
    fontScale = 1
    color = (255, 200, 10)
    thickness = 2
    # Using cv2.putText() method
    image = cv2.putText(img, "Unfortunately "+username+", you lost!!!" ,org, font,
                    fontScale, color, thickness, cv2.LINE_AA)
    # Displaying the image
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
