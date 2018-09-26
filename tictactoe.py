import replit

def printMatrix(matrix):
	for rowNum in range(len(matrix)):
		rowString = ''
		for colNum in range(len(matrix[rowNum])):
			rowString = rowString + str(matrix[rowNum][colNum]) + '  '
		print rowString
		

def play():
	replit.clear()
	blankBoard = [['-','-','-'],['-','-','-'],['-','-','-']]
	win = False
	tie = False
	player = 1
	printMatrix(blankBoard)
	while win == False and tie == False:
		if player == 1:
			print('X turn')
			row = int(raw_input('Row 1, 2 or 3? '))
			if row > 3 or row < 1 or row == '':
				row = int(raw_input('Invalid row. Row 1, 2 or 3? '))
			column = int(raw_input('Column 1, 2 or 3? '))
			if column > 3 or column < 1 or column == '':
				column = int(raw_input('Invalid column. Column 1, 2 or 3? '))
			if blankBoard[(row-1)][(column-1)] == '-':
				blankBoard[(row-1)][(column-1)] = 'X'
				player = 2
			elif blankBoard[(row-1)][(column-1)] != '-':
				print('Spot already taken')
				player = 1
			replit.clear()
			printMatrix(blankBoard)
			win = checkWin(blankBoard)
			tie = checkTie(blankBoard)
		else:
			print('O turn')
			row = int(raw_input('Row 1, 2 or 3? '))
			if row > 3 or row < 1 or row == '':
				row = int(raw_input('Invalid row. Row 1, 2 or 3? '))
			column = int(raw_input('Column 1, 2 or 3? '))
			if column > 3 or column < 1 or column == '':
				column = int(raw_input('Invalid column. Column 1, 2 or 3? '))
			if blankBoard[(row-1)][(column-1)] == '-':
				blankBoard[(row-1)][(column-1)] = 'O'
				player = 1
			elif blankBoard[(row-1)][(column-1)] != '-':
				print('Spot already taken')
				player = 2
			replit.clear()
			printMatrix(blankBoard)
			win = checkWin(blankBoard)
	if win == True:
		print blankBoard[(row-1)][(column-1)] + ' wins!'
	elif tie == True:
		print('Tie game')

def checkWin(blankBoard):
	diagonal = 0
	win = False
	for item in blankBoard:
		if item[0] == item[1] and item[1] == item[2] and item[1] != '-':
			win = True
	for i in range(0,3):
		if blankBoard[0][i]==blankBoard[1][i] and blankBoard[1][i] == blankBoard[2][i] and blankBoard[1][i] != '-':
			win = True
	if blankBoard[diagonal][diagonal+2]==blankBoard[diagonal+1][diagonal+1] and blankBoard[diagonal+1][diagonal+1]== blankBoard[diagonal+2][diagonal] and blankBoard[diagonal+1][diagonal+1] != '-':
		win = True
	if blankBoard[diagonal][diagonal]==blankBoard[diagonal+1][diagonal+1] and blankBoard[diagonal+1][diagonal+1]== blankBoard[diagonal+2][diagonal+2] and blankBoard[diagonal+1][diagonal+1] != '-':
		win = True
	return win

def checkTie(blankBoard):
	tieCount = 0
	for item in blankBoard:
		for space in item:
			if space == '-':
				tieCount += 1
	if tieCount == 0:
		return True
	else:
		return False
	


#Copyright Teddy Lambert 2017
