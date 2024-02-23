text = input("Input your text : ")

letter_count = 0
digit_count = 0

for symbol in text:
    try:
        if symbol.isalpha():
            letter_count += 1
        elif symbol.isdigit():
            digit_count += 1
        else:
            raise ValueError("it is not text and not digit")
    except ValueError as e:
        print(e)

print("Number of letters:", letter_count)
print("Number of digits:", digit_count)




