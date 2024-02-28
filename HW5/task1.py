import random

numbers = []
ARR_SIZE = 10
for _ in range(ARR_SIZE):
    numbers.append(random.randint(-10, 10))
print(numbers)

negative_numbers_sum = 0
even_numbers_sum = 0
odd_numbers_sum = 0
result_sum = 0
for number in numbers:
    if number < 0:  # Сума негативних чисел;
        negative_numbers_sum += number
    if number % 2 == 0:  # Сума парних чисел;
        even_numbers_sum += number
    if number % 2 != 0:  # Сума непарних чисел;
        odd_numbers_sum += number
    if number % 3 == 0:  # Добуток елементів з кратними індексами 3;
        result_sum += number

print(negative_numbers_sum)
print(even_numbers_sum)
print(odd_numbers_sum)
print(result_sum)

min_value_index = numbers.index(min(numbers))
max_value_index = numbers.index(max(numbers))

if min_value_index > max_value_index:
    min_value_index, max_value_index = max_value_index, min_value_index

result = 0
for i in range(min_value_index + 1, max_value_index):
    result += numbers[i]

print(result)

first_positive_index = last_positive_index = 0
for i in range(ARR_SIZE):
    if numbers[i] > 0:
        first_positive_index = i
    break

for i in range(ARR_SIZE - 1, -1, -1):
    if numbers[i] > 0:
        last_positive_index = i
        break
print(first_positive_index, last_positive_index)

result = 0
for i in range(first_positive_index + 1, last_positive_index):
    result += numbers[i]
