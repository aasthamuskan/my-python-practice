def get_ascii_value(string):
    if len(string) == 0:
        return "Invalid Input"

    first_char = string[0]
    ascii_value = ord(first_char)
    return ascii_value

# Example Usage
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result = get_ascii_value(input_string)

    print(result)
