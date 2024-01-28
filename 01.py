print("Welcome to the quiz!")

playing=input("Do you want to play? : ")
if playing.lower()!="yes":
    quit()

print("Okay! Let's play: ")
score=0

answer = input("What does CPU Stand for?: ")
if answer == "Central Processing Unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer1 = input("What does GPU Stand for?: ")
if answer1 == "Graphics Processing Unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer2 = input("What does RAM Stand for?: ")
if answer2 == "Random Access Memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer3 = input("What does PSU Stand for?: ")
if answer3 == "Power Supply Unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print("Your final score is: " + str(score) )