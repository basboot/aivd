import re
import time
from urllib.parse import urlencode

from bs4 import BeautifulSoup
from selenium import webdriver

import openpyxl

#
# base_url = "https://songteksten.net/lyric/188/5558/bob-marley/three-little-birds.html"
# # Full URL
# full_url = f""
#
# print(full_url)
#
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
#
# # Create a new Chrome WebDriver instance
# driver = webdriver.Chrome(options=options)
# # driver.maximize_window()
#
# # Navigate to a website
# driver.get(full_url)
#
# # Get the html page source of the current page
# page_source = driver.page_source

#
#
#
# # Print the page source
# # print(page_source)
#
# soup = BeautifulSoup(page_source, 'html.parser')
#
# songtext_paragraphs = soup.find_all('body') # class_='songtext'

s = """
Hier heb ik nog een foto van heel lang geleden
Maar als ik blijf kijken dan wordt het weer heden
Gemaakt op de ochtend van mijn vijfde verjaardag
De kamer vol slingers, 't cadeau dat al klaar lag
Het schippersclaviertje, de wens van mijn dromen
Heb ik 's middags nog mee naar het circus genomen
En brandweerman worden was het doel van het leven
Die dromen zijn over, 't gevoel is gebleven

refr.:
Diep in m'n hart verlang ik vaak naar dat kind terug
Kinderen willen groot zijn, nou dat gaat vlug
Als me het leven tegenzit, denk ik aan die tijd
Al werd ik nooit die brandweerman, raakte het kind niet kwijt

Toch leek alles heel simpel, geen zorgen geen twijfel
Van god kwam het goede en het kwaad van de duivel
De klok aan de muur hing daar puur voor het mooie
Ik had alle tijd in de buurt rond te schooien
Een zee was een slootje, m'n klomp was een bootje
En de dood was zoiets als de poes van m'n grootje
De wereld was niet groter dan de globe van vader
Ik kan hem met m'n pink om z'n as laten draaien

refr

Alleen zijn of eenzaam hoe kon ik dat kennen
Ik hoefde alleen maar naar huis toe te rennen
Met een gat in m'n kop en m'n broek vol met scheuren
Mijn moeder was thuis dus wat kon me gebeuren

Als me het leven tegenzit, denk ik aan die tijd
Al werd ik nooit een Ivanhoe,ik raakte het kind niet kwijt
"""
songtext_paragraphs = [s]

for p in songtext_paragraphs:
    text = p.replace("\n", " ").replace("  ", " ").upper()
    print(text)
    processed_text = re.sub(r'[^AEIOU\s]', '', text)
    print(processed_text)


    # Regex pattern to find 4 words with specific vowel sequences
    patterns = [
        r'\bAIEO\b\s+\bAIEO\b\s+\bAIEO\b\s+\bIAO\b',
        r'\bA\b\s+\bA\b\s+\bA\b\s+\bI\b\s+\bEE\b\s+\bA\b\s+\bA\b\s+\bA\b\s+\bI\b\s+\bEE\b\s+\bA\b\s+\bA\b\s+\bU\b',
        r'\bOEE\b\s+\bUI\b\s+\bO\b\s+\bE\b\s+\bAE\b\s+\bA\b\s+\bOI\b\s+\bEE\b\s+\bAE\b',
        r'\bO\b\s+\bI\b\s+\bI\b\s+\bO\b\s+\bI\b\s+\bI\b\s+\bOU\b\s+\bEE\b\s+\bEE\b',
    ]

    # Perform the search
    for i, pattern in enumerate(patterns):
        # print(processed_text)
        matches = re.findall(pattern, processed_text)

        if len(matches) > 0:
            print("FOUND")
            print(text)

time.sleep(1)
