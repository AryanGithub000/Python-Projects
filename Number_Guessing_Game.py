import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)  # Typecasting

    if top_of_range <= 0:
        print("Please type a number greater than zero!")
        quit()
else:
    print("Please type a number next time!")
    quit()

random_number = random.randrange(0, top_of_range)
count=0
#print(random_number)

while True:
    count+=1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)  # Typecasting
    else:
        print("Please type a number next time!")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess>random_number:
        print("Guess lower!")
    else:
        print("Guess higher!")

print("You got it in",count,"guesses")
