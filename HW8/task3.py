import re


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


# Тестові дані
test_emails = [
    "example@example.com",
    "user@example",  # Без домену
    "user@example.",  # Некоректний домен
]

for email in test_emails:
    print(f"{email}: {validate_email(email)}")
