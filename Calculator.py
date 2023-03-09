num = 0 

def whileloop():
    while True:
        global num
        num += 1
        Buzz = False
        Bash = False
        numcheck1 = num % 3
        numcheck2 = num % 5

        if numcheck1 == 0:
            Buzz = True
        if numcheck2 == 0:
            Bash = True
        if Buzz and Bash:
            print(f"Jackpot {num}")
        elif Buzz:
            print(f"Buzz {num}")
        elif Bash:
            print(f"Bash {num}")
        else:
            print(num)

whileloop()
#its a loop
