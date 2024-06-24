import random

top_range_number = input('type a Number : ')

if top_range_number.isdigit():
    top_range_number = int(top_range_number)

    if top_range_number <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, top_range_number)

guess_time = 0
while True:
    guess_time += 1
    user_guess = input(" make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type e number next time. ")
        continue

    print("The random Number is : " + str(random_number))

    if user_guess == random_number:
        print("Ohh my God! Guess number and random is match!!!! ")
        break
    elif user_guess > random_number:
        print("Please remember your input random range is : " + str(top_range_number))
    else:
        print("Ops!! not match. Try next time.")

print("You got matches your guess number with random number after trying " + str(guess_time) + " times. ")
