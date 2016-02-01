from __future__ import print_function
import random, copy
from kivy.storage.jsonstore import JsonStore

class _2048Controller:
	def __init__(self):
		self.width = 4
		self.height = 4
		self.store = JsonStore('data.json')
		self.best_score = 0
		if self.store.exists('score'):
			self.best_score = self.store.get('score')['best_score']
		self.initGame()

	def initGame(self):
		self.score = 0
		self.undo_left = 2
		self.undo_game_array = []
		self.game_array = self.generateGameArray()
		#self.game_array = [[0, 0, 8, 16], [32, 64, 128, 256], [512, 1024, 2048, 4096], [8192, 16384, 32768, 65536]]
		self.end_game = False
		self.new_number_array = []  # list of new number is generated
		self.undo_game_array = []  # ####
		for i in range(2):
			self.generateNumber()  # generate 2 new numbers

	def checkExists(self, x, y):
		return self.game_array[y][x] != 0

	def generateGameArray(self):
		game_board = []
		for y in range(self.height):
			rows = []
			for x in range(self.width):
				rows.append(0)
			game_board.append(rows)
		return game_board

	def generateNumber(self):
		while True:  # loop until the position is valid
			x = random.randint(0, self.width - 1)
			y = random.randint(0, self.height - 1)
			if not self.checkExists(x, y):
				number = 2
				if random.randint(1, 100) > 80:
					number = 4
				self.game_array[y][x] = number
				break
		self.new_number_array.append((x, y))

	def slideUp(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		moved = False
		score = 0
		animation_way = []
		for x in range(self.width):
			notCombineList = []
			for y in range(self.height):
				if game_board[y][x] == 0:
					continue
				for stop_y in range(y - 1, -1, -1):
					if game_board[stop_y][x] != 0:
						if game_board[stop_y][x] == game_board[y][x] and stop_y not in notCombineList:
								game_board[stop_y][x] *= 2
								game_board[y][x] = 0
								moved = True
								score += game_board[stop_y][x]
								notCombineList.append(stop_y)
								animation_way.append([(x, y), (x, stop_y)])
						else:
							game_board[stop_y + 1][x], game_board[y][x] = game_board[y][x], game_board[stop_y + 1][x]
							if y != stop_y + 1:
								animation_way.append([(x, y), (x, stop_y + 1)])
								moved = True
						break
					if stop_y == 0 and game_board[0][x] == 0 and game_board[y][x] != game_board[0][x]:
						game_board[0][x], game_board[y][x] = game_board[y][x], game_board[0][x]
						moved = True
						animation_way.append([(x, y), (x, stop_y)])
		return [moved, score, animation_way]

	def slideDown(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		moved = False
		score = 0
		animation_way = []
		for x in range(self.width):
			notCombineList = []
			for y in range(self.width - 1, -1, -1):
				if game_board[y][x] == 0:
					continue
				for stop_y in range(y + 1, self.height):
					if game_board[stop_y][x] != 0:
						if game_board[stop_y][x] == game_board[y][x] and stop_y not in notCombineList:
								game_board[stop_y][x] *= 2
								game_board[y][x] = 0
								moved = True
								score += game_board[stop_y][x]
								notCombineList.append(stop_y)
								animation_way.append([(x, y), (x, stop_y)])
						else:
							game_board[stop_y - 1][x], game_board[y][x] = game_board[y][x], game_board[stop_y - 1][x]
							if y != stop_y - 1:
								animation_way.append([(x, y), (x, stop_y - 1)])
								moved = True
						break
					if stop_y == (self.height - 1) and game_board[self.height - 1][x] == 0 and \
							game_board[y][x] != game_board[self.height - 1][x]:
						game_board[self.height - 1][x], game_board[y][x] = game_board[y][x], game_board[self.height - 1][x]
						moved = True
						animation_way.append([(x, y), (x, stop_y)])
		return [moved, score, animation_way]

	def slideLeft(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		moved = False
		score = 0
		animation_way = []
		for y in range(self.height):
			notCombineList = []
			for x in range(1, self.width):
				if game_board[y][x] == 0:
					continue
				for stop_x in range(x - 1, -1, -1):
					if game_board[y][stop_x] != 0:
						if game_board[y][stop_x] == game_board[y][x] and stop_x not in notCombineList:
							game_board[y][stop_x] *= 2
							game_board[y][x] = 0
							moved = True
							score += game_board[y][stop_x]
							notCombineList.append(stop_x)
							animation_way.append([(x, y), (stop_x, y)])
						else:
							game_board[y][stop_x + 1], game_board[y][x] = game_board[y][x], game_board[y][stop_x + 1]
							if x != stop_x + 1:
								animation_way.append([(x, y), (stop_x + 1, y)])
								moved = True
						break
					if stop_x == 0 and game_board[y][0] == 0 and game_board[y][x] != game_board[y][0]:
						game_board[y][0], game_board[y][x] = game_board[y][x], game_board[y][0]
						moved = True
						animation_way.append([(x, y), (stop_x, y)])
		return [moved, score, animation_way]

	def slideRight(self, game_board=None):
		if not game_board:
			game_board = self.game_array
		moved = False
		score = 0
		animation_way = []
		for y in range(self.height):
			notCombineList = []
			for x in range(self.width - 2, -1, -1):
				if game_board[y][x] == 0:
					continue
				for stop_x in range(x + 1, self.width):
					if game_board[y][stop_x] != 0:
						if game_board[y][stop_x] == game_board[y][x] and stop_x not in notCombineList:
							game_board[y][stop_x] *= 2
							game_board[y][x] = 0
							moved = True
							score += game_board[y][stop_x]
							notCombineList.append(stop_x)
							animation_way.append([(x, y), (stop_x, y)])
						else:
							game_board[y][stop_x - 1], game_board[y][x] = game_board[y][x], game_board[y][stop_x - 1]
							if x != stop_x - 1:
								animation_way.append([(x, y), (stop_x - 1, y)])
								moved = True
						break
					if stop_x == (self.width - 1) and game_board[y][self.width - 1] == 0 and\
							game_board[y][x] != game_board[y][self.width - 1]:
						game_board[y][self.width - 1], game_board[y][x] = game_board[y][x], game_board[y][self.width - 1]
						moved = True
						animation_way.append([(x, y), (stop_x, y)])
		return [moved, score, animation_way]

	def checkForWin(self):
		for y in range(len(self.game_array)):
			for x in range(len(self.game_array[0])):
				if self.game_array[y][x] == 2048:
					return True
				else:
					return False

	def checkForBestScore(self):
		if self.score > self.best_score:
			self.best_score = self.score

	def saveData(self):
		self.store.put('score', best_score=self.best_score)

	def up(self):
		tmp_game_array = copy.deepcopy(self.game_array)
		tmp_score = self.score
		moved, score, animation_way = self.slideUp()
		self.score += score
		self.checkForBestScore()
		if not self.existsMove() and self.undo_left == 0:
			self.end_game = True
		elif moved:
			self.undo_game_array.append([tmp_game_array, tmp_score])
			self.generateNumber()
		return animation_way

	def down(self):
		tmp_game_array = copy.deepcopy(self.game_array)
		tmp_score = self.score
		moved, score, animation_way = self.slideDown()
		self.score += score
		self.checkForBestScore()
		if not self.existsMove() and self.undo_left == 0:
			self.end_game = True
		elif moved:
			self.undo_game_array.append([tmp_game_array, tmp_score])
			self.generateNumber()
		return animation_way

	def left(self):
		tmp_game_array = copy.deepcopy(self.game_array)
		tmp_score = self.score
		moved, score, animation_way = self.slideLeft()
		self.score += score
		self.checkForBestScore()
		if not self.existsMove() and self.undo_left == 0:
			self.end_game = True
		elif moved:
			self.undo_game_array.append([tmp_game_array, tmp_score])
			self.generateNumber()
		return animation_way

	def right(self):
		tmp_game_array = copy.deepcopy(self.game_array)
		tmp_score = self.score
		moved, score, animation_way = self.slideRight()
		self.score += score
		self.checkForBestScore()
		if not self.existsMove() and self.undo_left == 0:
			self.end_game = True
		elif moved:
			self.undo_game_array.append([tmp_game_array, tmp_score])
			self.generateNumber()
		return animation_way

	def existsMove(self):
		exists = False
		#if self.slideUp(game_array_clone)[0] or self.slideDown(game_array_clone)[0] or \
		#	self.slideLeft(game_array_clone)[0] or self.slideRight(game_array_clone)[0]:
		#	exists = True
		for test in (self.slideLeft, self.slideRight, self.slideUp, self.slideDown):
			game_array_clone = copy.deepcopy(self.game_array)  # clone the game array to check
			if test(game_array_clone)[0]:
				exists = True
		return exists

	def undo(self):
		if self.undo_left == 0 or len(self.undo_game_array) == 0:  # if start game or out of undo left, not do undo
			return
		self.undo_left -= 1
		temp_array, temp_score = self.undo_game_array.pop()  # pop the undo data (array and score)
		for y in range(len(temp_array)):         # dont do this : self.game_array = temp.array
			for x in range(len(temp_array[0])):  # because it reference to new list, not a current list, it wont work
				self.game_array[y][x] = temp_array[y][x]
		self.score = temp_score
