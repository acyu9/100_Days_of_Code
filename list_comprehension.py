numbers = [1, 1, 2, 3, 5, 8, 13, 21, 24, 35]

#squared_numbers = [n ** 2 for n in numbers]
#print(squared_numbers)

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)