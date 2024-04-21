def sum_and_product_of_digits(number):
    digits = [int(digit) for digit in str(number)]
    digit_sum = sum(digits)
    
    product = 1
    for digit in digits:
        product *= digit
    
    return digit_sum, product


if __name__ == "__main__":
    input_number = int(input("Enter an integer: "))
    result_sum, result_product = sum_and_product_of_digits(input_number)

    print("Sum of digits:", result_sum)
    print("Product of digits:", result_product)
