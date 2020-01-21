from objects import puzzle

def loadFile(fileToLoad):
	file = open(fileToLoad,"r")
	lines = []
	words = []
	finishedLines = False

	for line in file:

		if line in ['\n']:
			finishedLines = True
		elif (finishedLines==False):
			lines.append(line)
		else:
			words.append(line)


	global puzzle
	puzzle = puzzle(lines, words)

	return puzzle


