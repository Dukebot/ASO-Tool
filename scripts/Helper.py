import sys
import re
import json
import csv

def create_json_file(json_string, json_file_path = 'out/json/result.json'):
    with open(json_file_path, 'w') as fp: 
        json.dump(json_string, fp, indent=4)

def create_file(text, file_path = 'out/text/result.txt'):
	file = open(file_path,"w+")
	file.write(text)
	file.close()

def create_file_utf8(text, file_path = 'out/text/result.txt'):
	with open(file_path, "w+", encoding="utf-8") as file:
		file.write(text)
		file.close()

def create_csv(data, excel_path = 'out/csv/result.csv'):
	with open(excel_path, 'w') as csv_file:
		csv_writer = csv.writer(csv_file, dialect='excel')
		csv_writer.writerows(data)

def read_text_from_file(file_path):
	file_text = open(file_path).read() # Read the text from the file
	transformed = file_text.lower() # Text to lowercase
	clean = re.sub('[.,!?;:()*&^%$#@_+\~"]', '', transformed) # Replace all the signs with empty string
	reformat = ' '.join(clean.split()) # Get rid of the line breaks
	return reformat #Return the text formatted

def reformat_text(text):
	transformed = text.lower() # Text to lowercase
	clean = re.sub('[.,!?;:()*&^%$#@_+\~"]', '', transformed) # Replace all the signs with empty string
	reformat = ' '.join(clean.split()) # Get rid of the line breaks
	return reformat #Return the text formatted

def de_emojify_text(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
							"]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'', text)