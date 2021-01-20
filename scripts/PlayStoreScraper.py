#Script to read data from the google play store
import play_scraper

def get_app_details(app_id = 'com.android.chrome'):
    return play_scraper.details(app_id)