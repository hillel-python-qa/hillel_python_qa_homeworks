# You have the file text.txt(attached). Please count how many times each letter appears in this task.
import re


def remove_duplicates(item, arr):
    for _ in range(arr.count(item) - 1):
        arr.remove(item)
    return arr


if __name__ == "__main__":
    with open("text.txt", "r") as file:
        text_for_check = file.read()

    letters_from_text = sorted([item.lower() for item in re.findall(r"[A-Za-z]{1}", text_for_check)])

    for item in letters_from_text:
        if item.isalpha():
            print(f'Number of letter {item.upper()} in text is: {letters_from_text.count(item)}\n')
            remove_duplicates(item, letters_from_text)
        else:
            continue

