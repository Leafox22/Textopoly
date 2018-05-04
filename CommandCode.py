import random
from PropertyLibrary import *
from VisualDice import dice1, dice2, make_dice1, make_dice2, show_dice

playerpos = 0
playermoney = 1500
playerchar = "∆"
ownedprops = []
move = 0

flag = True
hasrolled = False
injail = False
rollcount = 0
doublecount = 0


def propertycard(p):
	print("--------------------------------*")
	print(boardpos[p][name])
	print("- " + boardpos[p][colour].title() + " -")
	print("Price: $" + boardpos[p][price])
	print("Rent with no buildings: $" + boardpos[p][rent])
	print("    \"     one house: $" + boardpos[p][onehouse])
	print("    \"     two houses: $" + boardpos[p][twohouse])
	print("    \"     three houses: $" + boardpos[p][threehouse])
	print("    \"     four houses: $" + boardpos[p][fourhouse])
	print("    \"     hotel: $" + boardpos[p][hotel])
	print("")
	print("Price of single building: $" + boardpos[p][buildprice])

def railcard(i):
	print("")
	print(boardpos[i][name])
	print("- railroad -")
	print("Price: $200")
	print("Rent with one railway: $25")
	print("    \"     two railways: $50")
	print("    \"     three railways: $100")
	print("    \"     four railways: $200")
	print("")

def utilitycard(i):
	print("--------------------------------*")
	print(boardpos[i][name])
	print("- utility -")
	print("If ONE Utility is owned, rent is 4x amount shown on dice.")
	print("If BOTH Utilities are owned, rent is 10x the amount shown on the dice.")
	print("")

command = input("What would you like to do? ").lower()

while flag == True:

	#giving the player's info
	infocheck = command.split()

	#Making sure that you don't end turn before rolling the dice.
	if ((command == "end turn") or (command == "end")) & (hasrolled == False):
		print("You can't end your turn now, you have to roll!")
		print()

	#Ending the loop
	elif (command == "end") or (command == "end turn"):
			break

	#Bringing up the command list
	elif command == "?":
		print()
		print("end - ends your turn")
		print("roll - rolls the dice and moves your token.")
		print("info/i player - shows your player info (money, properties etc.)")
		print("info/i property - shows the info for a property you specify")
		print("info/i tile - shows the info for the tile you are currently on")
		print("buy - attempt to buy the property your piece is currently on.")
		#print("buy house - attempt to buy a house on a property you own")
		print()

	#Rolling the dice
	elif (command == "roll") & (hasrolled == False):
		#make new dice
#		dice1 = make_dice1()
#		dice2 = make_dice2()
		show_dice()
		rollturn = dice1 + dice2
		if playerpos + rollturn >= 40:
			playerpos = rollturn - (40 - playerpos)
			print("You passed Go! $200 added to your account.")
			playermoney += 200
		else:
			playerpos += rollturn
		print("You have moved", rollturn ,"spaces! You're now on", boardpos[playerpos][name] + ".")
		print()
		hasrolled = True
		if dice1 == dice2: # <-- allowing for rolling again
			print("DOUBLE, you can roll again when you're ready!")
			print()
			hasrolled = False
			doublecount += 1
			if doublecount == 3:
				playerpos = 10
				print("You rolled three doubles! That's speeding, you're in jail!")
				injail = True
				hasrolled = True

	#Telling that they can't roll again.
	elif (command == "roll") & (hasrolled == True):
		print("You've already rolled, you can't roll again.")
		print()

	#Basic info command
	elif (infocheck[0] == "info") or (infocheck[0] == "i"):
		if len(infocheck) == 1:
			print("Invalid input, try 'info player', 'info property', or 'info tile'")
			print()

		#gives current player stats
		elif infocheck [1] == "player":
			print("Character:", playerchar)
			print("Money: $" + str(playermoney))

			for o in ownedprops:
				print("Properties:", o[name], end=" ")
			print("")
			print("")

		#gives information on specified property
		elif command.split()[1] == "property":
			propsearch = input("What property are you wanting to know about? ")
			for i in range(0, len(boardpos)):
				if propsearch.lower() == boardpos[i][name].lower():
					if boardpos[i][colour] == "railway":
						propertycard(i)
						if boardpos[i][owner] == "":
							print("< unowned >")
							print("--------------------------------*")
						else:
							print("< Owned by", boardpos[i][owner], ">")
							print("--------------------------------*")
					elif len(boardpos[i]) == 11:
						propertycard(i)
						if boardpos[i][owner] == "":
							print("< unowned >")
							print("--------------------------------*")
						else:
							print("< Owned by", boardpos[i][owner],">")
							print("--------------------------------*")
					elif boardpos[i][colour] == "utility":
						utilitycard(i)
						if boardpos[i][3] == "":
							print("< unowned >")
							print("--------------------------------*")
						else:
							print("Owned by", boardpos[i][3])
							print("")

		#getting info for tile
		elif command.split()[1] == "tile":				
			if (len(boardpos[playerpos]) == 11) and (boardpos[playerpos][colour] != "railway"):
				propertycard(playerpos)
				if boardpos[playerpos][owner] == "":
					print("< unowned >")
					print("--------------------------------*")
				else:
					print("< Owned by", boardpos[playerpos][owner], ">")
					print("--------------------------------*")
			elif (len(boardpos[playerpos]) == 11) and (boardpos[playerpos][colour] == "railway"):
				railcard()
				if boardpos[playerpos][owner] == "":
					print("< unowned >")
					print("--------------------------------*")
				else:
					print("< Owned by", boardpos[playerpos][owner], ">")
					print("--------------------------------*")
			elif boardpos[playerpos][name] == "Go":
				print("This is Go. It's the first tile of the board, and every time you pass it you get $200 salary! Yeet!")
				print("")
			elif boardpos[playerpos][name] == "Community Chest":
				print("This is a Community Chest. It can have any number of wonderful things in it, and it's likely to be cash! No guarantees though.")
				print("")
			elif boardpos[playerpos][name] == "Chance":
				print("This is a Chance card. It's much more varied in its effects than a Community Chest, and you won't always like what you get. High risk, high reward!")
				print("")
			elif boardpos[playerpos][name] == "Income Tax":
				print("Uh oh. This is the Income Tax tile, and it means you'll have to pay $200 to the bank! Such is the cost of being so darn rich!")
				print("")
			elif boardpos[playerpos][name] == "Super Tax":
				print("Uh oh. This is the Super Tax tile, and it means you'll have to pay $100 to the bank! It's what you get for working towards a stable retirement!")
				print("")
			elif boardpos[playerpos][colour] == "utility":
					utilitycard(playerpos)
					if boardpos[playerpos][owner] == "":
						print("< unowned >")
						print("--------------------------------*")
					else:
						print("< Owned by", boardpos[playerpos][owner], ">")
						print("--------------------------------*")

		else:
			print("Invalid input, try 'info player', 'info property', or 'info tile'")
			print()

	#buying the property that they are on
	elif command == "buy":
		if len(boardpos[playerpos]) == 1:
			print("You can't buy", boardpos[playerpos][name] + "!")
			print("")
		elif boardpos[playerpos][owner]!= "":
			print("This property is already owned!")
			print()
		elif playermoney >= int(boardpos[playerpos][price]):
			#confirmation before buying
			buyconfirm = input(
			"Are you sure you want to buy this property? It will cost $"
			+ str(boardpos[playerpos][price]) + " (You have $" + str(playermoney) + ") ")
			if (buyconfirm.lower() == "yes") or (buyconfirm.lower() == "buy"):
				playermoney = playermoney - int(boardpos[playerpos][price])
				boardpos[playerpos][owner] = playerchar
				print("You now own", boardpos[playerpos][name] + "!")
				ownedprops.append(boardpos[playerpos])
				print("You have $" + str(playermoney), "left in your account.")
				print()
			elif buyconfirm.lower() == "no":
				print("")
				pass
			else:
				print("Invalid input. Yes/No only!")
		else:
			print("You do not have enough money for that.")
			print()

	#error statement for invalid commands
	else:
		print ("Not a valid command. (enter ? for command list)")
		print()

	command = input("What would you like to do? ").lower()
