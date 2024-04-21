def calculate_sum_and_multiplication(number):
    digits = str(number)
    length = len(digits)

    if length < 2 or number < 0:
        print("Invalid Input")
        return

    odd_sum = 0
    even_product = 1

    for i in range(length):
        if i % 2 == 0:
            even_product *= int(digits[i])
        else:
            odd_sum += int(digits[i])

    return even_product, odd_sum

if __name__ == "__main__":
    input_number = int(input("Enter a non-negative integer: "))
    result = calculate_sum_and_multiplication(input_number)

    if result:
        print(result[0])  
        print(result[1])  
