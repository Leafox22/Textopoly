import random

def make_dice1():
	local_dice1 = random.randint(1, 6)
	return(local_dice1)
	
def make_dice2():
	local_dice2 = random.randint(1, 6)
	return(local_dice2)


#dice1 = make_dice1()
#dice2 = make_dice2()

def show_dice():
	#dice art (Only front face from: Joan G. Stark, https://www.asciiart.eu/miscellaneous/dice)
	
	
	#first dice
	for dice in dice1, dice2:
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
