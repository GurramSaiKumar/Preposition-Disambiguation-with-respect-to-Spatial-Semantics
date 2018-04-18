import nltk

s="About 20 kids in traditional clothing and hats waiting on stairs."

list_of_words = s.split()
next_word = list_of_words[list_of_words.index("clothing") - 1]
print(next_word)
