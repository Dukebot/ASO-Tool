import json
import sys
import re

def create_json_file(json_string, json_file_path = 'json/result.json'):
    with open(json_file_path, 'w') as fp: 
        json.dump(json_string, fp, indent=4)

def create_file(text, file_path = 'text_files/result.txt'):
	file = open(file_path,"w+")
	file.write(text)
	file.close()

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