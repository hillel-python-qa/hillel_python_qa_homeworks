import re
import string

with open('text.txt', 'r') as file:
    text = file.read()
upper_alphabet = string.ascii_uppercase
lover_aplhabet = string.ascii_lowercase

for letter in upper_alphabet:
    upper_letters = re.findall(letter, text)
    print(f'Number of letter {letter} in upper case: {upper_letters.count(letter)}\n')

for lover_letter in lover_aplhabet:
    lover_letters = re.findall(lover_letter, text)
    print(f'Number of letter {lover_letter} in lover case: {lover_letters.count(lover_letter)}\n')