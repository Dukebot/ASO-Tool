from PlayStoreScraper import get_app_details
from Helper import reformat_text, create_file
from KeywordDensityChecker import keydensity

app_ids = [
    "online.limitless.appleknight.free", #Apple Knight: Action Platformer
    "com.waybefore.fastlikeafox", #Fast like a Fox
    "bounce.global.superbros.adventure.world", #Super Jacky's World - Free Run Game
    "com.raongames.bouneball", #BounceBall
    "com.azurgames.stackball", #Stack Ball - Blast through platforms
    "com.bricks.wall.balls.shooter", #Bricks and Balls - Brick Breaker Game
    "com.amanotes.pamadancingroad", #Dancing Road: Color Ball Run!
    "com.genico.bounce", #Bounce Classic
    "com.endorphin.bouncereloadedhd", #Bounce Ball Classic - Original Retro Game
    "com.bbtv.odd1sout", #TheOdd1sOut: Let's Bounce
    "com.red.ball.ballgames.bounceball.redball5", #Bounce Ball 5 - Jump Ball Hero Adventure
]

#SCRIPT PARAMETERS
app_id = app_ids[1]
cap_results_to = 10

#GET THE APP DATA
app_details = get_app_details(app_id)
title = app_details["title"]
category = app_details["category"]
description = app_details["description"]

#PREPARE THE TEXT THAT WE WANT TO ANALYZE
description = reformat_text(description)

#CALCULATE THE KEYWORD DENSITY
one_word_result = keydensity(description, 1)
two_word_result = keydensity(description, 2)
three_word_result = keydensity(description, 3)

#MERGE RESULTS IN ONE SINGLE STRING
result = "Results for app ---> " + app_id
result += "\n\nOne word results\n"
for res in one_word_result[:cap_results_to]:
    result += "\n" + res
result += "\n\nTwo words results\n"
for res in two_word_result[:cap_results_to]:
    result += "\n" + res
result += "\n\nThree words results\n"
for res in three_word_result[:cap_results_to]:
    result += "\n" + res

#SAVE RESULT INTO FILE
create_file(result, "text_files/" + app_id.replace(".", "_") + ".txt")