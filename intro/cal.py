from email import message


def print_header():

    print("-" * 25)
    print("PyCalc 3000")
    print("-" * 25)

    print("[1] - Sum")
    print("[2] - Subtract")
    print("[3] - Multiplication")
    print("[4] - Division")
    print("[5] - Message")

    print("Press 'q' For Exit ")


option = ""

while(option != "q"):
    print_header()

    option = input("Select an option: ")

    if option == "q":
        break 

    if option != "5":
        num1 = float(input("Insert Your First Number: "))
        num2 = float(input("Insert Your Second Number: "))

    if option == "1":

        res = num1 + num2
        print ("Answer: " + str(res))


    if option == "2":

      
        res = num1 - num2  
        print ("Answer: " + str(res))


    if option == "3":

        res = num1 * num2
        print ("Answer: " + str(res))

    if option == "4":

        if num2 == 0:
            print("Error: you can kill us all, please stop this")
        
        else:
            res = num1 * num2
            print("The result is: " +str(res))

    if option == "5":
        message = input("Please Enter a Message:")
        times  = int (input("How Many Times?"))
        time = times - 1

        for n in range (times):
            print(message)
        
        i = 0
        while (i <= times ):
            print(message)
            i += 1

         
print("Hasta La Vista, Baby!")