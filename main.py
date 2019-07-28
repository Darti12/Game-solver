#TODO
#Add the mirrored boards to the removeequalstates function,
# and make it so that the states to be explored are immediatley checked for copies (see first recursion in debug mode)

import copy

board = [
[2,2,2,2,2,2,2,2,2],
[2,2,2,1,1,1,2,2,2],
[2,2,2,1,1,1,2,2,2],
[2,1,1,1,1,1,1,1,2],
[2,1,1,1,0,1,1,1,2],
[2,1,1,1,1,1,1,1,2],
[2,2,2,1,1,1,2,2,2],
[2,2,2,1,1,1,2,2,2],
[2,2,2,2,2,2,2,2,2]]

exploredStates = []

def getOptions(currentBoard):
	if checkWinCondition(currentBoard):
		print("WIN!")
		return True
	possibleStates = getPossibleStates(currentBoard)

	for x in possibleStates:
		getOptions(x)
	return False

def getPossibleStates(CB):
	states = []
	for x in range(0, len(CB)):
		for y in range(0, len(CB[0])):
			if CB[x][y] == 0:
				if CB[x][y-1] == 1:
					if CB[x][y-2] == 1:
						NB = copy.deepcopy(CB)
						NB[x][y] = 1
						NB[x][y-1] = 0
						NB[x][y-2] = 0
						states.append(NB)
				if CB[x][y+1] == 1:
					if CB[x][y+2] == 1:
						NB = copy.deepcopy(CB)
						NB[x][y] = 1
						NB[x][y+1] = 0
						NB[x][y+2] = 0
						states.append(NB)
				if CB[x-1][y] == 1:
					if CB[x-2][y] == 1:
						NB = copy.deepcopy(CB)
						NB[x][y] = 1
						NB[x-1][y] = 0
						NB[x-2][y] = 0
						states.append(NB)
				if CB[x+1][y] == 1:
					if CB[x+2][y] == 1:
						NB = copy.deepcopy(CB)
						NB[x][y] = 1
						NB[x+1][y] = 0
						NB[x+2][y] = 0
						states.append(NB)
	states = removeExploredStates(states)
	#print(len(states))
	return states

def removeExploredStates(states):
	states = removeEqualStates(states)
	for x in states:
		word = stringify(x)
		if word in exploredStates:
			states.remove(x)
	for x in states:
		exploredStates.extend(getEqualStates(x))
	return states

def removeEqualStates(states):
	newstates = []
	temp = []
	temp = copy.deepcopy(states)
	for x in range(0, len(temp)):
		for y in range(x+1, len(temp)):
			pass
	return states


def stringify(CB):
	word = ""
	for x in CB:
		for y in x:
			word += str(y)
	return word

def compareStates(state1, state2):
	allrotated1 = getAllRotatedBoards(state1)
	for x in allrotated1:
		if x == state2:
			return True
	return False

def getEqualStates(CB):
	states = []
	rot1 = []
	rot2 = []
	rot3 = []
	rot1 = getRotatedBoard(CB)
	rot2 = getRotatedBoard(rot1)
	rot3 = getRotatedBoard(rot2)
	states.append(stringify(CB))
	states.append(stringify(rot1))
	states.append(stringify(rot2))
	states.append(stringify(rot3))
	return states

def getRotatedBoard(CB):
	rotated = list(zip(*reversed(CB)))
	for x in range(0, len(rotated)):
		rotated[x] = list(rotated[x])
	return rotated

def getAllRotatedBoards(CB):
	allboards = []
	rot1 = getRotatedBoard(CB)
	rot2 = getRotatedBoard(rot1)
	rot3 = getRotatedBoard(rot2)
	allboards.append(rot1)
	allboards.append(rot2)
	allboards.append(rot3)
	return allboards

def prettyPrintBoard(CB):
	for x in CB:
		word = "|"
		for y in x:
			if y == 2:
				word += "   "
			if y == 1:
				word += " x "
			if y == 0:
				word += " o "
		word += "|"
		print(word)
	print()

def checkWinCondition(CB):
	amount = 0
	for x in CB:
		for y in x:
			if y == 1:
				amount += 1
	if amount == 1:
		prettyPrintBoard(CB)
		return True
	else:
		return False


if __name__ == "__main__":
	print(getOptions(board))