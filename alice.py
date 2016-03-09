
# @bakerj

# resources used:
# http://www.nltk.org/book/
# https://blogs.princeton.edu/etc/files/2014/03/Text-Analysis-with-NLTK-Cheatsheet.pdf

# Dependencies for core functionality are nltk package and "book corpus" materials (and pip package manager if you desire)
# At command prompt, run: "pip install nltk"
# Then, inside a python shell, run "nltk.download()" and choose corpus material for book

import nltk
from nltk.corpus import gutenberg
import argparse

# set up argument parser
parser = argparse.ArgumentParser(
          description='alice.py displays specific NLP results about Alice in Wonderland.')
# add option to plot word frequency, sets argument to true if used
parser.add_argument("-p","--plot", action='store_true', required=False,
                    help="show a plot of the 4 most common words (requires matplotlib, see http://matplotlib.org/)")
args = parser.parse_args()

# Question 1
# What are the four most frequent words used in the Project Gutenberg version of Alice in Wonderland?

# using built-in project gutenberg nltk library
alice_text = nltk.Text(nltk.corpus.gutenberg.words('carroll-alice.txt'))

# strip punctuation for some cases
alice_words_only = [w for w in alice_text if w.isalpha()]

# frequency distance for top words
frequency = nltk.FreqDist(alice_words_only)

# output the 4 most common words from the frequency object, via nifty tabulate method
print "The 4 most common words in Project Gutenberg's version of Alice in Wonderland are:"
frequency.tabulate(4)

# Question 2
# How often does the word Alice appear on either side of an adjective?

# use nltk POS tagger to tag the sanitized version of the book
alice_tagged_clean = nltk.pos_tag(alice_words_only)

# set counting of adjective instances before and after Alice to zero to start
count_adj_after_alice = 0
count_adj_before_alice = 0

# search the POS tagged book for instances of Alice
# the tagged book is a list of tuples with ["word", POS]
# use enumerate function to get list index (based on http://goo.gl/1kKcNH)
for index, value in enumerate(alice_tagged_clean):
	# if the first element in the tuple is Alice
	if value[0] == "Alice":	
		# look at the second tuple element (the POS) in the list index one BEFORE Alice instance, compare to all nltk adjective tags
		if alice_tagged_clean[index - 1][1] == "JJ" or alice_tagged_clean[index - 1][1] == "JJR" or alice_tagged_clean[index - 1][1] == "JJS":
			# verbose output if needed:
			# print "Found ADJ before Alice"
			# print alice_tagged_clean[index - 1][1]
			# increment appropriate counter if true 
			count_adj_before_alice += 1
		# look at the second tuple element (the POS) in the list index one AFTER Alice instance, compare to all nltk adjective tags
		if alice_tagged_clean[index + 1][1] == "JJ" or alice_tagged_clean[index + 1][1] == "JJR" or alice_tagged_clean[index + 1][1] == "JJS":
			# verbose output if needed:
			# print "Found ADJ after Alice"
			# print alice_tagged_clean[index + 1][1]
			# increment appropriate counter if true
			count_adj_after_alice += 1

# Output results
print "Number of times an adjective comes before Alice:"
print count_adj_before_alice
print "Number of times an adjective comes after Alice:"
print count_adj_after_alice

# Output answer to Question 2:
print "Number of times the word Alice appears on either side of an adjective:"
print count_adj_before_alice + count_adj_after_alice

# Optional plotting
if args.plot:
	# gracefully check if the user has required matplotlib package installed
	try:
		import matplotlib
	except ImportError:
		raise ValueError('The plot function requires matplotlib to be installed.'
                     'See http://matplotlib.org/')
	print "Generating word frequency plot..."
	# use the frequency object's plot method to generate the plot via matplotlib
	frequency.plot(4, title="4 Most Common Words from Alice in Wonderland")
