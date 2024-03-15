import re


def validate_home_phone(phone_number):
    pattern = r'^\d{5,15}$'  # Від 5 до 15 цифр
    return bool(re.match(pattern, phone_number))


# Тестові дані
test_phone_numbers = [
    "12345",
    "12345678901",
    "123-456-789",  # Некоректний формат
    "12345678901234567890"  # Надто довгий номер
]

for phone_number in test_phone_numbers:
    print(f"{phone_number}: {validate_home_phone(phone_number)}")
