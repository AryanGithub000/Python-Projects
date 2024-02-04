name = input("Enter you name: ")
print("Welcome",name,"to this adventure!")

answer = input("You are on a dirt road,it had come to ane dn so go either L or R, whered you going? \n").lower()

if answer=="l":
    answer=input("You come to a river, you can walk aroun dit or swin across? Type W to walk around and S to swim across!").lower()
    if answer=="s":
        print("You swam across and were eaten by an alligator!")
    elif answer=="w":
        print("You walked for many miles! Ran out of water and lost the game.")
    else:
        print("YOU LOSE!!!")

elif answer=="r":
    answer=input("You come to a bridge, it looks wobbly! Wanna cross or head back?? (C->Cross / B->Back)").lower()
    if answer=="c":
        print("You crossed the bridge and met a stranger? Talk or not (T)")
        answer=input()
        if answer=='t':
            print("The stranger gives you gold and you WON! wohoo")
        else:
            print("YOU LOOSE!!")
    elif answer=="b":
        print("You came back and are now on the main road!")
    else:
        print("YOU LOSE!!!")
    
else:
    print("YOU LOSE!!!")