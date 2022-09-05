import re
text = ''.join(open("/Users/olya/Downloads/text_file/text").readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
print(text)
