
if __name__ == '__main__':
    with open("text.txt", "r") as file:
        frequency_text = file.read()

        for letter in set(frequency_text.lower()):
            if letter in "abcdefghijklmnopqrstuvwxyz":
                print("Frequency of letters:", ','.join(('{}-{}'.format(letter, frequency_text.lower().count(letter)))))
