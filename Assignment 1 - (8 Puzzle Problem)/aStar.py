import time
from State import *

class aStar:
	def __init__(self, goal, current, heuristic):
		self.goalState = State(goal, 0, 0, None)
		self.currentState = State(current, 0, 0, None)
		self.heuristic = heuristic
		if self.heuristic == "man":
			self.currentState.calcH_Man(self.goalState)
		if self.heuristic == "disp":
			self.currentState.calcH_Displacement(self.goalState)
		# if self.heuristic is "man":
		# if self.heuristic is "man":
		self.open = []
		self.closed = []
		self.open.append(self.currentState)

	def printState(self):
		self.currentState.printState()

	def checkNeighbors(self, curState, childState):
		for neighbor in self.open:
			if childState.isEqual(neighbor) is True:
				cf = childState.g + childState.h
				nf = neighbor.g + neighbor.h
				if cf <= nf:	# this allows worst case to solve
					# remove duplicates
					self.open.remove(neighbor)
		self.open.append(childState)

	def solve(self):
		timer = time.time()
		count = 0
		goalReached = False
		while(goalReached is False):
			count+=1
			if count == 10000:
				return ((time.time() - timer), count, curState.g)
			curState = self.open.pop(0)
			if curState.isEqual(self.goalState) is True:
				goalReached = True
				depth = curState.g
				while curState is not None:
					self.closed.append(curState)
					curState = curState.parent
				self.closed = self.closed[::-1]
			else:
				for child in curState.getChildren(self.goalState, self.heuristic):
					self.checkNeighbors(curState, child)
				self.open.sort(key = lambda x : x.h + x.g)
		return ((time.time() - timer), count, depth)