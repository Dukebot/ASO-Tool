#Allows us to retrieve the app data from the googple play store
from PlayStoreScraper import get_app_details
#Helper functions to process text and create files
from Helper import reformat_text, create_file_utf8
#Function to analyze the key density of a given text
from KeywordDensityChecker import keydensity


#List of application ID's we want to analyze
app_ids = [
    "online.limitless.appleknight.free", #Apple Knight: Action Platformer
    "com.waybefore.fastlikeafox", #Fast like a Fox
    "bounce.global.superbros.adventure.world", #Super Jacky's World - Free Run Game
    "com.mobge.Oddmar", #Oddmar
    "com.raongames.bouneball", #BounceBall
    "com.azurgames.stackball", #Stack Ball - Blast through platforms
    "com.bricks.wall.balls.shooter", #Bricks and Balls - Brick Breaker Game
    "com.amanotes.pamadancingroad", #Dancing Road: Color Ball Run!
    "com.genico.bounce", #Bounce Classic
    "com.endorphin.bouncereloadedhd", #Bounce Ball Classic - Original Retro Game
    "com.bbtv.odd1sout", #TheOdd1sOut: Let's Bounce
    "com.red.ball.ballgames.bounceball.redball5", #Bounce Ball 5 - Jump Ball Hero Adventure
]

#Words that we will filter as we are not interested in them
words_to_ignore = ["de", "en", "y", "el", "la", "no" , "a", "para", "tu", "que", "pero", "más", "esta", "es", "un", "una", "mã¡s","the", "in", "to", "of", "and", "than", "o", "more", "mas", "los", "del", "con", "you", "your", "is", "while", "for", "with", "you're", "yourself", "but", "will", "on", "-", "by", "at", "an", "all", "who", "if", "not", "his", "himself", "he", "as", "let's", "it's", "we", "are", "it", "can", "can't", "be", "this", "it"]

words_to_ignore = []

max_results = 100


#Calculates the keyword density of a given text
def calculate_keyword_density(text):
    text_formatted = reformat_text(text)
    
    one_word_result = keydensity(text_formatted, 1, words_to_ignore)
    two_word_result = keydensity(text_formatted, 2, words_to_ignore)
    three_word_result = keydensity(text_formatted, 3, words_to_ignore)

    result = "\n\nOne word results\n"
    for res in one_word_result[:max_results]:
        result += "\n" + res
    
    result += "\n\nTwo words results\n"
    for res in two_word_result[:max_results]:
        result += "\n" + res
    
    result += "\n\nThree words results\n"
    for res in three_word_result[:max_results]:
        result += "\n" + res
    
    return result


#Analyzes the keyword density of a given app id (package name)
def analyze_app(app_id):
    app_details = get_app_details(app_id)
    title = app_details["title"]
    description = app_details["description"]
    
    result = "Title ---> " + title
    result += "\n\nDescription ---> " + description
    result += calculate_keyword_density(title + " " + description)

    create_file_utf8(result, "text_files/" + reformat_text(title) + ".txt")

#Analyzes and array of apps ids and creates a single file per app
def analyze_apps():
    for app_id in app_ids:
        analyze_app(app_id)


#Merges the texts of all apps and gives the result in one single file
def analyze_all_in_one_go():
    all_text = ""
    for app_id in app_ids:
        app_details = get_app_details(app_id)
        all_text += app_details["title"] + " " + app_details["description"]
    result = calculate_keyword_density(all_text)
    create_file_utf8(result)


#analyze_all_in_one_go()
analyze_apps()