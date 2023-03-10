print("[WELCOME TO THE CAR GAME]")
print(" Type Start, to start the car\n Type Stop to stop the car\n Type Quit to stop playing\n Type Help for help")
import random

Charrit = ""

Start = 0
Stop = 1

def Engine():
    global Stop,Start
    TheInput = input()
    if TheInput == "Start" and Start == int(0):
        print("The car has started..")
        Start += 1
        Stop -= 0
        Engine()
    elif TheInput == "Start" and Start == int(1):
        print("The car is already started!")
        Start = 1
        Stop = 0
        Engine()
    elif TheInput == "Stop" and Stop == int(0):
        print("The car has stopped...")
        Start -= 0
        Stop += 1
        Engine()
    elif TheInput == "Stop" and Stop == int(1):
        print("You can not stop a stopped car")
        Start = 0
        Stop = 1
        Engine()
    elif TheInput == "Help":
        print(
            " Type Start, to start the car\n Type Stop to stop the car\n Type Quit to stop playing\n Type Help for help")
        Engine()
    elif TheInput == "Quit":
        x = random.randrange(10)
        if x == int(5):
            print('You tried to exit the car but ended up getting hit by another car and died')
        else:
            print("Come back soon")
            exit()
    else:
        print("I do not understand you")

        Engine()


Engine()

# Car game but with while loops



while True:
    Start = 0
    Stop = 1

    TheInput = input()
    if TheInput == "Start" and Start == int(0):
        print("The car has started..")
        Start += 1
        Stop -= 0

    elif TheInput == "Start" and Start == int(1):
        print("The car is already started!")
        Start = 1
        Stop = 0

    elif TheInput == "Stop" and Stop == int(0):
        print("The car has stopped...")
        Start -= 0
        Stop += 1

    elif TheInput == "Stop" and Stop == int(1):
        print("You can not stop a stopped car")
        Start = 0
        Stop = 1

    elif TheInput == "Help":
        print(
            " Type Start, to start the car\n Type Stop to stop the car\n Type Quit to stop playing\n Type Help for help")
    elif TheInput == "Quit":
        x = random.randrange(10)
        if x == int(5):
            print('You tried to exit the car but ended up getting hit by another car and died')
            break
        else:
            print("Come back soon")
            break
    else:
        print("I do not understand you")
