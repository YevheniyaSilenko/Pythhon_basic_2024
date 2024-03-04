def find_minimum(list):
    if not list:
        return None
    min_element = list[0]
    for num in list:
        if num < min_element:
            min_element = num
    return min_element


my_list = [5, 3, 8, 2, 1]
result = find_minimum(my_list)
print(result)  # Output: 1
