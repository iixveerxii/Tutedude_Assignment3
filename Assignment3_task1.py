# Calculating Factorial Using a Function
# Using Recursive function to find factorial

def fact(a):
    """
    this function tests if input value is negative, below or equal to 1 or above 1
    function returns "not defined" for negative inputs,
    1 for equal to or below zero,
    factorial of input if value is above 1 using recursive function
    :param a: input from user
    :return: factorial of input
    """
    if a < 0:
        return "not defined"
    elif a <= 1:
        return 1
    else:
        return a * fact(a - 1)

userinput = int(input("Enter a number: "))
factorial = fact(userinput)

print(f"factorial of {userinput} is: {factorial}")

