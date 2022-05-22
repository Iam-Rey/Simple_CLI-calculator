# Simple CLI Calculator
print("Welcome to Simple CLI Calculator")

is_running = True

while is_running:
    # Processing calculator
    print("Starting Calculator Process")
    user_operation = input("what operation would you like to perform?\nPick any of :   ['+','-','*','/'] : ")

    try: # Try to get user numbers if they are valid integers/floats, continue
        
        no1 = float(input("First number: "))
        no2 = float(input("Second nuimber: "))

    except: # we get an error running it
        print("Failed, invalid numbers...")
        continue


    if user_operation == '+':
        # perform addition
        print(no1 + no2)

    elif user_operation == '-':
        # perform subtraction
        print(no1 - no2)    

    elif user_operation == '*':
       # perform multiplication
       print(no1 * no2) 

    elif user_operation == '/':
       # perform division
       print(no1 / no2)

    else:
        print("Invalid operation entered, try again...")    

    Choice = input("Would you like to perform another operation? [y,n]")
    if Choice == "y":
        pass

    if Choice == "n":
        is_running = False
        # This is the same thing as a break

     # Ctrl + C to exit any python program...