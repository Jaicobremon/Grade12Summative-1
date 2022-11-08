# Programmed by Jaicob Remon
# Grade 12 CS summative part 2

# Defining the function
def fineCalculator():

    # Asking for speed limit
    speedLimit = input("What was the speed limit on the road ?: ")

    # Asking for the drivers speed
    recordedSpeed = input("What speed were you driving at ?: ")

    # Calculating wheter the driver was speeding or not
    difference = int(recordedSpeed) - int(speedLimit)

    # If the driver was not speeding
    if difference <= 0:
        print("Congratulations you were within the speed limit")
    
    # If the driver was speeding between 1 and 20
    if difference >= 1 and difference <= 20:
        print("You were slightly over the speed limit")
        print("Your fine is $100")

    # If the driver was speeding between 21 and 30
    if difference >= 21 and difference <= 30:
        print("You were over the speed limit")
        print("Your fine is $270")

    # If the driver was speeding above 31
    if difference >= 31:
        print("You were way above the speed limit")
        print("Your fine is $500")

# Calling the function
fineCalculator()
