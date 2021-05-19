import random

print("Number Guessing Game")

number = random.randint(1, 9)

chances = 0

while chances < 5:
    guess = int(input("Enter your number: "))

    if guess == number:
        print("Congratulations! Your guess is right.")
        break

    elif guess < number:
        print("Your guess is not right. Try guessing a number higher than.", guess)

    else:
        print("Your guess is not right. Try guessing a number lower than", guess)

    chances+=1

if not chances < 5:
    print("You Lose! The number is:", number)

