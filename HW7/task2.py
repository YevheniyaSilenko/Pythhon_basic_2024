def print_stars(N):
    if N <= 0:
        return
    else:
        print('*', end='')
        print_stars(N - 1)


num_stars = int(input("Введіть кількість зірок: "))
print_stars(num_stars)

# print_stars(5) -> '*' + print_stars(4)
# print_stars(4) -> '*' + print_stars(3)
# print_stars(3) -> '*' + print_stars(2)
# print_stars(2) -> '*' + print_stars(1)
# print_stars(1) -> '*' + print_stars(0)
