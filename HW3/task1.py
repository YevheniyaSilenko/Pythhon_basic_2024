try:

    day_number = int(input("Введіть номер дня тижня (1-7): "))

    # Використовуємо match
    match day_number:
        case 1:
            print("понеділок")
        case 2:
            print("вівторок")
        case 3:
            print("середа")
        case 4:
            print("четвер")
        case 5:
            print("п'ятниця")
        case 6:
            print("субота")
        case 7:
            print("неділя")
        case _:
            # Виводимо повідомлення про помилку, якщо номер дня тижня не відповідає жодному дню
            raise ValueError("Введіть число від 1 до 7.")

except ValueError as e:
    print(f"Error: {e}")
