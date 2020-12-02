# Calculating miles per gallon

print ("This program calculates miles per gallon")

# Ask input from the user

miles_driven = float(input("Enter miles driven: "))

# Get gallons used from the user

gallons_used = float(input("Enter gallons used: "))

# Calculate  and print the answer

mpg = miles_driven / gallons_used

print ("Miles per gallon: %.2f" %(mpg))
