def filter_string(input_string):
    refined_string = ''.join(char.upper() for char in input_string if char.isalpha())
    return refined_string

# Example Usage
if __name__ == "__main__":
    input_string = input().strip()
    initial_length = len(input_string)
    refined_string = filter_string(input_string)
    refined_length = len(refined_string)

    print(refined_string)
    print(initial_length)
    print(refined_length)
