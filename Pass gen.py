import os
import random
import string


def Passwordgen():
    print("Welcome to the password generator")

    print("here i im going to create a password for you and i just need a few details")

    newdir = input("where do you want this file to be stored in (Give a dir name)")
    if not os.path.exists(f"{newdir}"):
        os.makedirs(f"{newdir}")
    print("Great it seems we have discovered your desired dir now!")
    Name = input("what should be the name of your file?")
    file = open(f"{newdir}/{Name}.txt", "w")
    print("What is the name of the thing you are trying to make a password for?")
    PassName = input()

    def lengthy():
        global length
        length = input("how many characters do you want in your password?")

        if "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" not in length:
            print("I need only numbers sir")
        else:
            pass

    lengthy()
    print("Alright we got the name and length we are generating the password")
    writeadditional = input("Do you want to write something extra in this file?")
    writeadditional = (writeadditional.lower())

    def Finishingtouches():

        if writeadditional == "y" or "yes":
            write = input()
            file.write(f"{write}\n")
            print("Ok we got the password ready!")
            letters = string.ascii_lowercase + string.digits
            result_str = ''.join(random.choice(letters) for i in range(int(length)))
            print(f"Password is: {result_str} to the user {PassName} do not lose it:)")
            file.write(f"User: {PassName}----------------Password: {result_str}")
            file.close()
            exit()
        if writeadditional == "no" or "n":
            print("Ok we got the password ready!")
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(int(length)))
            print(f"Password is: {result_str} to the user {PassName} do not lose it:)")
            file.write(f"User: {PassName}----------------Password: {result_str}")
            file.close()
            exit()
        else:
            print("what?")
            Finishingtouches()

    Finishingtouches()


Passwordgen()






