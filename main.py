# User inputs height in centimeters, and it converted to float data type
Height = float(input("Enter your height in centimeters: _"))
# User inputs weight in kilograms, and it converted to float data type
Weight = float(input("Enter your Weight in Kg: _"))
# Converting height from centimeters to meters
Height = Height / 100
# Calculating BMI, The formula is weight(kg) divided by height(meter) squared
BMI = Weight / (Height * Height)
# Displays the BMI result
print("your Body Mass Index is: ", BMI)

'''
conditional statements from the BMI result to determine if the user is severely underweight, underweight, Healthy,
overweight, severely overweight or the data inputted by the user is incorrect.

By BMI standard health values, 
below 18.5 – you're in the underweight range. 
between 18.5 and 24.9 – you're in the healthy weight range. 
between 25 and 29.9 – you're in the overweight range. 
between 30 and 39.9 – you're in the obese range.
'''

# The first if statement checks that BMI is greater than zero before processing to the indented statements
if BMI > 0:
    # The second if statement checks BMI if it's less than or equal to 16
    if BMI <= 16:
        # Displays you are severely underweight
        print("you are severely underweight")
    # This elif statement checks BMI if it's less than 18.5
    elif BMI < 18.5:
        # Displays you are underweight
        print("you are underweight")
    # This elif statement checks BMI if it's less than or equal to 24.9
    elif BMI <= 24.9:
        # Displays you are Healthy
        print("you are Healthy")
    # This elif statement checks BMI if it's less than or equal to 29.9
    elif BMI <= 29.9:
        # Displays you are overweight
        print("you are overweight")
    # This elif statement checks BMI if it's less than or equal to 39.9
    elif BMI <= 39.9:
        # Displays you are obese
        print("you are obese")
    # This else statement runs when BMI is greater than 39.9
    else:
        # Displays you are severely overweight
        print("you are severely overweight")
# This else statement runs when BMI is less than or equal to zero
else:
    # Displays enter valid details
    print("enter valid details")
