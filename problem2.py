#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

x = float(input("Enter a number: "))
N = int(x)

if N == x:
    print("your number is an integer")
else:
    print("your number is not an integer")