#https://pypi.org/project/google-play-scraper/
from google_play_scraper import app, Sort, reviews, reviews_all


def get_app_detail():
    app_package = 'com.android.chrome'
    language = "lang='es'"
    country = "country='sp'"
    result = app(app_package, language, country)
    print(result)


def get_reviews():
    result, continuation_token = reviews(
        'com.fantome.penguinisle',
        lang='en', # defaults to 'en'
        country='us', # defaults to 'us'
        sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
        count=3, # defaults to 100
        filter_score_with=5 # defaults to None(means all score)
    )
    
    # If you pass `continuation_token` as an argument to the reviews function at this point,
    # it will crawl the items after 3 review items.
    result, _ = reviews(
        'com.fantome.penguinisle',
        continuation_token=continuation_token # defaults to None(load from the beginning)
    )
    print(result)

def get_all_reviews():
    result = reviews_all(
        'com.fantome.penguinisle',
        sleep_milliseconds=0, # defaults to 0
        lang='en', 
        country='us', 
        sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
        filter_score_with=5 # defaults to None(means all score)
    )
    print(result)


get_app_detail()
#get_reviews()
#get_all_reviews()
