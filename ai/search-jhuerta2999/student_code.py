from expand import expand
from queue import PriorityQueue
from node import Node

def a_star_search (dis_map, time_map, start, end):
	path = []
	# TODO Put your code here.
	# be sure to call the imported function expand to get the next list of nodes

	#CHECKING IF END LOC EXISTS
	if start not in dis_map or end not in dis_map:
		print("Start/End Location Does Not Exist")
		print("FAILED!")

	else:
		pq = PriorityQueue()
		closed = []
		startPos = Node(start,dis_map.get(start, {}).get(start),dis_map.get(start,{}).get(end), None, 0)
		pq.put((startPos.estimatedTotal,startPos))
			
		#LOOP UNTIL WE HAVE FOUND GOAL
		foundGoal = False
		while foundGoal == False:

			if pq.empty():
				return "FAILED!"

			current = pq.get()[1]

			#MAKING SURE WE WORK WITH LOCATIONS THAT HAVE NOT BEEN VISITED YET
			if current.name not in closed:
				#IF CURRENT LOC IS THE GOAL LOC
				if current.name == end:
					while current.parent != None:
						#add parent nodes to path list
						path = [current.name] + path
						current = current.parent

					path = [startPos.name] + path
					foundGoal = True
				else:	
					#OBTAIN LIST OF SUCCESSOR NODES FROM CURRENT LOC			
					succesors = expand(current.name, time_map)
					for e in succesors:
						newNode = Node(e,time_map.get(current.name, {}).get(e),dis_map.get(e,{}).get(end), current, current.costToReach)
						pq.put((newNode.estimatedTotal, newNode))
					#ADD CURRENT LOC TO CLOSED LIST TO NEVER VISIT AGAIN
					closed.append(current.name)

	return path