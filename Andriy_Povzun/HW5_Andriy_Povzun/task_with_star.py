import re

with open('index.html', 'r') as file:
    html_data = file.read()

id_data = re.findall(r'id=\"[^id=\"block]\w+', html_data)
list_links = re.findall(r'href=\"http://\w+\.[a-z]+/\w+-*\w+|href=\"[a-z]+\.[a-z]+\.[a-z]+|href=\"[a-z]+.[a-z]+',
                        html_data)
text_of_the_links = re.findall(r'[A-Z]{1}[a-z]{2,}', html_data)

id_data = ' '.join(id_data).replace('id=\"', '').split(' ')
list_links = ' '.join(list_links).replace('href=\"', '').split(' ')

finish_list = []
for i in range(len(id_data)):
    finish_list.append([(id_data[i], list_links[i], text_of_the_links[i])])
print(finish_list)
