import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()
from nltk.stem.porter import PorterStemmer
stem = PorterStemmer()
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np



#The program will read the file that you are inputing
name = input("Please give me the name of the TEXT file that you would like to input. ")
file = open(name , "r") 
text = file.read()

print()
print("-----------------------")
print()

#grouping text in sentences, each sentence is an item on a list
tokenized_sent = sent_tokenize(text)

print("The ammount of sentences you have:", len(tokenized_sent))

print()
print("-----------------------")
print()

# gourping text in words, each word is an item on a list
tokenized_word = word_tokenize(text)
print("The ammount of words you have:", len(tokenized_word))

print()
print("-----------------------")
print()

# Frequency Distribution/ What are the most common words seen in the users document
fdist = FreqDist(tokenized_word)

#Allowing the user to choose how many of their mosy common words they want to see
def frequency(numb):
	print(fdist.most_common(numb))

print("In this code you will be able to see your most commonly used words.")
print()
commonQuestion = input("Would you like to view your most commonly used words? yes/no ")
if commonQuestion == "yes":
	print("-------------------------")
	print()
	print("Please close the following graph to continue with the code.")
	print()
	freqwords = int(input("How many of you most commonly used words would you like to see? "))

	print(frequency(freqwords))

	#Plotting all of the words that are most commonly found in the text
	fdist.plot(15, cumulative = False)

	plt.show()

print()
print("-----------------------")
print()

#Showing ALL stopwords
stop_words = set(stopwords.words("english"))

print("These are all the most common stop words in the english language:")
print(stop_words)

print()
print("-----------------------")
print()

#Filtering all stopwords out of the text'
stemmed_words=[]
filtered_sent=[]
print("Stop words in text are considerd as noise")
print()
question1 = input("Would you like to filter out all stopwords? yes/no ")
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
if question1 == "yes":
	print("Broken Up Sentence:",tokenized_sent)
	print("Filterd Sentence:",filtered_sent)

print()
print("-----------------------")
print()

#transforms root word with the use of vocabulary and morphological analysis
print("Words can be simplified to only have their base or root.")
print()
print("A root word is the primary form of a word while a base word is a word that can stand on its own.")
print()
print("The base and the root of a word can sometimes be the same.")
print()
difWordQuestion = input("Would you like to simplyfiy a word to see its root and base? yes/no ") 
if difWordQuestion == "yes":
	word = input("What word would you like to see be simplified? ")
	print()
	print("Base Word:",lem.lemmatize(word,"v"))
	print("Root Word:",stem.stem(word))

print()
print("-----------------------")
print()

#Reducing words to their word root word or chopping off the derivational affixes
question2 = input("Would you like to reduce all words in your document to their roots? yes/no ")
if question2 == "yes":
	ps = PorterStemmer()
	for w in tokenized_word:
	    stemmed_words.append(ps.stem(w))
	print("Broken Up Sentence:",tokenized_sent)
	print()
	print("Root word Sentence:",stemmed_words)

print()
print("-----------------------")
print()

#Part Of Speach tagging
nouns = 0
adjetives = 0
verbs = 0
tokens = word_tokenize(text)
POS = nltk.pos_tag(tokens)
posQuestion = input("Would you like to see how many adjectives, nouns, and verbs you have? yes/no ")
if posQuestion == "yes":
	print("Close the following graph to terminate this program")
#Finding only the part of speach tag in the list and using that to add one every time that tag comes up to the respective category
	for r in POS:
		partOfSpeach = r[1]
		if partOfSpeach == "NN" or partOfSpeach == "NNS" or partOfSpeach == "NNP" or partOfSpeach == "NNPS":
			nouns += 1
		elif partOfSpeach == "JJ" or partOfSpeach == "JJR" or partOfSpeach == "JJS":
			adjetives += 1
		elif partOfSpeach == "VB" or partOfSpeach == "VBD" or partOfSpeach == "VBN":
			verbs += 1
#Creating a graph to show the user how many of the diffrent types of parts of speach they have in their file
	x = ["Nouns", "Adjectives", "Verbs"]
	pos2 = [nouns, adjetives, verbs]
	plt.xlabel('Parts of speach')  
	plt.ylabel('Ammount of times shown')
	plt.bar(x, pos2, color='green')
	plt.show()

	print("Adjectives:", adjetives)
	print("Nouns:", nouns)
	print("Verbs:", verbs)