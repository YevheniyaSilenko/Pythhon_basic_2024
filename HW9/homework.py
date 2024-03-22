import re


# Переписати слова, які складаються не менше ніж з семи літер
def rewrite_long_words(input_file: object, output_file: object) -> object:
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    long_words = re.findall(r'\b\w{7,}\b', content)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(' '.join(long_words))


# Підрахувати кількість слів у тексті
def count_words(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    words = re.findall(r'\b\w+\b', content)
    return len(words)


# Заміна неприпустимих слів на *
def replace_invalid_words(input_file, invalid_word, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    replaced_content = re.sub(r'\b' + re.escape(invalid_word) + r'\b', '*' * len(invalid_word), content)
    replacements = content.count(invalid_word)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(replaced_content)

    return replacements


if __name__ == "__main__":
    # Завдання 1
    rewrite_long_words('input.txt','output1.txt')

    # Завдання 2
    word_count = count_words('input.txt')
    print("Кількість слів у тексті:", word_count)

    # Завдання 3
    invalid_word = 'die'
    replacements = replace_invalid_words('input.txt', invalid_word, 'output3.txt')
    print(f"Статистика: {replacements} заміни слова {invalid_word}.")
