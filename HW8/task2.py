import re


def validate_mobile_phone(phone_number):
    pattern = r'^\+?\d{10,15}$'  # плюс, від 10 до 15 цифр
    return bool(re.match(pattern, phone_number))


# Тестові дані
test_mobile_numbers = [
    "+1234567890",
    "+12345678901",
    "123-456-789",  # Некоректний формат
    "+12345678901234567890"  # Надто довгий номер
]

for phone_number in test_mobile_numbers:
    print(f"{phone_number}: {validate_mobile_phone(phone_number)}")
