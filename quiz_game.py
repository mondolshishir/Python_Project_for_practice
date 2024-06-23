import re

print("Welcome to my Computer Quiz Game!!!!!!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
my_info = input("Please enter your name: ")

print("Okay! Let's play :")
score = 0

answer = input("What dose CPU stand for ? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What dose RAM stand for ? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What dose GPU stand for ? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

print(my_info + " , you got " + str(score) + " for your correction answers")
print("Your score percentage is "+ str(score / 3 * 100) + "%")
