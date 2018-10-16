def show_dice(roll1, roll2):
	#dice art (Only front face from: Joan G. Stark, https://www.asciiart.eu/miscellaneous/dice)
	dicestuff = roll1, roll2
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
