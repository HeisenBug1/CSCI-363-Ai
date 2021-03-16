import time
from State import *

class aStar:
	def __init__(self, goal, current, heuristic, limit):
		self.goalState = State(goal, 0, 0, None)
		self.currentState = State(current, 0, 0, None)
		self.heuristic = heuristic
		if self.heuristic == "man":
			self.currentState.calcH_Man(self.goalState)
		if self.heuristic == "disp":
			self.currentState.calcH_Displacement(self.goalState)
		self.open = []
		self.closed = []
		self.open.append(self.currentState)
		self.limit = limit

	def printState(self):
		self.currentState.printState()

	def checkNeighbors(self, curState, childState):
		for neighbor in self.open:
			if childState.isEqual(neighbor) is True:
				cf = childState.costF()
				nf = neighbor.costF()
				if cf <= nf:	# this allows worst case to solve using Manhattan
					# remove duplicates
					self.open.remove(neighbor)
		self.open.append(childState)

	def solve(self):
		timer = time.time()
		count = 0
		goalReached = False
		gCost = -1
		while(goalReached is False):
			if (time.time() - timer >= 600):	# time limit 10 min
				return ((time.time() - timer), count, gCost, self.closed)
			if count == self.limit:	# limit
				return ((time.time() - timer), count, gCost, self.closed)
			count+=1
			curState = self.open.pop(0)
			if curState.isEqual(self.goalState) is True:
				goalReached = True
				gCost = curState.g
				while curState is not None:
					self.closed.append(curState)
					curState = curState.parent
				self.closed = self.closed[::-1]
				return ((time.time() - timer), count, len(self.closed)-1, self.closed)
			else:
				for child in curState.getChildren(self.goalState, self.heuristic):
					self.checkNeighbors(curState, child)
				self.open.sort(key = lambda x : x.h + x.g)