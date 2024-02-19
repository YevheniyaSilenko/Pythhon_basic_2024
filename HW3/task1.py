try:

    day_number = int(input("Enter numbers of week (1-7): "))

    # Використовуємо match
    match day_number:
        case 1:
            print("monday")
        case 2:
            print("tuesday")
        case 3:
            print("wednesday")
        case 4:
            print("thursday")
        case 5:
            print("friday")
        case 6:
            print("saturday")
        case 7:
            print("sunday")
        case _:
            # Виводимо повідомлення про помилку, якщо номер дня тижня не відповідає жодному дню
            raise ValueError("Enter numbers from 1 till 7.")

except ValueError as e:
    print(f"Error: {e}")
