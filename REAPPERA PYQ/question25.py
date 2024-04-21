def rearrange_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

# Test Case 1
input_sentence = "Hello world! Python is amazing"
output_sentence = rearrange_sentence(input_sentence)
print(output_sentence)

# Additional Inputs
print(rearrange_sentence("Avi"))
print(rearrange_sentence("Dec 14, 2023, 10:16"))
