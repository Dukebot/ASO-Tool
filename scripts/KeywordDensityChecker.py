#Words that we will filter as we are not interested in them
words_to_ignore = ["de", "en", "y", "el", "la", "no" , "a", "para", "tu", "que", "pero", "más", "esta", "es", "un", "una", "mã¡s","the", "in", "to", "of", "and", "than", "o", "more", "mas", "los", "del", "con", "you", "your", "is", "while", "for", "with", "you're", "yourself", "but", "will", "on", "-", "by", "at", "an", "all", "who", "if", "not", "his", "himself", "he", "as", "let's", "it's", "we", "are", "it", "can", "can't", "be", "this"]

words_to_ignore = []


#Return the list of words of the given text filtering the words in the list providced
def get_words_list(text, words_to_filer):
	all_words = text.split(' ') # Get the words into a list
	
	# Filter the words that we don't want
	filtered_words = []
	for word in all_words:
		if not word in words_to_filer:
			filtered_words.append(word)
	return filtered_words


def one_word(word_list):
	uniquewords = set(word_list) # Create a list of unique words
	total = len(word_list) # Count total of all words
	
	# Prepare a new empty list(Product=[]), create a loop where each word in unique words is counted(how many times it repeats in word_list)
	# Each word is then calculated and formated to a percentage of the total. Both the word and its percentage are added to the new list as a single element.
	product = []
	for word in uniquewords:
		result = word_list.count(word)
		percentage = '{:.2%}'.format(result / total) # Percentage is up to a 2nd decimal
		product.extend([percentage + ' - ' + word])
	return sorted(product, reverse=True)


def two_words(word_list):
	# Create a new list of two words joined together but separated with space.
	# We will use built in zip() function to join words 1 by 1 together and later add them to the list as one element.
	twowordlist = []
	for x,y in zip(word_list[::1], word_list[1::1]):
		twowords = x+' '+y
		twowordlist.append(twowords)
	
	# Same as before but now the new list of 2 joined words is used instead
	uniquetwowords = set(twowordlist)
	totals = len(twowordlist)

	product = []
	for word in uniquetwowords:
		result = twowordlist.count(word)
		percentage = '{:.2%}'.format(result / totals)
		product.extend([percentage + ' - ' + word])
	return sorted(product, reverse=True)



def three_words(word_list):
	# Same as two words but now three are joined together, same principle
	threewordlist = []
	for x,y,z in zip(word_list[::1], word_list[1::1], word_list[2::1]):
		threewords = x+' '+y+' '+z
		threewordlist.append(threewords)

	uniquethreewords = set(threewordlist)
	total = len(threewordlist)

	product = []
	for word in uniquethreewords:
		result = threewordlist.count(word)
		percentage = '{:.2%}'.format(result / total)
		product.extend([percentage + ' - ' + word])
	return sorted(product, reverse=True)


# The main function
# Words to ignore it's a list of strings
def keydensity(text, num_words = 1):
	word_list = get_words_list(text, words_to_ignore)
	
	result = []
	if num_words == 1:
		result = one_word(word_list)
	elif num_words == 2:
		result = two_words(word_list)
	elif num_words == 3:
		result = three_words(word_list)
	else:
		print("Wrong num words, it has to be 1, 2 or 3 and it's " + num_words)

	return result

