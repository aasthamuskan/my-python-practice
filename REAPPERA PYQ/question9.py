def english_to_mathematical(input_string):
    mathematical_string = ""
    for char in input_string:
        if char.isalpha():
            # Convert uppercase and lowercase letters to their corresponding numerical values
            mathematical_string += str(ord(char.lower()) - ord('a') + 1)
    return mathematical_string

# Taking input
input_string = input()

# Converting the input string to Mathematical language
mathematical_string = english_to_mathematical(input_string)

# Printing the result
print(mathematical_string)
