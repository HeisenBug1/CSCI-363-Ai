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
DFBnB_Lval = [7, 11, 14, 32]

limit = 100000
index = 0

pathList = []

for state in states:
	print("\n"+sName[index])
	print("-------------------------------")

	# A* using distance
	aD = aStar(goalState, state, "disp", limit)
	time, count, depth, path = aD.solve()
	del(aD)
	print("A* using # of dis-placed tiles")
	if depth == -1:
		pathList.append(None)
		if time >= 600 and time < 601:
			print("No solution found. Time limit Reached")
		else:
			print("No solution found. Reached Limit: "+str(limit))
	else:
		pathList.append(path)
	print("Solution Depth: " + str(depth))
	print("Total Nodes Explored: " + str(count))
	print("Time Taken: " + str(time) +"\n")

	# A* using Manhattan
	aM = aStar(goalState, state, "man", limit)
	time, count, depth, path = aM.solve()
	del(aM)
	print("A* using Manhattan Heuristic")
	if depth == -1:
		pathList.append(None)
		print("No solution found. Reached Limit: "+str(limit))
	else:
		pathList.append(path)
	print("Solution Depth: " + str(depth))
	print("Total Nodes Explored: " + str(count))
	print("Time Taken: " + str(time) + "\n")

	# IDA* using Manhattan
	idaStar = DFBB(goalState, state, 0, True, limit)
	time, L1, L2 , count, depth, path = idaStar.solve()
	del(idaStar)
	print("IDA* using Manhattan Heuristic")
	if depth == -1:
		pathList.append(None)
		print("No Solution using L range: " + str(L1)+" - "+str(L2))
	else:
		pathList.append(path)
	print("L range: " + str(L1)+" - "+str(L2))
	print("Solution Depth: " + str(depth))
	print("Total Nodes Explored: " + str(count))
	print("Time Taken: " + str(time) +"\n")

	# DFBnB using Manhattan
	dfbb = DFBB(goalState, state, DFBnB_Lval[index], False, limit)
	time, L1, L2 , count, depth, path = dfbb.solve()
	del(dfbb)
	print("DFBB using Manhattan Heuristic with L: " + str(L2))
	if depth == -1:
		pathList.append(None)
		print("No Solution using L range: " + str(L1)+" - "+str(L2))
	else:
		pathList.append(path)
	print("Final L: " + str(L1))
	print("Solution Depth: " + str(depth))
	print("Total Nodes Explored: " + str(count))
	print("Time Taken: " + str(time))


	index += 1
	print("-------------------------------")


outFile = open("PathList.txt", "w")
string = ""
index = 0
for i in range(0, len(pathList), 4):
	string +=(sName[index])
	index += 1
	string +=("\n-------------------------------")
	string +=("\nA* using Distance:\n")
	if pathList[i] is not None:
		for state in pathList[i]:
			string +=(state.printState())
			string +=('\n')
	else:
		string +=("\nNo Solution\n")

	string +=("\n-------------------------------")
	string +=("\nA* using Manhattan:\n")
	if pathList[i+1] is not None:
		for state in pathList[i+1]:
			string +=(state.printState())
			string +=('\n')
	else:
		string +=("\nNo Solution\n")

	string +=("\n-------------------------------")
	string +=("\nIDA* using Manhattan:\n")
	if pathList[i+2] is not None:
		for state in pathList[i+2]:

			string +=(state.printState())
			string +=('\n')
	else:
		string +=("\nNo Solution\n")

	string +=("\n-------------------------------")
	string +=("\nDFBnB using Manhattan:\n")
	if pathList[i+3] is not None:
		for state in pathList[i+3]:
			string +=(state.printState())
			string +=('\n')
	else:
		string +=("\nNo Solution\n")
	string += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"

outFile.write(string)