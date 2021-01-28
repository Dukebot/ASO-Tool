#Script to read data from the google play store
import play_scraper

def get_app_details(app_id = 'com.android.chrome'):
    return play_scraper.details(app_id)

def get_suggestions(word):
    return play_scraper.suggestions(word)

#This function don't work, the github project must be outdated as the Google Play API changed
def get_app_collection(collection='TRENDING', category='GAME_RACING', results=5, page=0):
    return play_scraper.collection(collection, category, results, page)

#This function don't work, the github project must be outdated as the Google Play API changed
def get_developer_apps(developer_name, results=5, page=0, detailed=False, hl='en', gl='us'):
    return play_scraper.developer(developer_name, results, page, detailed, hl, gl)