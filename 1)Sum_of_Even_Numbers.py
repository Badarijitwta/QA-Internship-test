#Using for loop

def sum_even_numbers(numbers):
    result = 0
    
    for num in numbers:
        # Check if the number is even
        if num % 2 == 0:
            # If the number is even, add it to the sum
            result += num
    
    # Return the sum or total value
    return result


#Using built in function
def sum_even_numbers_built_in(numbers):
    total = sum(filter(lambda num: num % 2 == 0, numbers))
    return total

numbers=[1,2,3,4,5,6,7,8]
print(sum_even_numbers_built_in(numbers))
print(sum_even_numbers(numbers))