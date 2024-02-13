number1 = int(input("Enter number: "))
number2 = int(input("Enter number: "))
number3 = int(input("Enter number: "))

choice = input("Choose operation ('min', 'max', 'average') : ")
# min
if choice == 'min':
    result = number1
    if number2 < result:
        result = number2
    if number3 < result:
        result = number3
# max
elif choice == 'max':
    result = number1
    if number2 > result:
        result = number2
    if number3 > result:
        result = number3
# average
elif choice == 'average':
    result = (number1 + number2 + number3) / 3
else:
    result = "Wrong choice"

# Вивести результат
print("Результат:", result)