
word = input("Enter a word: ")
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print("Reversed word:", reversed_word)