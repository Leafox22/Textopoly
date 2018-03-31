import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
	
def show_dice():
	
	#dice art (Only front face from: Joan G. Stark, https://www.asciiart.eu/miscellaneous/dice)

	#first dice
	if dice1 == 1:
		print("""	 _______
	|       |
	|   o   |
	|       |
	'-------' 
	""")
	elif dice1 == 2:
		print("""	 _______
	|     o |
	|       |
	| o     |
	'-------'
	""")
	elif dice1 == 3:
		print("""
	 _______
	|     o |
	|   o   |
	| o     |
	'-------'
	""")
	elif dice1 == 4:
		print("""
	 _______
	| o   o |
	|       |
	| o   o |
	'-------'
	""")
	elif dice1 == 5:
		print("""
	 _______
	| o   o |
	|   o   |
	| o   o |
	'-------'
	""")
	elif dice1 == 6:
		print("""
	 _______
	| o   o |
	| o   o |
	| o   o |
	'-------'
	""")


	#second dice
	if dice2 == 1:
		print("""
  _______
 |       |
 |   o   |
 |       |
 '-------'
	""")
	elif dice2 == 2:
		print("""
  _______
 |     o |
 |       |
 | o     |
 '-------'
	""")
	elif dice2 == 3:
		print("""
  _______
 |     o |
 |   o   |
 | o     |
 '-------'
	""")
	elif dice2 == 4:
		print("""
  _______
 | o   o |
 |       |
 | o   o |
 '-------'
	""")
	elif dice2 == 5:
		print("""
  _______
 | o   o |
 |   o   |
 | o   o |
 '-------'
	""")
	elif dice2 == 6:
		print("""
  _______
 | o   o |
 | o   o |
 | o   o |
 '-------'
	""")



#not sure we need this! But the dice are friggin awesome
'''
def show_m1y(player):
	real_player = player - 1
	print("Player", player, "has", str(m1y_bank[real_player]), "MONOPOLY Dollars")


for i in player_list:
	show_m1y(i)
'''

