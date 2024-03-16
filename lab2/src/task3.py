import string
from pathlib import Path
from random import randint

filename = "passwords.txt"
filepath = "../text"

alphabet = string.ascii_letters
print(alphabet)
numbers = string.digits

letters = f"{alphabet}{numbers}"

words = []

for i in range(0, 1000):
    word = ""
    for j in range(0, 6):
        randomIndex = randint(0, len(letters) - 1)
        word += letters[randomIndex]
    words.append(word)

string = ""
for word in words:
    string += f"{word} "

Path(f"{filepath}/{filename}").write_text(string)
