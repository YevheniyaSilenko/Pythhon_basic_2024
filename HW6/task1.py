def product_of_elements(list):
    product = 1
    for num in list:
        product *= num
    return product


my_list = [2, 3, 4, 5]
result = product_of_elements(my_list)
print(result)
