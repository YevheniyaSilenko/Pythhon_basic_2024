# 1
number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
number3 = int(input("Enter number3: "))
result1 = number1 + number2 + number3
result2 = number1 * number2 * number3
print(result1)
print(result2)

# 2

length1 = int(input("Enter length1: "))
length2 = int(input("Enter length2: "))
area = ((length1 * length2) / 2)
print(area)

# 3

number = int(input("Enter 4-digit number: "))
n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 100 // 10
n4 = number % 10

result = n1 * n2 * n3 * n4
print(f"n1: {n1} n2: {n2} n3: {n3} n4: {n4}")
print(f"Result: {result}")
