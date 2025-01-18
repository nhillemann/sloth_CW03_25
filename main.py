'''
Sloth Bytes Weekly Challenge - Calendar Week 03 2025

Task: Create a function that takes a string and censors words over four characters with *

Notes:
Don't censor words with exactly four characters.
If all words have four characters or less, return the original string.
The amount of * is the same as the length of the word.
'''

# My solution:
# Function takes user input as string and split it in words
def word_censor():
    text_input = input("Enter your text here:")
    words = text_input.split()

    output_words = []

# If number of chars in word > 4: safe so many asterisks (*) like number of chars in word
    for word in words:
        if len(word) > 4:
            censored_word = "*" * len(word)
            output_words.append(censored_word)
        else:
            output_words.append(word)
# Reassemble the censored words into a string again
    output_text = " ".join(output_words)
    print(f"Output:", output_text)

if __name__ == '__main__':
    word_censor()