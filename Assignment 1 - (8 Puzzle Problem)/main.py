from aStar import *

goalState = [[1,2,3], [8,0,4], [7,6,5]]

easyState = [[1,3,4], [8,6,2], [7,0,5]]
mediumState = [[2,8,1], [0,4,3], [7,6,5]]
hardState = [[2,8,1], [4,6,3], [0,7,5]]
impossibleState = [[5,6,7], [4,0,8], [3,2,1]]

test = [[1,2,3], [8,7,6], [0,4,5]]

aS = aStar(goalState, impossibleState, "disp")
time, count, depth = aS.solve()
for state in aS.closed:
	state.printState()
	print("-----")
print("A* using Mahattan Heuristic")
print("Total Depth: " + str(depth))
print("Total Nodes Explored: " + str(count))
print("Time Taken: " + str(time))