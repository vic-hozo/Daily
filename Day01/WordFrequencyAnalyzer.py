#IMPORTANT
#str.translate() is a string method that returns a new string where each
#character is replaced (or removed) according to a translation table.
#The translation table is usually created using str.maketrans().
from collections import Counter
import string

user_input = input("Enter a paragraph: ")

remove_punctuation = str.maketrans('', '', string.punctuation) #remove punctuations
cleaned_text = user_input.translate(remove_punctuation).lower() #to lowercase the input

counts = Counter(cleaned_text.split()) #split the user input and count how many times each word appears
counts.most_common() #sort to most common to least

print(counts)


