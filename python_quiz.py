print("Welcome to python quiz")
playing=input("Do you  want to play :")
if playing.lower()!="yes" :
    quit()
print("okay! Lets play.....")
score=0
answer=input("who developed python")
if answer.lower()=="guido van rossum" :
    print("correct answer")
    score=+1
else:
    print("incorrect answer!")
answer=input("what is the correct extension of python file")
if answer.lower()==".py":
    print("correct answer")
    score=+1
else:print("incorrect answer")