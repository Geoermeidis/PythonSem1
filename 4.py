import re
import random

file = open("temp.txt", "r", encoding="utf-8")
text = ""

for line in file:
    line = line.replace("\n", " ")
    if line == "":
        continue
    text += line

file.close()

new_text = ""

for char in text:
    if char.isalpha() or char == " ":
        new_text += char.lower()

new_text = re.split(" ", new_text)

if new_text[0] == "":  # case if the first character was a space
    del new_text[0]

i = 0
while i < len(new_text):
    if new_text[i] == "":  # remove new lines
        del new_text[i]
        i -= 1
    else:
        i += 1

triples = []

for i in range(len(new_text)-2):  # make the triplets
    print(new_text[i:i+3])
    triples.append(new_text[i:i+3])

random.shuffle(triples)  # shuffle them
final_text = [triples[random.randrange(len(triples))]]  # pick one random triplet to be th start
final_text_str = ""

i = 0
while i < 199:
    matches = []

    for j in range(len(triples)):
        if triples[j][0] == final_text[i][1] and triples[j][1] == final_text[i][2]:  # secure the same words
            matches.append(triples[j])

    if not matches:
        print(final_text_str)
        quit()
    else:
        final_text.append(matches[random.randrange(len(matches))])  # add to the text one random triplets that matches
        final_text_str += final_text[i][2] + " "
    i += 1

print(final_text_str)
