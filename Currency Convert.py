print("Hello!, Welcome to my currency converter")
Currency = ["US", "GBP", "Kuwait Dinar", "Rubels", "Yen"]
for i, choice in enumerate(Currency, start=1):
    print(f"{i}. {choice}")

Choice = int(input("What currency would you want to convert?"))
Choice1 = Currency[Choice - 1]
Convert = int(input("What currency do you want it to be converted"))
Convert1 = Currency[Convert - 1]

Value = int(input(f"How much of {Choice1} do you want to convert to {Convert1}?: "))
if Choice == int(1) and Convert == int(1):
    x = Value
elif Choice == int(1) and Convert == int(2):
    x = (Value - (0.16 * Value))
elif Choice == int(1) and Convert == int(3):
    x = (Value - (0.69 * Value))
elif Choice == int(1) and Convert == int(4):
    x = (Value + (74.76 * Value))
elif Choice == int(1) and Convert == int(5):
    x = (Value + (135 * Value))
elif Choice == int(2) and Convert == int(1):
    x = (Value + (0.19 * Value))
elif Choice == int(2) and Convert == int(2):
    x = Value
elif Choice == int(2) and Convert == int(3):
    x = (Value - (0.63 * Value))
elif Choice == int(2) and Convert == int(4):
    x = (Value + (89.34 * Value))
elif Choice == int(2) and Convert == int(5):
    x = (Value + (161.90 * Value))
elif Choice == int(3) and Convert == int(1):
    x = (Value + (2.25 * Value))
elif Choice == int(3) and Convert == int(2):
    x = (Value + (1.73 * Value))
elif Choice == int(3) and Convert == int(3):
    x = Value
elif Choice == int(3) and Convert == int(4):
    x = (Value + (245.53 * Value))
elif Choice == int(3) and Convert == int(5):
    x = (Value + (443.63 * Value))
elif Choice == int(4) and Convert == int(1):
    x = (Value - (0.987 * Value))
elif Choice == int(4) and Convert == int(2):
    x = (Value - (0.989 * Value))
elif Choice == int(4) and Convert == int(3):
    x = (Value - (0.9959 * Value))
elif Choice == int(4) and Convert == int(4):
    x = Value
elif Choice == int(4) and Convert == int(5):
    x = (Value + (0.80 * Value))
elif Choice == int(5) and Convert == int(1):
    x = (Value - (0.9927 * Value))
elif Choice == int(5) and Convert == int(2):
    x = (Value - (0.9939 * Value))
elif Choice == int(5) and Convert == int(3):
    x = (Value - (0.9978 * Value))
elif Choice == int(5) and Convert == int(4):
    x = (Value - (0.55 * Value))
elif Choice == int(5) and Convert == int(5):
    x = Value
else:
    x = 0

print(f" your {Choice1} is worth {str(x)} {Convert1}")
# Program made and completed at March 10th 2023