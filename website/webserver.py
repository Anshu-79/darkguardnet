
import scraper


def scrape(text):
    return scraper.extract_phrases(text)

def submit_form(request):

    phrases = scrape(request)
    phrase_dict = dict(zip(phrases, dps_predictor.are_dark_patterns(phrases)))

    dp_count = list(phrase_dict.values()).count(True)
    
    dark_patterns = [k for k in phrase_dict.keys() if phrase_dict.values() == True]
    classified_dp = dpc_predictor.make_predictions(dark_patterns)
    dp_types = {i:classified_dp.count(i) for i in set(classified_dp)}

submit_form("https://amazon.in")