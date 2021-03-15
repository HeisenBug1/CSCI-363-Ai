import time
from State import *

class DFBB:
	def __init__(self, goal, current, l, idaStar, limit):
		self.goal = State(goal, 0, 0, None)
		self.curState = State(current, 0, 0, None)
		self.curState.calcH_Man(self.goal)
		self.open = []
		self.closed = []
		self.limit = limit
		self.open.append(self.curState)
		if idaStar is True:
			self.L = self.curState.costF()
		else:
			self.L = l
		self.ida = idaStar

	def printState(self):
		self.curState.printState()

	def solve(self):
		timer = time.time()
		L = self.L
		count = 0
		gCost = -1
		minL = 99999
		maxL = 0
		while(len(self.open) > 0):
			if count == self.limit: # limit
				if self.ida is False:
					return ((time.time() - timer), L, self.L, count, gCost, self.closed)
				else:
					return ((time.time() - timer), minL, maxL, count, gCost, self.closed)
			count += 1
			curState = self.open.pop(0)
			if curState.isEqual(self.goal):
				if self.ida is False:
					L = min(curState.costF(), L)
				gCost = curState.g
				while curState is not None:
					self.closed.append(curState)
					curState = curState.parent
				self.closed = self.closed[::-1]
				if self.ida is False:
					return ((time.time() - timer), L, self.L, count, gCost, self.closed)
				else:
					return ((time.time() - timer), minL, maxL, count, gCost, self.closed)
			else:
				childList = []
				tempL = 9999999999
				tempChild = None
				# print("Parent: "+str(curState.costF()))
				for child in curState.getChildren(self.goal, "man"):
					# print("Child: "+str(child.costF()))
					if tempL > child.costF():
						tempL = child.costF()
						tempChild = child
					if child.costF() <= L:
						childList.append(child)
				childList.sort(key=lambda x : x.h + x.g)
				if self.ida is True:
					if len(childList) > 0:
						L = childList[0].costF()
					else:
						# print("FailSafe")
						L = tempL
						childList.append(tempChild)
				for child in childList:
					self.open.append(child)
				if minL > L:
					minL = L
				if maxL < L:
					maxL = L
		if self.ida is False:
			return ((time.time() - timer), L, self.L, count, gCost, self.closed)
		else:
			return ((time.time() - timer), minL, maxL, count, gCost, self.closed)