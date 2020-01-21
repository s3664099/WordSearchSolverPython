from objects import wordHolders

def traversePuzzle(wordToFind, puzzle):
	global word
	result = -1
	direction = "Across"
	stringIteration = 0
	word = wordHolders(wordToFind)
	numberOfLines = len(puzzle.lines)
	stringToSearch = ""

	while result == -1:
		
		while result == -1 and stringIteration < numberOfLines:
			if direction == "Across":
				stringToSearch = puzzle.lines[stringIteration]
			elif direction == "Down":
				for line in puzzle.lines:
					stringToSearch += line[stringIteration]

			result = findMatch(wordToFind,stringToSearch)

			if result != -1:

				if direction == "Down":
					word.xCoord = stringIteration+1
					word.yCoord = result+1
					word.direction = direction
				else:
					word.xCoord = result+1
					word.yCoord = stringIteration+1
					word.direction = direction

				return word

			stringIteration+=1
			stringToSearch = ""

		if direction == "Across":

			stringIteration = 0
			numberOfLines = len(puzzle.lines[0])
			direction = "Down"

		elif direction == "Down":

			direction = "Diagonal Right"
			word = diagonalSearch(wordToFind, puzzle, False, direction)

			if word.xCoord != -1:
				return word

		elif direction == "Diagonal Right":

			direction = "Diagonal Left"
			word = diagonalSearch(wordToFind, puzzle, True, direction)

			if word.xCoord != -1:
				return word

		else:

			result = 0

	return word

def diagonalSearch(wordToFind, puzzle, leftRight, direction):

	diagonalRow = 0
	diagonalColumn = 0
	lineLength = len(puzzle.lines[0])
	wordLength = len(wordToFind)-1
	finishedSearch = False
	numberOfLines = len(puzzle.lines)

	if leftRight == True:
		diagonalRow = numberOfLines-1

	while finishedSearch == False:

		i = diagonalRow
		j = diagonalColumn
		stringToCheck = ""
		reachedEnd = False
		tooSmall = False

		if leftRight == True:

			if diagonalRow+wordLength>numberOfLines:

				tooSmall = True

			elif diagonalColumn + wordLength>lineLength+1:
				tooSmall = True

		else:

			if diagonalRow+wordLength>numberOfLines or diagonalColumn+wordLength>lineLength+1:
				tooSmall = True

			elif diagonalColumn - wordLength <-1:
				tooSmall = True

		if tooSmall == False:
			while reachedEnd == False:

				print("I: "+str(i)+" J: "+str(j)+" direction: "+str(leftRight))
				stringToCheck += puzzle.lines[i][j]
				print(stringToCheck)


				if leftRight == True:
					i+=1

					if j>-1:
						j+=1

					if j==lineLength:
						j=lineLength-1

					if i>=numberOfLines or j>lineLength:
						reachedEnd = True

				else:
					i+=1

					if j>0:
						j-=1

					if i>=numberOfLines or j<0:
						reachedEnd = True

			wordLocation = findMatch(wordToFind,stringToCheck)

			if wordLocation != -1:

				if leftRight == False:
					word.xCoord = diagonalColumn+wordLocation+1
					word.yCoord = diagonalRow+wordLocation+1
					word.direction = direction
				else:
					word.xCoord = diagonalColumn+wordLocation+1
					word.yCoord = diagonalRow+wordLocation+1
					word.direction = direction	
			
				return word

		if leftRight == True:

			diagonalColumn+=1

			if diagonalRow>0:
				diagonalRow-=1
				diagonalColumn = 0

		else:
			diagonalColumn+=1

			if diagonalColumn >=lineLength:
				diagonalColumn = lineLength-1
				diagonalRow+=1
			else:
				diagonalrow = 0

		i = diagonalRow
		j = diagonalColumn
		reachedEnd = False

		if leftRight == False and diagonalColumn == lineLength-1 and diagonalRow == numberOfLines:
			finishedSearch = True
		elif leftRight == True and diagonalColumn == lineLength-1 and diagonalRow == 0:
			finishedSearch = True

	return word

def findMatch(pattern, sentance):
	sentanceLength = len(sentance)
	patternLength = len(pattern)-1

	for i in range(0,sentanceLength-patternLength+1):

		j=0

		while j<patternLength and sentance[i+j]==pattern[j]:

			j=j+1

			if j==patternLength:

				return i

	return -1