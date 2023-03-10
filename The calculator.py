import string
from sympy import *


def TheCalculator():
    print("Hello! user, i am a calculator and i can do math")

    def Route():
        global Route1
        Route1 = input("What type of calculator do you want me to be? Simple or Complex(Defective) or Comp: ")
        Route1 = (Route1.lower())

    Route()

    def Simple():
        if Route1 == "simple":
            print("Great! now i need the problem related to simple math")

            def parameters():
                Parameters1 = input("Do you want any parameters in your code?")
                Parameters = (Parameters1.lower())

                if Parameters == "y" or "yes":
                    def CompPara():
                        global RoundedoffTop, RoundedoffBot, Integer, Float, SQROOT
                        Roundedoff = input("Do you want your answer to be rounded to the (T)op or (B)ottom?: ")
                        if Roundedoff == "T":
                            RoundedoffTop, RoundedoffBot = True, False
                        if Roundedoff == "B":
                            RoundedoffTop, RoundedoffBot = False, True
                        else:
                            RoundedoffTop, RoundedoffBot = False, False
                        NoType = ["Integer", "Float"]
                        for i, Type in enumerate(NoType, start=1):
                            print(f"{i}. {Type}")
                        NoType1 = int(input("Do you want you answer to be in which of these types"))
                        SelecterType = NoType[NoType1 - 1]
                        if SelecterType == int(1):
                            Integer, Float = True, False
                        if SelecterType == int(2):
                            Float, Integer = True, False
                        else:
                            Integer, Float = False, False
                        SQROOT = input("Do you also want your answer to be also paired with a Square Root?")
                        if SQROOT == "y" or "yes":
                            SQROOT = True
                        else:
                            SQROOT = False

                        input("Do you want coffe?")

                    parameters()

                else:
                    RoundedoffTop, RoundedoffBot, Integer, Float, SQROOT = False, False, False, False, False

            def SimpleMath():
                while True:
                    global expression
                    expression = input(
                        "Enter a mathematical expression or type 'quit' to exit\nOr type 'retry' to put a"
                        "different equation: ")
                    if expression == 'quit':
                        exit()
                    if expression == "retry":
                        SimpleMath()
                    else:
                        if RoundedoffTop:
                            if Integer:
                                if SQROOT:
                                    print(round(int(expression)))
                                    print(sqrt(expression))
                                else:
                                    print(round((int(expression))))
                            if Float:
                                if SQROOT:
                                    print(round(float(expression)))
                                    print(sqrt(expression))
                                else:
                                    print(round(float(expression)))
                            else:
                                print(round(int(expression)))
                        else:
                            print(expression)
                            exit()

            SimpleMath()

    Simple()

    def Comp():
        if Route1 == "comp":
            print("Ok user, comp math function is like complex but uses a library which is more stable")

            def CompMath():
                print("Now user, its time for the math, you have three variables x, y, z")
                x, y, z = symbols("x y z")
                str_expr = input("Give me a mathematical expression: ")
                expr = sympify(str_expr)
                print(expr)
            CompMath()
    Comp()

    def Complex():
        if Route1 == "complex":
            print("Ok user, Complex math it is [Note: I may break down if the problem is too hard because im unstable]")
            Parameters = input("Do you want to set some customs within your solution?")
            Parameters = (Parameters.lower())

            if Parameters in ["yes", "y", "accept"]:
                def ComplexParameters():
                    pass

                ComplexParameters()

                def ComplexMath():
                    pass

                ComplexMath()

                def RetryAgain():

                    Retry = input("Do you want to put another equation or go back(1) to the main page(2)")

                    if Retry == "1":
                        Complex()
                    if Retry == "2":
                        TheCalculator()
                    else:
                        print("I didnt quite get you")
                        RetryAgain()

                RetryAgain()

            if Parameters == "no" or "denied":
                def ComplexMath():
                    global Final1, Final2, Final3
                    print("The only Variable you are allowed to use is X or Y or Z, if you used anything other"
                          "then this, the code may break and your variable must be at the last ")
                    expression1 = input("First math expression(x):  ")
                    expression2 = input("Second math expression(y): ")
                    expression3 = input("Third math expression(z): ")
                    if string.ascii_letters in expression1:
                        if "x" in expression1:
                            eval1 = (expression1.replace('x', str(0)))

                            Result1 = eval(eval1)
                            Final1 = Result1 + 'x'
                        else:
                            print("We found a mistake in the first expression")
                            ComplexMath()
                    else:
                        Final1 = eval(expression1)

                    if string.ascii_letters in expression2:
                        if "y" in expression2:
                            eval2 = (expression2.replace('y', '0'))
                            Result2 = eval(eval2)
                            Final2 = Result2 + 'y'
                        else:
                            print('We found a problem in the second expression')
                            ComplexMath()
                    else:
                        Final2 = eval(expression2)
                    if string.ascii_letters in expression3:
                        if "z" in expression3:
                            eval3 = (expression3.lower())
                            Result3 = eval(eval3)
                            Final3 = Result3 + 'z'
                        else:
                            print("we have found a problem in the third expression")
                            ComplexMath()
                    else:
                        Final3 = eval(expression3)

                    print(f"The Answer to the question you gave me is: {Final1} + {Final2} + {Final3}")

                ComplexMath()

                def RetryAgain():

                    Retry = input("Do you want to put another equation or go back(1) to the main page(2)")
                    if Retry == "1":
                        Complex()
                    if Retry == "2":
                        TheCalculator()
                    else:
                        print("I didnt quite get you")
                        RetryAgain()

                RetryAgain()
            else:
                print("What?")
                Complex()

    Complex()


TheCalculator()
