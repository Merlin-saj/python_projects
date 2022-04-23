name=input("type your name")
print("\n welcome",name,"to this adventure")
answer=input("\n You are on a dirty road,it has come to an end and you can go left or right,which way you wanna go?").lower()
if answer=="left":
    answer=input("\n you can cross a river, you can walk around it or swim across. Type walk if you want walk around or type swim")
    if answer=="swim":
        print("\n You swim across the river and were eaten by an alligator")
    elif answer=="walk":
        print("\n You walked miles and ran out of water and lost the game!")
    else:
        print("\n Not a valid option. You loose")
elif answer=="right":
    answer=input("\n You came across a bridge, it looks wobbly, do you want to cross it or head back(cross/back)?")
    if answer=="back":
        print("\n You go back and lose")
    if answer=="cross":
        answer=input("\n You cross the bridge and met a stranger. Do you want to talk to him(yes/no)")
        print("\n You cross the bridge and met a stranger. Do you want to talk to him(yes/no)")
        if answer=="yes":
            print(" \n You talk to the stranger and they gift you the treasure and you won!!")
        elif answer=="no":
            print("\n you ignore the stranger and they get offended and you lose...")
        else:
            print("\n invalid option you lose")
    else:
        print("\n invalid option you lose")
else:
    print("\n invalid option please try again...")
print("\n Thank you for trying ",name)