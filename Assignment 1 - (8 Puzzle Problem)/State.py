class State:
	def __init__(self, stateArray, h, g, p):
		self.state = stateArray
		self.h = h
		self.g = g
		self.parent = p

	def printState(self):
		row = len(self.state)
		col = len(self.state[0])
		for i in range(row):
			for j in range(col):
				x = self.state[i][j]
				if x == 0:
					print(" ", end=' ');
				else:
					print(x, end=' ');
			print()

	# find a value in state
	# returns x, y cordinate
	def find(self, x):
		row = len(self.state)
		col = len(self.state[0])
		for i in range(row):
			for j in range(col):
				if(x == self.state[i][j]):
					return i,j
		return None

	# return a copy of current state
	def copy(self):
		row = len(self.state)
		col = len(self.state[0])
		newCopy = []
		for i in range(row):
			temp = []
			for j in range(col):
				temp.append(self.state[i][j])
			newCopy.append(temp)
		return State(newCopy, self.h, self.g, self)

	# calculate combined manhattan heuristic of all blocks in current state
	def calcH_Man(self, goal):
		row = len(goal.state)
		col = len(goal.state[0])
		self.h = 0
		for i in range(row):
			for j in range(col):
				x,y = self.find(goal.state[i][j])
				self.h += abs(x-i) + abs(y-j)
		return self.h

	def calcH_Displacement(self, goal):
		row = len(goal.state)
		col = len(goal.state[0])
		self.h = 0
		for i in range(row):
			for j in range(col):
				if goal.state[i][j] != 0:
					x,y = self.find(goal.state[i][j])
					if(x != i and y != j):
						self.h += 1


	# returns a list of new states
	def getChildren(self, goal, heuristic):
		x,y = self.find(0)	# get empty block's cordinate
		directions = [[x-1,y], [x+1,y], [x,y-1], [x,y+1]]
		children = []
		for cordinates in directions:
			child = self.swap(x, y, cordinates[0], cordinates[1])
			if child is not None:
				child.g += 1
				if heuristic == "man":
					child.calcH_Man(goal)
				if heuristic == "disp":
					child.calcH_Displacement(goal)
				children.append(child)
		return children

	# swap empty block (x,y) with (i,j)
	def swap(self, x,y, i,j):
		if i >= 0 and i < len(self.state) and j >= 0 and j < len(self.state[0]):
			newState = self.copy()
			temp = newState.state[i][j]
			newState.state[i][j] = newState.state[x][y]
			newState.state[x][y] = temp
			return newState
		else:
			return None

	def isEqual(self, neighbor):
		if neighbor is not None:
			row = len(self.state)
			col = len(self.state[0])
			for i in range(row):
				for j in range(col):
					if(self.state[i][j] != neighbor.state[i][j]):
						return False;
			return True
		else:
			return False