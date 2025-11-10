def list_product(lst):
    product = 1
    for num in lst:
        product *= num
    return product

numbers = [2, 3, 4, 5]  
result = list_product(numbers)
print("The product of the list items", numbers, "is:", result)
