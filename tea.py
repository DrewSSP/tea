from random import randint
import argparse
import os

# an array tree to hold the names of teas available. The first tree splits into True/False, which respectively represent Caffeinated/Non-caffeinated. The arrays with tea names are the lists of teas that go with the caffeinate/non-caffeinated labels
teas = [
	# caffeinated teas
	['Organic Lapsang Souchong Star (Medium)',
	'Organic Silk Dragon Jasmine (Medium)',
	'Blood Orange Pu\'erh (Medium)',
	'Organic La La Lemon (Medium)',
	'Santa\'s Secret (Medium)',
	'Glitter & Gold (Medium)',
	'Coffee Pu\'erh (Medium)',
	'Maharaja Chai Oolong and Samurai Chai Mate Mix (Medium)',
	'Tetley Mint Green Tea ',
	'Citron Oolong (Low)',
	'Organic Buttered Rum (Low)',
	'Tetley Chai (Don\'t know)'], 
	# non-caffeinated teas
	['Bravissimo (None)',
	'Chrysanthemum (None)',
	'Organic Rooibos (None)',
	'Organic Cinnamon Rooibos Chai (None)',
	'Goji Pop (None)',
	'Organic Cold 911 (None)',
	'Pink Lemonade (None)',
	'Mamma Mia (None)',
	'Organic Super Ginger (None)',
	'Forever Nuts (None)',
	'Tetley Revive (None)',
	'Tetley Warmth (None)',
	'Tetley Mojito (None)',
	'Tetley Dream (None)',
	'Tetley Cleanse (None)',
	'Ginger Lemon (None)']]

# store flags inputted from terminal to allow the user to specify if he/she wants the selector to choose caffeinated, non-caffeinated, or both types of teas.
parser = argparse.ArgumentParser(description='From the teas in the list defined in tea.py, produces a random tea for you to make.')
parser.add_argument('-c', '--caf', '--caffeinated', action='store_true', help="Only output teas that might have enough caffeine to keep you awake")
parser.add_argument("-d", "--decaf", '--decaffeinated', action='store_true', help="Only output teas that DON'T have enough caffeine to keep you awake")
parser.add_argument("-t", "--teas", action='store_true', help="Shows the source code for the aplication so that you may change the available teas")
args = parser.parse_args()

# If user inputs both decaf and caf teas or does not specify, return either caffeinated or non-caffeinated teas
if args.teas==True:
	os.system('vim ' + os.path.realpath(__file__)) # I know editing a program with itself is bad practice but I'll fix it later when I put the tea array in seperate files
elif args.caf==True and args.decaf==True or args.caf==False and args.decaf==False:
	# Chooses whether a tea is caffeinad. Non-caf is 1, cafeinated is 0.
	caf_nocaf = randint(0, 1)
	# Chooses one of the teas from the caf/nocaf list that was chosen by caf_nocaf
	tea_index = randint(0, len(teas[caf_nocaf])-1)
	print teas[caf_nocaf][tea_index]
elif args.caf==True:
	# Chooses an index for one of the teas from the caf list
	tea_index = randint(0, len(teas[0])-1)
	print teas[0][tea_index]
else:
	# Chooses an index for one of the teas from the nocaf list
	tea_index = randint(0, len(teas[1])-1)
	print teas[1][tea_index]
