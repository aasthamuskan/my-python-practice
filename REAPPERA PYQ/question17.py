user_input = input()

last_character_ascii = ord(user_input[-1])

print(last_character_ascii)
#if we want the middle value of the string then the code goes like..

def print_middle_char_ascii(s):
    middle_index = len(s) // 2
    middle_char = s[middle_index]
    ascii_value = ord(middle_char)
    print(ascii_value)
 #without def function 
s = "Hello, world!"
middle_index = len(s) // 2
middle_char = s[middle_index]
ascii_value = ord(middle_char)
print(ascii_value)

#for first charater 
def print_first_char_ascii(s):
    first_char = s[0]
    ascii_value = ord(first_char)
    print(ascii_value) 

#without def function
s = "Hello, world!"
first_char = s[0]
ascii_value = ord(first_char)
print(ascii_value)