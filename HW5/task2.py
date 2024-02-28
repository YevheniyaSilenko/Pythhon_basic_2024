import random

# Створення списку цілих чисел, заповненого випадковими числами
random_numbers = [random.randint(-100, 100) for _ in range(20)]

# Створення списку цілих, що містить лише парні числа з першого списку
even_numbers = [num for num in random_numbers if num % 2 == 0]

# Створення списку цілих, що містить лише непарні числа з першого списку
odd_numbers = [num for num in random_numbers if num % 2 != 0]

# Створення списку цілих, що містить лише негативні числа з першого списку
negative_numbers = [num for num in random_numbers if num < 0]

# Створення списку цілих, що містить лише позитивні числа з першого списку
positive_numbers = [num for num in random_numbers if num > 0]

# Виведення результатів
print("Випадкові числа:", random_numbers)
print("Парні числа:", even_numbers)
print("Непарні числа:", odd_numbers)
print("Негативні числа:", negative_numbers)
print("Позитивні числа:", positive_numbers)
