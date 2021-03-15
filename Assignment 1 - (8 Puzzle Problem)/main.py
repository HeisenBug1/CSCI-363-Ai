from aStar import *
from DFBB import *

goalState = [[1,2,3], [8,0,4], [7,6,5]]

easyState = [[1,3,4], [8,6,2], [7,0,5]]
mediumState = [[2,8,1], [0,4,3], [7,6,5]]
hardState = [[2,8,1], [4,6,3], [0,7,5]]
worstState = [[5,6,7], [4,0,8], [3,2,1]]

states = [easyState, mediumState, hardState, worstState]
sName = ["Easy State:", "Medium State:", "Hard State:", "Worst State"]
# values that work best with DFBnB's L value
# but not sure about worst case so 1000
DFBnB_Lval = [7, 11, 14, 1000]

limit = 5050
index = 0

for state in states:
	print("\n"+sName[index])
	print("-------------------------------")

	aD = aStar(goalState, state, "disp", limit)
	time, count, depth, path = aD.solve()
	del(aD)
	# for state in path:
	# 	state.printState()
	# 	print("-----")
	print("A* using # of dis-placed tiles")
	if depth == -1:
		print("No solution found. Reached Limit: "+str(limit))
	print("Solution Depth: " + str(depth))
	print("Total Nodes Explored: " + str(count))
	print("Time Taken: " + str(time) +"\n")

	aM = aStar(goalState, state, "man", limit)
	time, count, depth, path = aM.solve()
	del(aM)
	# for state in path:
	# 	state.printState()
	# 	print("-----")
	print("A* using Manhattan Heuristic")
	if depth == -1:
		print("No solution found. Reached Limit: "+str(limit))
	print("Solution Depth: " + str(depth))
	print("Total Nodes Explored: " + str(count))
	print("Time Taken: " + str(time) + "\n")

	idaStar = DFBB(goalState, state, 0, True, limit)
	time, L1, L2 , count, depth, path = idaStar.solve()
	del(idaStar)
	# for state in path:
	# 	state.printState()
	# 	print("-----")
	print("IDA* using Manhattan Heuristic")
	if depth == -1:
		print("No Solution using L range: " + str(L1)+" - "+str(L2))
	print("L range: " + str(L1)+" - "+str(L2))
	print("Solution Depth: " + str(depth))
	print("Total Nodes Explored: " + str(count))
	print("Time Taken: " + str(time) +"\n")

	dfbb = DFBB(goalState, state, DFBnB_Lval[index], False, limit)
	time, L1, L2 , count, depth, path = dfbb.solve()
	del(dfbb)
	# for state in path:
	# 	state.printState()
	# 	print("-----")
	print("DFBB using Manhattan Heuristic with L: " + str(L2))
	if depth == -1:
		print("No Solution using L range: " + str(L1)+" - "+str(L2))
	print("Final L: " + str(L1))
	print("Solution Depth: " + str(depth))
	print("Total Nodes Explored: " + str(count))
	print("Time Taken: " + str(time))

	index += 1
	print("-------------------------------")