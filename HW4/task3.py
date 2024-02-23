# 1
text = "Good morning everyone"
print(text)

text = text.replace("morning", "night", 1)
print(text)


# 2
text = input("Введіть рядок: ")
word_to_find = input("Введіть слово для пошуку: ")
word_to_replace = input("Введіть слово для заміни: ")

new_text = text.replace(word_to_find, word_to_replace)

print("Отриманий рядок:", new_text)
