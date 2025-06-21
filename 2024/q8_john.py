import re
import time
from urllib.parse import urlencode

from bs4 import BeautifulSoup
from selenium import webdriver

import openpyxl

songs_all = ['song-31762-one-in-a-million.html', 'song-9278-one-in-a-million.html', 'song-2611-one-in-a-million.html', 'song-147768-a-million-miles-away-behind-the-door.html', 'song-132065-one-in-a-million.html', 'song-88720-power-of-a-million-lights.html', 'song-52137-a-million-more.html', 'song-16624-one-in-a-million.html', 'song-246992-mr-never-in-a-million-years.html', 'song-239241-starfish-ride-for-a-million-dollar-handshake.html', 'song-238912-one-in-a-million.html', 'song-238007-a-million-days.html', 'song-223458-a-million-things.html', 'song-220971-never-in-a-million-years.html', 'song-219760-one-in-a-million.html', 'song-217756-dawn-of-a-million-souls.html', 'song-211898-a-million-ways.html', 'song-209131-a-million-ways-to-fall.html', 'song-208245-a-million-to-one.html', 'song-208029-a-million-miles-away.html', 'song-199874-a-million-miles-away.html', 'song-199509-a-million-miles.html', 'song-176853-one-in-a-million.html', 'song-174863-a-million-teardrops.html', 'song-168138-one-in-a-million-world.html', 'song-145713-i-found-a-million-dollar-baby.html', 'song-143148-a-million-things.html', 'song-143001-a-million-miles.html', 'song-136628-i-m-a-million.html', 'song-132369-a-million-miles-to-the-city.html', 'song-130631-one-in-a-million.html', 'song-126855-a-million-to-one.html', 'song-126724-a-million-to-one.html', 'song-125895-one-in-a-million.html', 'song-124541-a-million-years-or-so.html', 'song-120277-one-in-a-million.html', 'song-120267-one-in-a-million.html', 'song-116611-a-million-ways.html', 'song-115664-a-million-to-one.html', 'song-107231-for-a-million-years.html', 'song-107106-one-in-a-million.html', 'song-95111-not-in-a-million-years.html', 'song-83626-maybe-in-a-million-years.html', 'song-82714-a-million-miles-away.html', 'song-80886-a-million-gods.html', 'song-80273-one-in-a-million.html', 'song-77685-two-in-a-million.html', 'song-75697-a-million-years.html', 'song-75377-never-in-a-million-years.html', 'song-71816-never-in-a-million-years.html', 'song-69991-one-in-a-million.html', 'song-69773-for-a-million.html', 'song-59177-they-need-a-million.html', 'song-58912-a-moment-in-a-million-years.html', 'song-55575-land-of-a-million-drums.html', 'song-54533-one-in-a-million.html', 'song-54532-one-in-a-million.html', 'song-52342-i-ll-trade-a-million-dollars.html', 'song-51374-a-million-and-1-questions-extended.html', 'song-41041-one-in-a-million-remix.html', 'song-40639-a-million-miles-away.html', 'song-37805-a-million-and-1-buddah-spots.html', 'song-35647-intro-a-million-and-one-questions-rhyme-no-mor.html', 'song-28958-one-in-a-million.html', 'song-26781-a-million-and-1-questions-extended.html', 'song-26660-intro-a-million-and-one-questions-rhyme-no-mor.html', 'song-25114-i-never-thought-i-d-live-to-be-a-million.html', 'song-24491-land-of-a-million-drums.html', 'song-20783-two-in-a-million.html', 'song-20137-a-million-and-one-things.html', 'song-19653-a-million-love-songs.html', 'song-19088-more-than-a-million-miles.html', 'song-14078-a-million-miles-away.html', 'song-13409-a-million-tears.html', 'song-7781-try-n-2-make-a-million.html', 'song-4299-a-million-miles-away.html', 'song-2643-one-in-a-million.html', 'song-9287-hole-in-my-heart.html', 'song-44594-we-will-meet-again.html', 'song-41181-givin-you-more.html', 'song-41180-i-gotcha-back.html', 'song-31764-never-comin-back.html', 'song-31763-never-giving-up.html', 'song-31761-beats-4-da-streets-intro.html', 'song-31760-everything-s-gonna-be-alright.html', 'song-9288-this-is-our-life.html', 'song-9286-all-because-of-you.html', 'song-9285-i-don-t-wanna-say-goodbye.html', 'song-9284-stay.html', 'song-9283-let-your-soul-shine.html', 'song-9282-we-live.html', 'song-9281-over-the-mountains.html', 'song-9280-where-are-you.html', 'song-9279-i-believe.html', 'song-2625-came-to-give-love.html', 'song-2624-the-one-i-gave-my-heart-to.html', 'song-2623-ladies-in-da-house.html', 'song-2622-never-comin-back.html', 'song-2621-heartbroken.html', 'song-2620-never-givin-up.html', 'song-2619-i-gotcha-back.html', 'song-2618-giving-you-more.html', 'song-2617-everythings-gonna-be-alright.html', 'song-2616-4-page-letter.html', 'song-2615-got-to-give-it-up.html', 'song-2614-choosey-lover-old-school-new-school.html', 'song-2613-if-your-girl-only-knew.html', 'song-2612-a-girl-like-you.html', 'song-2610-hot-like-fire.html']

songs = set(songs_all)


for song in songs:

    base_url = "https://www.mldb.org/"
    # Full URL
    full_url = f"{base_url}{song}"

    print(full_url)

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

    songtext_paragraphs = soup.find_all('p', class_='songtext') # class_='songtext'


    print(song)

    if len(songtext_paragraphs) == 0:
        print(f"{song} NOT FOUND")

    for p in songtext_paragraphs:
        text = p.text.replace("\n", " ").replace("  ", " ").upper()

        processed_text = re.sub(r'[^AEIOU\s]', '', text)

        # Regex pattern to find 4 words with specific vowel sequences
        patterns = [
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