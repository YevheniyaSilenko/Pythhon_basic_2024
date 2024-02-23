try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num1 == num2:
        print("Numbers same")
    else:
        print("Numbers not same. Number {} less than number {}".format(min(num1, num2), max(num1, num2)))

except ValueError:
    print("Incorrect data. Please enter number.")
