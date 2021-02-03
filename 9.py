import math

with open("temp2.txt", "r", encoding="utf-8") as file:
    text = file.read()

odd_chars = []

for char in text:
    if ord(char) % 2 == 1:
        odd_chars.append(char)

occurrence = {}
total = len(odd_chars)  # total uneven characters

letters = [char for char in odd_chars if char.isalpha()]

for char in letters:
    occurrence[char] = math.ceil(letters.count(char) / total * 100)

for char, number in zip(occurrence.keys(), occurrence.values()):
    bars = ""
    for i in range(number):
        bars += "*"
    print(f"{char}: {bars}")
