House = 1000000
Credit_Good = True
buyer = input("Hello, what is your name?")

if Credit_Good is True:
    Downpayment = House * 0.1
elif Credit_Good is False:
    Downpayment = House * 0.2
else:
    print("Im not selling this house to you!")
    exit()


print(f"For this house worth {str(House)}$ you need to put down {str(int(Downpayment))}$ as downpayment")
end()
