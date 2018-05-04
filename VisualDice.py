import random

def show_dice():
	#dice art (Only front face from: Joan G. Stark, https://www.asciiart.eu/miscellaneous/dice)
	
	dicestuff = []
	dice1 = random.randint(1, 6)
	dice2 = random.randint(1, 6)
	dicestuff.append(dice1)
	dicestuff.append(dice2)

	#first dice
	for dice in dicestuff:
		if dice == 1:
			print("""	
 _______
|       |
|   o   |
|       |
'-------' 
		""")
		elif dice == 2:
			print("""	
 _______
|     o |
|       |
| o     |
'-------'
		""")
		elif dice == 3:
			print("""
	 _______
	|     o |
	|   o   |
	| o     |
	'-------'
		""")
		elif dice == 4:
			print("""
	 _______
	| o   o |
	|       |
	| o   o |
	'-------'
		""")
		elif dice == 5:
			print("""
		 _______
		| o   o |
		|   o   |
		| o   o |
		'-------'
		""")
		elif dice == 6:
			print("""
		 _______
		| o   o |
		| o   o |
		| o   o |
		'-------'
		""")
	return (dicestuff)	