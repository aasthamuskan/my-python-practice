# Taking input for list size
size = int(input())

# Taking input for list elements
elements = list(map(int, input().split()))

# Sorting the list based on conditions
largest_number = max(elements)
if largest_number > 50:
    sorted_elements = sorted(elements, reverse=True)
elif largest_number < 50:
    sorted_elements = sorted(elements)
else:
    sorted_elements = elements

# Printing the sorted list
print(*sorted_elements)
