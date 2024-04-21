class WordReverser:
    def __init__(self):
        self.word = ""

    def set_word(self, word):
        self.word = word

    def reverse_word(self):
        reversed_word = self.word[::-1]
        return reversed_word

# Example Usage
if __name__ == "__main__":
    input_word = input("Enter a word: ")
    
    reverser = WordReverser()
    reverser.set_word(input_word)
    reversed_word = reverser.reverse_word()
    
    print("Original word:", input_word)
    print("Reversed word:", reversed_word)
