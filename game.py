import random

initial_board = """
_{}_|_{}_|_{}_
_{}_|_{}_|_{}_
 {} | {} | {}
"""
starting_board = """
_0_|_1_|_2_
_3_|_4_|_5_
 6 | 7 | 8
"""
winning_boards = [
[0,1,2],
[3,4,5],
[6,7,8],
[0,3,6],
[1,4,7],
[2,5,8],
[0,4,8],
[2,4,6]
]
class Game:
	def __init__(self):
		self.pos_dict = {0:"_", 1:"_",2:"_", 3:"_",4:"_", 5:"_",6:" ", 7:" ",8:" "}
		self.board = initial_board
		self.positions = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
		self.who = 0

	def play_turn(self):
		player = self.who + 1
		valid_choice = False
		while not valid_choice:
			print(f"Player {player}, please enter a board position")
			try:
				player_choice = int(input())
			except ValueError:
				print("Please enter a number")
			else:
				if player_choice >= 0 and player_choice <= 8 and self.positions[player_choice] == -1:
					valid_choice = True
				else:
					print("Please enter a valid board position")
		self.update(player_choice, self.who, self.pos_dict)
		self.who = abs(self.who - 1)


	def win_condition(self):
		for board in winning_boards:
			if self.positions[board[0]] == self.positions[board[1]] == self.positions[board[2]] and self.positions[board[0]] != -1:
				return abs(self.who - 1)
		if not -1 in self.positions:
			return 3
		return -1

	def update(self, player_choice, who, pos_dict):
		if who == 0:
			pos_dict[player_choice] = "O"
		else:
			pos_dict[player_choice] = "X"
		self.board = f"""
_{pos_dict[0]}_|_{pos_dict[1]}_|_{pos_dict[2]}_       _0_|_1_|_2_
_{pos_dict[3]}_|_{pos_dict[4]}_|_{pos_dict[5]}_       _3_|_4_|_5_
 {pos_dict[6]} | {pos_dict[7]} | {pos_dict[8]}         6 | 7 | 8
"""
		print(self.board)
		self.positions[player_choice] = who

	def play_game(self):
		print(starting_board)
		win = self.win_condition()
		while win == -1:
			self.play_turn()
			win = self.win_condition()
		if win == 0 or win == 1:
			player = win + 1
			print(f"Congratulations Player {player}, you've won!")
		else:
			print("The game ends in a draw!")

	def easy_AI_turn(self):
		choice = random.randint(0, 8)
		while self.positions[choice] != -1:
			choice = random.randint(0,8)
		self.update(choice, self.who, self.pos_dict)
		self.who = abs(self.who - 1)

	def play_vs_AI(self, difficulty):
		print(starting_board)
		if difficulty == 1:
			AI = self.easy_AI_turn
		if difficulty == 2:
			AI = self.easy_AI_turn
		else:
			AI = self.easy_AI_turn
		win = self.win_condition()
		while win == -1:
			self.play_turn()
			if self.win_condition() != -1:
				win = self.win_condition()
				break
			AI()
			win = self.win_condition()
		if win == 0:
			print("Congratulations Player, you have won!")
		elif win == 1:
			print("Better luck next time :(")
		else:
			print("The game ends in a draw!")


