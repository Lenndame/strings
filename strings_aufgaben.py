"""
Write a Python function that takes a list of words
 and return the longest word and the length of the longest one.
 List contains minimum one word

Sample Output:
Longest word: Exercises
Length of the longest word: 9
"""
word_list = ["Amsterdam", "Kopenhagen", "Oslo", "Paris", "London"]

counter = 0
for word, char in enumerate(word_list):
    if len(char) > len(word_list[counter]):
        counter = word

print(f"Längstes Wort: {word_list[counter]}")
print(f"Länge: {len(word_list[counter])} ")
