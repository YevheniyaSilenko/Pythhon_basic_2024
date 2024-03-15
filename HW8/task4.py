import re


def validate_full_name(full_name):
    pattern = r'^[a-zA-Zа-яА-Я]{2,20}( [a-zA-Zа-яА-Я]{2,20}){2}$'  # 3 слова, кожне від 2 до 20 символів
    return bool(re.match(pattern, full_name))


# Тестові дані
test_names = [
    "Test Name Improve",
    "A B C",  # Замало слів
    "Too Long Name Too Long Name Too Long Name",  # Занадто довгий
    "Тест Наме",  # Кирилиця
    "Test 123 Name"  # Некоректні символи
]

for name in test_names:
    print(f"{name}: {validate_full_name(name)}")
