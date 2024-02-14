from django.shortcuts import render, redirect
from django.http import HttpResponse

import sys
import logging
import warnings

warnings.filterwarnings("ignore")
logging.getLogger("transformers.modeling_utils").setLevel(logging.ERROR)
sys.path.append('D:/Programming/DPBH-Team_Veritas/')

import scraper
from dark_pattern_spotter import predictor as dps_predictor
from dark_pattern_classifier import predictor as dpc_predictor

def scrape(text):
    return scraper.extract_phrases(text)

def submit_form(request):
    if request.method == 'POST':
        text_value = request.POST.get('inputbox')
        phrases = scrape(text_value)
        print("Total phrases found =", len(phrases))
        phrase_dict = {}
        for idx, phrase in enumerate(phrases):
            is_dp = dps_predictor.is_dark_pattern(phrase)
            phrase_dict[phrase] = is_dp
            print(f"{idx+1}. {phrase} => {is_dp}")

        dark_patterns = [k for k in phrase_dict if phrase_dict[k] == True]
        print("Total dark patterns found =", len(dark_patterns))

        classified_dp = {}
        for idx, dp in enumerate(dark_patterns):
            category = dpc_predictor.make_prediction(dp)
            classified_dp[dp] = category
            print(f"{idx+1}. {dp} => {category}")

        categories = ['Misdirection', 'Scarcity', 'Social Proof', 'Urgency']
        dp_types = {}
        for category in categories:
            if category in classified_dp.values():
                dp_types[category] = list(classified_dp.values()).count(category)
            else:
                dp_types[category] = 0
        
        for type in dp_types:
            print(f"Total {type} = {dp_types[type]}")
        
        processed_data = [len(phrases), len(dark_patterns)]
        processed_data.extend(dp_types.values())

        return render(request, 'result.html', {'processed_data': processed_data})
    
    else:
        return render(request, 'search.html')    
        

def process_form(request):
    pass


def home(request):
    return render(request, 'search.html')
