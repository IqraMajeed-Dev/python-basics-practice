
numbers = [1, 2, 3, 4, 5]
odd_numbers = [x for x in numbers if x % 2 != 0]
even_numbers = [x for x in numbers if x % 2 == 0]

odd_numbers = odd_numbers[::-1]
even_numbers = even_numbers[::-1]

result = []
odd_index = 0
even_index = 0

for num in numbers:
    if num % 2 != 0: 
        result.append(odd_numbers[odd_index])
        odd_index += 1
    else: 
        result.append(even_numbers[even_index])
        even_index += 1

print(result)

numbers = [1, 2, 3, 4, 5]

even_numbers = [x for x in numbers if x % 2 == 0]

even_numbers[0], even_numbers[-1] = even_numbers[-1], even_numbers[0]

result = []
even_index = 0

for num in numbers:
    if num % 2 == 0:  
        result.append(even_numbers[even_index])
        even_index += 1
    else:
        result.append(num)  

print(result)

