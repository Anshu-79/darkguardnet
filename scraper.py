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

    # Remove empty strings and strip whitespaces
    phrases = [phrase.strip() for phrase in phrases if phrase.strip()]

    return phrases
