from bs4 import BeautifulSoup, SoupStrainer

with open("../html/links.html") as fp:
    soup = BeautifulSoup(fp)

print(soup.prettify())

only_a_tags = SoupStrainer("a")

atags = soup.find_all(only_a_tags)
print(soup.find_all(only_a_tags))

links = []
for tag in atags:
    links.append(tag['href'])

print(links)

