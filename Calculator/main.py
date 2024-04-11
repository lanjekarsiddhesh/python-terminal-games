from art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    # if num2==0:
    #   return "ERROR!!! Any of the number can't divided by 'Zero'"
    # else:
    return n1 / n2

action = {'+': add, '-': sub, '*': mul, '/': div}

def calculator():
    print(logo)
    num1 = float(input("Enter first number:- "))

    for sign in action:
        print(sign)

    while True:
        operand = input("which operation you perform:- ")
        

        if operand in action.keys():
            operation = action[operand]
        else:
            print("Choose correct operation ex. +, - ,*, /")
            operand = input("which operation you perform:- ")


        num2 = float(input("Enter your next number:- "))

        result = operation(num1, num2)

        print(f"{num1} {operand} {num2} = {result}")

        next = input("Do you perform another operation with previous result type 'yes/no' \n or If you exit calculator type 'exit or Q' :- ")
        
        if "yes" in next or "y" in next:
            num1 = result

        elif "no" in next or "n" in next:
            calculator()

        elif "exit" in next or "q" in next:
            break
        else:
            print("Please enter valid operation")

calculator()