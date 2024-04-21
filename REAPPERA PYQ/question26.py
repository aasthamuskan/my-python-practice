class CharacterCounter:
    def __init__(self):
        self.input_string = ""

    def setstring(self, user_input):
        self.input_string = user_input

    def countcharacters(self, char_to_count):
        count = 0
        for char in self.input_string:
            if char == char_to_count:
                count += 1
        return count

# Example Usage
if __name__ == "__main__":
    input_string = input()
    char_to_count = input()
    
    # Creating an instance of the CharacterCounter class
    counter = CharacterCounter()
    # Setting the input string
    counter.setstring(input_string)
    # Counting occurrences of the specified character
    result = counter.countcharacters(char_to_count)
    print(result)
