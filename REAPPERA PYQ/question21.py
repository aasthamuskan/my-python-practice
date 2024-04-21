class WordReverser:
    def __init__(self):
        self.word = ""

    def setword(self, user_input):
        self.word = user_input

    def reverseWord(self):
        reversed_word = self.word[::-1]
        print(reversed_word)

# Example Usage
if __name__ == "__main__":
    reverser = WordReverser()
    user_input = input("Enter a word: ")
    reverser.setword(user_input)
    reverser.reverseWord()
