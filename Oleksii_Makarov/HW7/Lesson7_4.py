import re


def numbers_remover(text_path: str):
    # Maybe it should return something? Or this should be enough?
    """
        Takes an existing file with text and rewrites it without numbers. Returns nothing.
    """
    with open(text_path, 'r') as text_input:
        text = text_input.read()
        text_output = re.sub(r'\d', '', text)
    with open(text_path, 'w') as text_result:
        text_result.write(str(text_output))


numbers_remover("./text.txt")
