def get_last_char_ascii(string):
    if len(string) == 0:
        return "Invalid Input"

    last_char = string[-1]
    ascii_value = ord(last_char)
    return ascii_value

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result = get_last_char_ascii(input_string)

    print(result)
