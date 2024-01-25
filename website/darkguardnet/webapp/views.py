from django.shortcuts import render, redirect
from django.http import HttpResponse

import sys
sys.path.append('D:\Programming\DPBH-Team_Veritas')

import scraper
import dark_pattern_spotter
import dark_pattern_classifier

def scrape(text):
    return scraper.extract_phrases(text)
    
def submit_form(request):
    if request.method == 'POST':
        text_value = request.POST.get('inputbox')
        phrases = scrape(text_value)
        phrase_dict = dict(zip(phrases, dark_pattern_spotter.predictor.are_dark_patterns(phrases)))

        dp_count = list(phrase_dict.values()).count(True)
        
        dark_patterns = [k for k in phrase_dict.keys() if phrase_dict.values() == True]
        classified_dp = dark_pattern_classifier.predictor.make_predictions(dark_patterns)
        dp_types = {i:classified_dp.count(i) for i in set(classified_dp)}

        print(dp_types)
        return render(request, 'result.html', {'result': text_value})
        
    else:
        return render(request, 'search.html')
        

def process_form(request):
    pass


def home(request):
    return render(request, 'search.html')
