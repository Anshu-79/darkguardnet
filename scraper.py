import requests
from bs4 import BeautifulSoup
import re

def extract_phrases(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all text in the webpage
    texts = soup.stripped_strings

    phrases = []
    for text in texts:
        # Splitting text into phrases based on punctuation
        phrases.extend(re.split(r'[.!?]', text))

    # Remove single words, empty strings and strip whitespaces
    phrases = [phrase for phrase in phrases if len(phrase.split()) > 2]

    # Remove duplicate phrases
    return list(set(phrases))
