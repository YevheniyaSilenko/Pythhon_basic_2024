import random


def is_prime(number: int) -> bool:
    is_number_prime = True

    for num in range(2, number):
        if number % num == 0:
            is_number_prime = False
        break

    return is_number_prime


def get_prime_numbers(numbers: list[int]) -> int:
    prime_numbers_counter = 0

    for num in numbers:
        if is_prime(num):
            print(num, end=" ")
            prime_numbers_counter += 1

    print()
    return prime_numbers_counter


my_numbers = [random.randint(1, 20) for _ in range(10)]
print(my_numbers)
result = get_prime_numbers(my_numbers)
print(f"Prime numbers count: {result}")
