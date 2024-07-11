import time
import os
import random

os.system('cls')
print("HQ9- - The Ultimate Dumbest Programming Language Ever Based Off HQ9+")
print("Also use \"help\" for very useful information")
time.sleep(4)
os.system('cls')

variables = []
values = []

dumbjokes = [
    "Every 60 seconds in Africa, a minute passes. Together, we can stop this!",
    "What do you call a really stupid fish? A dumb bass",
    "A guy was in high school for 10 years. He must have been really stupid, but not as stupid as the guy who was there 20 years. The longer you go to high school, the dumber you are. Thats why I never went.",
    "Arguing with strangers online is like wrestling sharks. Even if you win, it was a really stupid thing to do.",
    "Why can’t politicians do algebra? They can’t solve the inequalities."
]

acc = 0
loop = 1
while loop == 1:
    user = input()
    try:
        if user == "h":
            # the h stands for "hello"
            print("Hello World!")
        elif user == "q":
            # the q stands for "Q". isn't that obvious
            print("Q")
        elif user == "9":
            # the 9 stands for "99"
            bottle = 99
            while (bottle > 0):
                print(f"{bottle} bottles of beer on the wall,")
                print(f"{bottle} bottles of beer.")
                bottle -= 1
                print(f"Take one down and pass it around {bottle} bottles of beer on the wall.")
                if bottle == 1:
                    break
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.")
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print("Go to the store and buy some more, 99 bottles of beer on the wall.")
        elif user == "+":
            # the + stands for "+". isn't that obvious
            acc += 1
            print(acc)
        elif user == "p":
            # the p stands for "porcupine"
            print("Porcupine on your head")
        elif user == "d":
            # the d stands for "dragon"
            print("dragon appears out of thin air")
        elif user == "c":
            # the c stands for "cat"
            os.system('cls')
            print(" /\\_/\\")
            print("( o.o )")
            print(" > ^ <")
        elif user == "b":
            # the b stands for "binary"
            print("1000111 1100101 1110100 100000 1000010 1101001 1101110 1100001 1110010 1111001 100000 1000010 1100001 1101110 1100001 1101110 1100001 100111 1100100 100001")
        elif user == "s":
            # the s stands for "system"
            raise Exception("Lil bro thought that they could exploit the system? Nuh uh!")
        elif user == "r":
            # the r stands for "random"
            print(random.choice(dumbjokes))
        elif user[0] == "v" and "=" in user:
            # the v stands for "variable" and it's the 1 serious command
            user = user[1:]
            user = user.replace(' ', '')
            variables.append(user.split("=")[0])
            values.append(user.split("=")[1])
            print(f"Now {user.split("=")[0]} is equal {user.split("=")[1]}!")
        elif user[0] == "o":
            # the o stands for "output" and it's the 2 serious command
            user = user[1:]
            user = user.replace(' ', '')
            if user in variables:
                print(values[variables.index(user)])
            else:
                print("lil bro first assign the variable dumbass")
        elif user[0] == "y":
            # the y stands for "your"
            user = [user[2:]]
            dumbjokes.append(user)
        elif user == "help":
            print("h helps you to write your first program!",
                  "q prints out itself!",
                  "9 sings a pretty good song!",
                  "+ accelerates!",
                  "p tells you what is on your head!",
                  "d summons a dragon!",
                  "c prints out the cutest ASCII art ever!",
                  "b prints out something you would like to decipher!",
                  "s releases HQ9+++ into the internet!",
                  "r tells you the funniest joke ever!",
                  "v [variable] = [value] makes you a god!",
                  "o [variables] makes you a god publicly!",
                  "y [value] makes you the funniest person ever!",
                  "help helps you!")
        else:
            print("Who do you think you are, little bro? Get out while you still can, your IP is 111.222.333.444!")
    except Exception as e:
        print(f"lil bro is so dumb they just casually caused an error in the interpreter dude btw the error is some {e} thingy idk what it is")
