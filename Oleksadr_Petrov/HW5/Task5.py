import re
result = []
with open('text', 'r') as file:
    text = file.read()
    step1 = re.sub('(\.){2,}', ".  ", text)
    step2 = re.split('\.\ ', step1)
    for sent in step2:
        if len(re.findall('[a-z]\.[A-Z]', sent)) > 1:
            result.append(re.sub('\.', ' ', sent).strip())
        elif len(re.findall('[a-z]\.[A-Z]', sent)) == 1:
            for substr in re.split('\.', sent):
                result.append(substr.strip())
        else:
            result.append(sent.strip())
for sent in result:
    print(sent)



