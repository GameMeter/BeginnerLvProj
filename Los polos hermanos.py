resturant_name = "Los polos hermanos"
MENU = "We have Drinks and Fast food"
Universal_Price = 10
Tax = 5
menu = "We have Chicken Rice\nMutton Rice\nPeppermint deluxe\nTaco crisp Ketchup serving"
Card = 100
import random
WaltLuck = 51
Cash = 500000
# These are general inputs for running the code

# This is the Fring bot, Staff bot and its resturaunt.
def Gustavo_Fring():
    # This is the Introductary def where the user is greeted and presented with option ti either go to family section
    # or get the menu (Walter is greeted specially in the next peices of code
    def Introductary():
        print("Welcome to the greatest Restuarnt in Albaqurque, " + resturant_name)
        global Costumer
        Costumer = input("What is your name? \n")
        print(Costumer)
        if Costumer == "Walter" or "Tony":
            consulting = input("I am sorry, Could i be given a full name?\n")
            if consulting == "Walter Hartwell White":
                print("What are you doing here")
                exit("Get out and never come back to " + resturant_name + " ever again")
            if consulting == "Tony Stark" and 50 > WaltLuck:
                print("I am sorry Tony, But this Country ain't big enough for the both of us...")
                exit("Get out before he comes..")
        def Choice():
            print("May i take your Order? " + Costumer)
            print("We have lots of item in the MENU, would you like to take a look?")
            print("Or sit at the FAMILY table to have one of our servers to take it for you?")
            decision1 = input("The items may change by your reason of stay!\n")
            global decision
            decision = (decision1.upper())
        Choice()
    Introductary()

    # This is the option if the user choose Menu, they are presented  with 2 more option Fast food and drinks
    # After choosing their desired option they are given a bill and the code ends
    if decision == "MENU":
        print("Great " + MENU + " And we have a special offer!, Everything in this Resturaunt is only 10$!! ")
        choice = input("So now, What would you prefer to be informed of?\n ")

        def Fast_Food():
            if choice == "Fast Food":
                print("We have Every single FastFood Item available so Order!")
                Food = input("So what would you like to have?\n")
                FoodAmount = input("How much " + Food + " do you need?\n")
                Foodprice = Universal_Price * int(FoodAmount) * Tax
                print("Here is your " + Food + " You asked for!")
                if Costumer == "Walter":
                    print("Your total is " + str(Foodprice) + "$")
                    if int(Foodprice) < Card:
                        print("Thank you for purchasing here!")
                        for x in "Walter":
                            print(x)
                            exit()
                    else:
                        exit("kys")
                else:
                    print("Your total is " + str(Foodprice) + "$")
                    print("Have a great day!")
                    exit()
        Fast_Food()

        def Drinks():
            if choice == "Drinks":
                print("We have every Drink available so let your mind drift")
                Drink_choice = input("So! What drink would it be?\n")
                Drink_AMOUNT = input("And how many cups?\n")
                Drink_Size = input("Would you want size 1, 2 or 3?\n")
                Total = Universal_Price * int(Drink_AMOUNT) * int(Drink_Size) + Tax
                if Costumer == "Walter":
                    print("Your total is" + str(Total))
                    if Total < Card:
                        print("Thank you for purchasing here!")
                        for x in "Walter":
                            print(x)
                            exit()
                    else:
                        exit("kys")
                else:
                    print("Your total is " + str(Total) + "$, Have a great day!")
                    exit()
            else:
                print("What?")
                Choice()
        Drinks()

    # If the user wants to goto the family section they are greeted by a server where inturn they have multiple option
    # A secret option is provided where no logging will be performed and a menu of this section after with they be
    # offered a bill and a chance to accept a membership (if name is not Walter)
    if decision == "FAMILY":
        print("Alright, I will take you to the family side resturaunt")
        print("Here we are!. Your seat no. is 204, I will have one of your servers to take your order")
        Loyalty1 = input("--Take you seat at 204 or go to the BATHROOM\n")
        Loyalty = (Loyalty1.upper())
        if Loyalty == "BATHROOM" and not Costumer == "GameMeter":
            print("I told you to take your seat.....")
            exit("You have now seen it, now you are d e a d")
        elif Loyalty == "BATHROOM" and Costumer == "GameMeter":
            print("Ahh yes " + Costumer + ", Wellcome to my meth lab. I saw you came to " + resturant_name)
            print("Is there any reason your here?")
            Meth1 = input("Do you have anything to do here?\n")
            Meth = (Meth1.lower())
            if Meth == "yes":
                Option = input("Let me guess, your here to purchase some high. Why else would you known to come here\n")
                if Option == "Code":
                    print(
                        "The Code contains the following\n Input\n Print\n ELIF IF statements\n Value Statement\n str to int statement\n And not statement\n Math statements\n DEF statement\n")
                    exit("Goodbye")
                if Option == "Meth":
                    print("We have meth\nCoke\nFety\nXzre\n And these items have there own price")
                    Drug_Choice = input("What would you like to buy?\n")

                    def Meth_offer():
                        if Drug_Choice == 'meth':
                            price = 20_000
                        elif Drug_Choice == "Coke":
                            price = 35_000
                        elif Drug_Choice == "Fety":
                            price = 40_400
                        elif Drug_Choice == "Xzre":
                            price = 50_000
                        else:
                            print("..., I will take that as a no")
                            exit("Goodbye" + Costumer)
                        Drug_Amount = int(input("How much of " + Drug_Choice + " Do you need? (gram)\n"))
                        Total = Drug_Amount * price
                        print("Thank you GameMeter for purchasing this item your total is " + str(Total) + "$")
                        if Total < Card:
                            exit("bye")
                        else:
                            exit("Im sorry, you do not have enough credit.")

                    Meth_offer()
                if Option == "Game":
                    def Game():
                        print("alright lets play a guessing game, you would have to guess a number from 1-10")
                        print("if you get it right you win if you lose you do it again or leave")
                        retake_formula = input("Do you want to do the game if you lose? y/n: ")
                        def GameStart():
                            x = random.randrange(1, 10)
                            Guess = input("What do you think the number is?")
                            print(x)
                            if x == " ":
                                print("again")
                                GameStart()
                            else:
                                if x == int(Guess):
                                    print("Aight you win")
                                    exit()
                                else:
                                    if retake_formula == "y":
                                        GameStart()
                                    else:
                                        exit()
                        GameStart()
                    Game()
                else:
                    exit("You need rest")
            if Meth == "no":
                exit("Goodbye")
            else:
                exit("What?")
        else:
            def Family():
                print("Hello " + Costumer + " May I take your order? " + menu + "\n")
                choice = input("So what would you like to order?\n")
                amount = input("How many plates?\n")
                if 9 < int(amount):
                    print("Haha funny joke " + Costumer + " How many do you actually want?")
                    exit("Nevermind get yo ass out of here you dum bothr")
                else:
                    print("Your food(" + choice + ") is on its way")
                    print("Here is your Food once your finished, let me know!")
                    input("Are you finished?\n")
                    Total = Universal_Price * Tax * int(amount)
                    if Costumer == "Walter":
                        print("Your total is" + str(Total))
                        if Total < Card:
                            print("Thank you for purchasing here!")
                            for x in "Walter":
                                print(x)
                                exit()
                        else:
                            exit("kys")
                    else:
                        print("Great! your total is " + str(Total))
                        if Total > Card:
                            exit("Im sorry, you do not have any credit. now i have to take your soul")
                        else:
                            print("Thank you for purchasing here!")

                            def SupermarketPrompt():
                                print(
                                    "Before you leave we have opened a Supermarket and i am distributing the membership")
                                Membership1 = input("Do you want a membership? Y/N\n")
                                global Membership
                                Membership = (Membership1.lower())

                                if Membership == "y" or "yes":
                                    print("Great! Its just around the corner from here")
                                    print("Have a great day!")
                                else:
                                    print("Ok., Have a great day!")

                            SupermarketPrompt()
            Family()
    else:
        print("What?")
        Choice()
Gustavo_Fring()

# If the users name is not Walter and they accept the membership they get access to the supermarket where they are
# greeted and they could buy things after which they may or may not go home
def Supermarket():
    if Membership == "y" or "yes":
        print("""Welcome to Zaza, where anything you need is present but have to wait till it 
                    gets here, I am Jezz how can i help you?""")
        Loyalty12 = input("""Before we head further do you happen to have a membership because you
                    need it to shop here, if you are here for anything else other then shopping please get out\n""")
        Loyalty13 = (Loyalty12.lower())
        if Loyalty13 == "y" or "yes":
            print("""Great!, Look around for the items you need and come back so i can charge 
                        10x its actual value""")
            Increment = 10
            List = ["Milk", "Eggs", "Chips", "Chicken"]
            M = E = C = CH = 10
            ShelvesStart = input("Alright 4 shelves i gotta get 4 items and leave im so tired")
            What_I_got = "0, 2, 5, 8"

            print("""_______V. Vegetables______________________G. Garlic________________P. Peppermint_______________
                        ___________________O. Onions________________E. Eggs_________________R. Ravolette(Special)___________________""")

            Greogry1 = input("What should i take?")
            if Greogry1 == "M":
                x = What_I_got.replace(str(0), str(1))
            if Greogry1 == "E":
                x = What_I_got.replace(str(5), str(1))
            if Greogry1 == "C":
                x = What_I_got.replace(str(8), str(1))
            if Greogry1 == "CH":
                x = What_I_got.replace(str(2), str(1))
            else:
                x = What_I_got.replace(str(0), str(9))

            print("""___________________M. Milk___________________MN.Mango Juice_______________E.Electronic Prime__________
                        ______________G. Ginger_______________CO. Corniflour_________________T. Tea_________________________________""")
            Greogry2 = input("3 more itemssssss")

            if Greogry2 == "M":
                y = x.replace(str(0), str(1))
            if Greogry2 == "E":
                y = x.replace(str(5), str(1))
            if Greogry2 == "C":
                y = x.replace(str(8), str(1))
            if Greogry2 == "CH":
                y = x.replace(str(2), str(1))
            else:
                y = x.replace(str(2), str(9))
                print("Les goo new things!")

            print("""__________________________CH.Chicken________________CR.Cake Ravoletter_______________CB. Chicken Breast_
                        __________________CL.Clock(Lelte)______________MR. Microsoft Rally10_______________________CC. COCK CHICKEN""")
            Greogry3 = input("2 more and i gotta leave")

            if Greogry3 == "M":
                z = y.replace(str(0), str(1))
            if Greogry3 == "E":
                z = y.replace(str(5), str(1))
            if Greogry3 == "C":
                z = y.replace(str(8), str(1))
            if Greogry3 == "CH":
                z = y.replace(str(2), str(1))
            else:
                z = y.replace(str(5), str(9))
                print("Ok ok nice")

            print("""________________C. Chips_________________N. Basketball(Neymar signed)______________TU. Telephone unit____
                        ______________R. Razers____________S. Siezers___________B. Blade__________________P. PokeBall__________""")
            Greogry4 = input("Last item!")

            if Greogry4 == "M":
                a = z.replace(str(0), str(1))
            if Greogry4 == "E":
                a = z.replace(str(5), str(1))
            if Greogry4 == "C":
                a = z.replace(str(8), str(1))
            if Greogry4 == "CH":
                a = z.replace(str(2), str(1))
            else:
                a = z.replace(str(8), str(9))
                print("Lets get these items in")

            if a == "1, 1, 1, 1":
                a = True
                Vaklu = 40
            else:
                a = False
                Vaklu = 50

            print("Cashier stall....")
            Total = Tax * 10 * Vaklu
            print("Cashier: Your Total is " + str(Total) + "$, Will you be paying with cash or card?")
            CashCard1 = input("Cash or Card?\n ")
            CashCard = (CashCard1.lower())
            if CashCard == "card":
                print("Cashier: Alright, Card it is please insert it in the card holder")
                if Total < Card:
                    print("Cashier: All done, Thank you for shopping here!")
                    if a is True:
                        print("Hmmm, I got everything i need time to head home.")
                    else:
                        print("Shit....., i missed smth dam now i can't go back.")
                else:
                    exit("KYS")
            if CashCard == "cash":
                print("Cashier: Ok you own me " + str(Total) + "$")
                if Total < Cash:
                    print("Thank you for shopping here!")
                    if a is True:
                        print("Hmmm, I got everything i need time to head home.")
                    else:
                        print("Shit....., i missed smth dam now i can't go back.")
                else:
                    exit("Get yo broke ass out of here")
            else:
                exit("Bruh")
        else:
            exit("What are you waiting for? Get out.")
    else:
        exit("Who let you in here then?")
Supermarket()

# This project has been finished at March 4, Saturday 2023 1:56pm