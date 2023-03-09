print('You: I wanna make coffee!\n Hmm, what coffee should i make?')
SafeAmount = 100
coffee_machines = ["Coffee101", "The Italian Cafe", "Russian Wake", "US-294Coffee", "EU-293Coffee"]
for i, machine in enumerate(coffee_machines, start=1):
    print(f"{i}. {machine}")
selection = int(input("You: What coffee machine should I use? "))
selected_machine = coffee_machines[selection - 1]

if selection == int(1):
    Coffee101 = True
    TheItalianCafe = False
    RussianWake = False
    USCoffee = False
    EUCoffee = False
    Poisening = 10
elif selection == int(2):
    TheItalianCafe = True
    RussianWake = False
    USCoffee = False
    EUCoffee = False
    Coffee101 = False
    Poisening = 5
elif selection == int(3):
    RussianWake = True
    TheItalianCafe = False
    USCoffee = False
    EUCoffee = False
    Coffee101= False
    Poisening = 20
elif selection == int(4):
    USCoffee = True
    RussianWake = False
    Coffee101 = False
    EUCoffee = False
    TheItalianCafe = False
    Poisening = 15
elif selection == int(5):
    EUCoffee = True
    RussianWake = False
    USCoffee = False
    Coffee101 = False
    TheItalianCafe = False
    Poisening = 3
else:
    print("You: I think i need more sleep")
    exit()

print(f"You: Hmm i think i will use {selected_machine}, its been a while since i used it")
print("You: Now where did i put my coffee at?")
CoffeeLoc101 = ["Pantry", "Wardrobe", "Bathroom", "Office", "Kitcher"]
for i, loc in enumerate(CoffeeLoc101, start=1):
    print(f"{i}. {loc}")
CoffeeLocation = int(input("Where is the coffee?: "))
CoffeeLocAns = CoffeeLoc101[CoffeeLocation - 1]

if CoffeeLocation != int(1):
    print("You: Gosh, that brain surgery last week really did smth bad to my brain, i gotta go to the doctor")
    exit()
else:
    print("*when you entered the pantry you saw a poster which was 15years ago and there was a writing in it which said\n'2nd birthday'*")
    print("You: So many options to pick from i kinda wanna try all of em but i can't so i will go with.....")

    if Coffee101 == True:
        CoffeeOption = ["CoffeeDeluxe", "Coffee101", "Caffeniece", "CoffeeGYRO"]
    elif USCoffee or EUCoffee == True:
        CoffeeOption = ["NestleCoffee", "Maxwell House", "AlpsCoffee", "GreekCoffee"]
    elif TheItalianCafe == True:
        CoffeeOption = ["Caffè Toraldo", "Caffè Vergnano", "Caffè Pellini", "Caffè Borbone"]
    elif RussianWake == True:
        CoffeeOption = ["Jardin", "Jockey", "Moscow Coffee House", "Chernaya Karta"]
    
    for i, CoffeeOpt in enumerate(CoffeeOption, start=1):
        print(f"{i}. {CoffeeOpt}")
    coffeeopt = int(input())
    coffeeopt1 = CoffeeOption[coffeeopt - 1]

    print(f"You: ...{coffeeopt1} heard good thing about em. Alright now its time to actually make it, \nnow how much coffee should i put?")
    CoffeeAmmount = int(input("mg: "))
    if CoffeeAmmount > SafeAmount:
        Death30 = True
        Dead = CoffeeAmmount - SafeAmount
    else:
        Death30 = False
    
    print(f"Hmm {CoffeeAmmount}mg should be enough now lets put turn on the machine")
    Cabletype1 = ["Schuko", "NEMA 5-15", "Socket101"]
    for i, Socket in enumerate(Cabletype1, start=1):
        print(f"{i}.{Socket}")
    Cabletype = int(input("What socket should you plug your Coffee  Machine?: "))
    if Coffee101 == True and not Cabletype == int(3):
        SystemFail = True
    elif RussianWake or TheItalianCafe or EUCoffee == True and not Cabletype == int(1):
        SystemFail = True
    elif USCoffee == True and not Cabletype == int(2):
        SystemFail = True
    else:
        SystemFail = False
    
    if SystemFail == True:
        print("You: Damn this aint fitting..... ah finally it fit")
    else:
        print("You: Lets turn it on!")
    
    print("You: now its time to clock the shutter and turn it on")
    Crank = int(input("How much degree should you clock the shutter?(Number only): "))
    if Crank != int(90):
        Poisening += 10
    else:
        Poisening += 0
    
    print("You: Ok time to turn this on")
    AREYOUSURE1 = input("Turn on the Coffee Machine?: y/n")
    AREYOUSURE = (AREYOUSURE1.lower())

    if AREYOUSURE == "yes" or "y" and SystemFail == True:
        print("The machine was plugged to the wrong socket and it exploded in your face and you died")
        exit()
    elif AREYOUSURE == "yes" or "y" and SystemFail == False:
        print("After the coffee is made you drank the coffee")
        if Poisening > 29:
            print("You died from poisening")
            exit()
        else:
            if Death30 == True:
                print("After 13years")
                input("Doctor: You are about to die")
                input("You: Why?")
                input(f"Doctor: You have added {Dead}mg more in your coffee ")
                input("You: Great..")
                exit('You died')
            else:
                print('you lived a happy life')
                quit()
    elif AREYOUSURE == "no" or "n":
        exit()
    else:
        print("Hmm nvm, i don't need coffee")
        exit()

# Code development started and ended at 9th March 2023