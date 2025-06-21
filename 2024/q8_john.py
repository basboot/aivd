import re
import time
from urllib.parse import urlencode

from bs4 import BeautifulSoup
from selenium import webdriver

import openpyxl

# Define variable to load the dataframe
dataframe = openpyxl.load_workbook("top2000.xlsx")

# Define variable to read sheet
dataframe1 = dataframe.active


# Iterate the loop to read the cell values
skip = True
colums = list(dataframe1.iter_cols(1, dataframe1.max_column))
for row in range(1, dataframe1.max_row):

    # Convert to query parameters
    params = {'mq': f"{colums[1][row].value.replace('(Albumversie)', '')} {colums[2][row].value}"}
    encoded_params = urlencode(params)

    song = f"{colums[1][row].value.replace('(Albumversie)', '')} {colums[2][row].value}"

    base_url = "https://www.mldb.org/search?"
    # Full URL
    full_url = f"{base_url}{encoded_params}&btnI=I%27m+Feeling+Lucky&si=0&mm=0&ob=1"

    print(full_url)

    url = "https://www.mldb.org/search?mq=Nothing+Else+Matters+Metallica&btnI=I%27m+Feeling+Lucky&si=0&mm=0&ob=1"
    url = "https://www.mldb.org/song-150575-nothing-else-matters-metallica.html"
    url = "https://www.mldb.org/search?mq=Roller+Coaster+Danny+Vera&btnI=I%27m+Feeling+Lucky&si=0&mm=0&ob=1"
    url = full_url

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # Create a new Chrome WebDriver instance
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()

    # Navigate to a website
    driver.get(url)

    # Get the html page source of the current page
    page_source = driver.page_source



    # Print the page source
    # print(page_source)

    soup = BeautifulSoup(page_source, 'html.parser')

    songtext_paragraphs = soup.find_all('body') # class_='songtext'
    songtext_paragraphs = soup.find_all('p', class_='songtext') # class_='songtext'


    print(song)

    if len(songtext_paragraphs) == 0:
        print(f"{song} NOT FOUND")

    for p in songtext_paragraphs:
        text = p.text.replace("\n", " ").replace("  ", " ").upper()

        processed_text = re.sub(r'[^AEIOU\s]', '', text)

        # Regex pattern to find 4 words with specific vowel sequences
        patterns = [
            r'\bAIEO\b\s+\bAIEO\b\s+\bAIEO\b\s+\bIAO\b',
            r'\bA\b\s+\bA\b\s+\bA\b\s+\bI\b\s+\bEE\b\s+\bA\b\s+\bA\b\s+\bA\b\s+\bI\b\s+\bEE\b\s+\bA\b\s+\bA\b\s+\bU\b',
            r'\bOEE\b\s+\bUI\b\s+\bO\b\s+\bE\b\s+\bAE\b\s+\bA\b\s+\bOI\b\s+\bEE\b\s+\bAE\b',
            r'\bO\b\s+\bI\b\s+\bI\b\s+\bO\b\s+\bI\b\s+\bI\b\s+\bOU\b\s+\bEE\b\s+\bEE\b',
            r'\bAY\b\s+\bE\b\s+\bA\b\s+\bAE\b\s+\bA\b\s+\bIIO\b\s+\bO\b\s+\bA\b\s+\bE\b\s+\bO\b\s+\bA\b\s+\bO\b\s+\bEE\b\s+\bEEY\b\s+\bEIOU\b\s+\bI\b\s+\bA\b\s+\bIE\b'
        ]

        # Perform the search
        for i, pattern in enumerate(patterns):
            # print(processed_text)
            matches = re.findall(pattern, processed_text)

            if len(matches) > 0:
                print(text)
                print(f"{song} Found pattern {i + 1}")

    time.sleep(1)

    # Close the browser window
    # driver.quit()