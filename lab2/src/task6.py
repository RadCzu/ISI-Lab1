from bs4 import BeautifulSoup, SoupStrainer, PageElement
import requests


class PropertyListing:
    def __init__(self, location, full_price, price_per_meter, surface):
        self.location = location
        self.full_price = full_price
        self.price_per_meter = price_per_meter
        self.surface = surface

    def __str__(self):
        return f"Location: {self.location}\n" \
               f"Full Price: {self.full_price}\n" \
               f"Price per Meter: {self.price_per_meter}\n" \
               f"Surface: {self.surface}"


# z góry przepraszam jeśli
URL = ("https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType"
       "=listing")
headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36',
    # Add more headers as needed
}

r = requests.get(URL, headers=headers)

if r.status_code == 200:
    print(r.text)  # Print the content of the response
else:
    print(f'Request failed with status code: {r.status_code}')

soup = BeautifulSoup(r.content, "html.parser")

print(soup.prettify())

only_article_tags = SoupStrainer("article")

offers = soup.find_all(only_article_tags)

offersText = []
for offer in offers:
    offerText: PageElement = offer.find(class_="css-1jy8rmp ev8qziy9")
    # print(offerText)

    offersText.append(offerText)


def parseOfferText(offerText):
    full_price = ''.join(offerText[0:offerText.index('zł')])
    location = ''.join(offerText[(offerText.index('zł')):offerText.index('Liczba')]).replace("zł", "").replace(",", " ")
    price_per_meter = ''.join(offerText[(offerText.index('Cenazametrkwadratowy')):offerText.index('zł/m²')]).replace("Cenazametrkwadratowy", "")
    surface = ''.join(offerText[(offerText.index('Powierzchnia')):offerText.index('m²')]).replace("Powierzchnia", "")
    return PropertyListing(location, full_price, price_per_meter, surface)


offerObjects = []
for offerText in offersText:
    text = offerText.text
    text = text.replace(" ", "")
    print(text)
    offerObjects.append(parseOfferText(text))

for obj in offerObjects:
    print(f"{obj.__str__()}")
