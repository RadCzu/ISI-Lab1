from pathlib import Path
import re

contents = Path("../text/test.txt").read_text()

print(contents)

contents = re.sub(",", "", contents)

words = contents.split(" ")

longestWord = ""
for word in words:
    if len(word) > len(longestWord):
        longestWord = word

print(f"\n{longestWord}")

