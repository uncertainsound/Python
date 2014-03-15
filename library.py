import re

r = re.compile(r'[a-zA-Z]+')
paragraph = raw_input("Input a paragraph: ")

paragraph = paragraph.replace("'", "")
words = r.findall(paragraph)
dicto = dict()

for each in words:
    number = len(each)
    try:
        dicto[number] = dicto[number] + 1
    except KeyError:
        dicto[number] = 1
    
for each in dicto:
    print dicto[each], "words with ", each, "letters." 


