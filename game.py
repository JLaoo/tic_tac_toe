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
	pos_dict = {0:"_", 1:"_",2:"_", 3:"_",4:"_", 5:"_",6:" ", 7:" ",8:" "}
	board = initial_board
	positions = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
	def __init__(self):
		print(starting_board)
		self.who = 0

	def play_turn(self):
		player = self.who + 1
		valid_choice = False
		while not valid_choice:
			print(f"Player {player}, please enter a board position or type exit to leave")
			player_choice = int(input())
			if player_choice >= 0 and player_choice <= 8 and self.positions[player_choice] == -1:
				valid_choice = True
			else:
				print("Please enter a valid board position")
		self.update(player_choice, self.who, self.pos_dict)
		self.who = abs(self.who - 1)


	def win_condition(self):
		if not -1 in self.positions:
			return 3
		for board in winning_boards:
			if self.positions[board[0]] == self.positions[board[1]] == self.positions[board[2]] and self.positions[board[0]] != -1:
				return self.who
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
		win = self.win_condition()
		while win == -1:
			self.play_turn()
			win = self.win_condition()
		if win == 1 or win == 2:
			print(f"Congratulations Player {win}, you've won!")
		else:
			print("The game ends in a draw!")
