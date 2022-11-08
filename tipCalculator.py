# Programmed by Jaicob Remon
# Grade 12 CS Summative part 1

# Creating calculator function
def tipCalculator():
    
    # Asking the user for their level of satisfaction
    levelOfSatisfaction = input("How satisfied were you with the service today ?:")

    # What to do if the customer is not satisfied
    if levelOfSatisfaction == "3":

        print("We are sorry to hear that .")

        # Setting the tax to 10%
        tax = 0.10

        # Asking for the total of the bill
        billCount = input("How much was your bill ?: ")

        # Calculating the final tip
        finalTip = float(billCount) * float(tax)

        # What is the tip which needs to be paid
        print('The tip owed is ---> $' + str(finalTip))

    # What to do if the customer is satisfied
    if levelOfSatisfaction == "2":

        print("That's good.")

        # Setting the tax to 15%
        tax = 0.15

        # asking how much was the bill
        billCount = input("How much was your bill ?: ")

        # Calculating the tip
        finalTip = float(billCount) * float(tax)

        # What is the tip that needs to be paid
        print('The tip owed is ---> $' + str(finalTip))

    # What to do if the customer is extremely satisfied
    if levelOfSatisfaction == "1":

        print("That's great !")

        # Setting the tax to 20%
        tax = 0.20

        # Asking for the total of the bill
        billCount = input("How much was your bill ?: ")

        # Calculating the tip
        finalTip = float(billCount) * float(tax)

        # Printing the tip
        print('The tip owed is ---> $' + str(finalTip))

# Calling the function
tipCalculator()

# Thanking the customer
print("Thank you for dining with us !")
