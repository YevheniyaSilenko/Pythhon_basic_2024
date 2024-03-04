def power_list(list, power):
    powered_list = [num ** power for num in list]
    return powered_list


my_list = [1, 2, 3, 4, 5]
power_value = 3
result = power_list(my_list, power_value)
print(result)
