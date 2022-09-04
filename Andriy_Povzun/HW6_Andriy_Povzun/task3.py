import re

with open('text.txt', 'r') as file:
    text = file.read()
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lover_aplhabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

i = 0
for letter in upper_alphabet:
    upper_letter = re.findall(upper_alphabet[i], text)
    lover_letter = re.findall(lover_aplhabet[i], text)
    print(f'Count of letter {upper_alphabet[i]} in upper case: {upper_letter.count(upper_alphabet[i])}\n'
          f'Count of letter {lover_aplhabet[i]} in lover case: {lover_letter.count(lover_aplhabet[i])}\n')
    i += 1
