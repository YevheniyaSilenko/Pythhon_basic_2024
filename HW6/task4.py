def remove_element(list, num):
    count = 0
    while num in list:
        list.remove(num)
        count += 1
    return count


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_to_remove = 5
result = remove_element(my_list, number_to_remove)
print(result)
print(my_list)
