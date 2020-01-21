import loadFile
import traversePuzzle
import sys
from objects import wordHolders

puzzle  = loadFile.loadFile(sys.argv[1])
words = []

for line in puzzle.lines:
	print(line, end='')

for wordToFind in puzzle.words:
	word = traversePuzzle.traversePuzzle(wordToFind, puzzle)
	words.append(word)

for item in words:
	print(item.word+" "+str(item.xCoord)+" "+str(item.yCoord)+" "+item.direction)

