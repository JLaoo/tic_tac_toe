from game import *
while True:
	ttt = Game()
	print("""
Choose an option:
1 - Human vs Human
2 - Easy AI
3 - Medium AI
4 - Hard AI
5 - Exit
"""
	)
	choice = input()
	try:
		choice = int(choice)
	except ValueError:
		print("Please enter a number")
	else:
		if choice < 1 or choice > 5:
			print("Please enter a valid option")
		elif choice == 1:
			ttt.play_game()
		if choice == 2:
			ttt.play_vs_AI(1)
		elif choice == 3:
			print("Still in development...")
		elif choice == 4:
			print("Still in development...")
		elif choice == 5:
			break