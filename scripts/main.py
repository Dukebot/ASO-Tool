from PlayStoreScraper import get_app_details
from Helper import reformat_text, create_file_utf8
from KeywordDensityChecker import keydensity

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


def calculate_keyword_density(text, max_results):
    text_formatted = reformat_text(text)
    
    one_word_result = keydensity(text_formatted, 1)
    two_word_result = keydensity(text_formatted, 2)
    three_word_result = keydensity(text_formatted, 3)

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


def analyze_app(app_id, max_results = 100):
    app_details = get_app_details(app_id)
    
    result = "Title ---> " + app_details["title"]
    result += "\n\nDescription ---> " + app_details["description"]
    result += calculate_keyword_density(app_details["description"], max_results)
    
    create_file_utf8(result, "text_files/" + app_id.replace(".", "_") + ".txt")


def analyze_apps(app_ids):
    for app_id in app_ids:
        analyze_app(app_id)


def analyze_all_in_one_go(app_ids):
    all_text = ""
    for app_id in app_ids:
        app_details = get_app_details(app_id)
        all_text += app_details["title"] + " " + app_details["description"]
    result = calculate_keyword_density(all_text, 100)
    create_file_utf8(result)


analyze_all_in_one_go(app_ids)
