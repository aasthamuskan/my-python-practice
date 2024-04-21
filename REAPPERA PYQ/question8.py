def square_list(lst):
    # List comprehension to square each element and filter out the even numbers
    squares = [x ** 2 for x in lst if x % 2 == 0]
    return squares

def even_checker(lst):
    # List comprehension to filter out the even numbers
    evens = [x for x in lst if x % 2 == 0]
    return evens

# Taking input
input_list = [int(x) for x in input().split(',')]

# Calling the functions
squared_evens = square_list(input_list)
print(','.join(map(str, squared_evens)))
