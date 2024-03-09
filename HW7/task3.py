def sum_range(a, b):
    if a == b:
        return a
    else:
        return a + sum_range(a + 1, b)


print(sum_range(1, 5))

# sum_range(1, 5) -> 1 + sum_range(2, 5)
# sum_range(2, 5) -> 2 + sum_range(3, 5)
# sum_range(3, 5) -> 3 + sum_range(4, 5)
# sum_range(4, 5) -> 4 + sum_range(5, 5)
# sum_range(5, 5) -> 5
