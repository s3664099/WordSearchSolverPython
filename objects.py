class puzzle:
	def __init__(self,lines, words):
		self.lines = lines
		self.words = words

class wordHolders:
	def __init__(self, wordToFind):
		self.word = wordToFind
		self.xCoord = -1
		self.yCoord = -1
		self.direction = ""