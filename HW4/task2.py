text = input("Input your text : ")
search = input("Input searching symbol: ")

index = text.find(search)

if index >= 0:
    print(f"The symbol '{search}' is found at index {index}.")
else:
    print(f"The symbol '{search}' is not found in the text.")
