import re

file = open("index.html")
html = file.read()
file.close()
result = []
id = re.findall("\"[a-z]{5,}\"", html)
url = re.findall("href\S\"[a-z]{3,}\S{2,}\.[a-z]{3}", html)
anchor = re.findall("[A-Z]{1}[a-z]{5,}", html)
id = "".join(id).replace('"', " ").lstrip().rstrip().split("  ")
url = "".join(url).replace('href=', "").replace('"', " ").lstrip().rstrip().split(" ")

for i in range(len(url)):
    result.append((id[i], url[i], anchor[i]))

print(result)
