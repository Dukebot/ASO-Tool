import PlayStoreScraper
import Helper
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
words_to_ignore = ["de", "en", "y", "el", "la", "no" , "a", "para", "tu", "que", "pero", "más", "esta", "es", "un", "una", "mã¡s","the", "in", "to", "of", "and", "than", "o", "more", "mas", "los", "del", "con", "you", "your", "is", "while", "for", "with", "you're", "yourself", "but", "will", "on", "-", "by", "at", "an", "all", "who", "if", "not", "his", "himself", "he", "as", "let's", "it's", "we", "are", "it", "can", "can't", "be", "this", "it", "when", "only", "its", "how", "also", "us", "those", "cannot"]


#Analyzes and array of apps ids and creates a single file per app
def main():
    analyze_apps()
    

def analyze_apps():
    for app_id in app_ids: 
        analyze_app(app_id)


#Analyzes the keyword density of a given app id (package name)
def analyze_app(app_id):
    app_details = PlayStoreScraper.get_app_details(app_id)
    title = app_details["title"]
    description = app_details["description"]
    
    all_word_results = calculate_keyword_density(title + " " + description, words_to_ignore)

    one_word_result = all_word_results[0]
    two_word_result = all_word_results[1]
    three_word_result = all_word_results[2]

    text_result = create_result_text(title, description, one_word_result, two_word_result, three_word_result)
    csv_result = zip(one_word_result, two_word_result, three_word_result)

    Helper.create_file_utf8(text_result, "out/text/" + Helper.reformat_text(title) + ".txt")
    #Helper.create_csv(csv_result, 'out/csv/' + Helper.reformat_text(title) + ".csv")


#Calculates the keyword density of a given text
def calculate_keyword_density(text, words_to_ignore):
    text_formatted = Helper.reformat_text(text)
    
    one_word_result = keydensity(text_formatted, 1, words_to_ignore)
    two_word_result = keydensity(text_formatted, 2, words_to_ignore)
    three_word_result = keydensity(text_formatted, 3, words_to_ignore)

    return [one_word_result, two_word_result, three_word_result]


def create_result_text(app_title, app_description, one_word_result, two_word_result, three_word_result):
    result = "Title ---> " + app_title
    result += "\n\nDescription ---> " + app_description
    
    result += "\n\nOne word results\n"
    for res in one_word_result:
        result += "\n" + res
    
    result += "\n\nTwo words results\n"
    for res in two_word_result:
        result += "\n" + res
    
    result += "\n\nThree words results\n"
    for res in three_word_result:
        result += "\n" + res
    
    return result


def analyze_trap_ball_description():
    text = Helper.read_text_from_file("files/trap ball long description.txt")
    all_word_results = calculate_keyword_density(text, words_to_ignore)
    
    one_word_result = all_word_results[0]
    two_word_result = all_word_results[1]
    three_word_result = all_word_results[2]

    result = create_result_text("Trap Ball", text, one_word_result, two_word_result, three_word_result)
    print(result)


main()