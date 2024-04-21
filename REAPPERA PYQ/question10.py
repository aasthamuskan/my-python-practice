# Function to find maximum element in a list
def find_max(lst):
    if not lst:
        return None
    max_element = lst[0]
    for num in lst:
        if num > max_element:
            max_element = num
    return max_element

# Taking input
n = int(input())
elements = []
for _ in range(n):
    elements.append(int(input()))

# Printing the list of elements
for element in elements:
    print(element)

# Finding and printing the maximum element
max_element = find_max(elements)
print(max_element)
