import unittest
import student_code as sc
import expand

dis_map = {
	'Big Ben':{'Big Ben':0, 'Big Cannon Hall':2, 'College Column':6, 'Hackathon Laboratory':2, 'Library':7, 'Multicultural Center':6, 'Stagger Hall':5},
	'Big Cannon Hall':{'Big Ben':2, 'Big Cannon Hall':0, 'College Column':6, 'Hackathon Laboratory':2, 'Library':5, 'Multicultural Center':6, 'Stagger Hall':5},
	'College Column':{'Big Ben':6, 'Big Cannon Hall':6, 'College Column':0, 'Hackathon Laboratory':4, 'Library':10, 'Multicultural Center':6, 'Stagger Hall':7},
	'Hackathon Laboratory':{'Big Ben':2, 'Big Cannon Hall':2, 'College Column':4, 'Hackathon Laboratory':0, 'Library':6, 'Multicultural Center':5, 'Stagger Hall':4},
	'Library':{'Big Ben':7, 'Big Cannon Hall':5, 'College Column':10, 'Hackathon Laboratory':6, 'Library':0, 'Multicultural Center':5, 'Stagger Hall':3},
	'Multicultural Center':{'Big Ben':6, 'Big Cannon Hall':6, 'College Column':6, 'Hackathon Laboratory':5, 'Library':5, 'Multicultural Center':0, 'Stagger Hall':3},
	'Stagger Hall':{'Big Ben':5, 'Big Cannon Hall':5, 'College Column':7, 'Hackathon Laboratory':4, 'Library':3, 'Multicultural Center':3, 'Stagger Hall':0}
}

time_map1 = {
	'Big Ben':{'Big Ben':None, 'Big Cannon Hall':20, 'College Column':None, 'Hackathon Laboratory':30, 'Library':None, 'Multicultural Center':None, 'Stagger Hall':None},
	'Big Cannon Hall':{'Big Ben':15, 'Big Cannon Hall':None, 'College Column':None, 'Hackathon Laboratory':None, 'Library':100, 'Multicultural Center':None, 'Stagger Hall':80},
	'College Column':{'Big Ben':None, 'Big Cannon Hall':None, 'College Column':None, 'Hackathon Laboratory':50, 'Library':None, 'Multicultural Center':100, 'Stagger Hall':100},
	'Hackathon Laboratory':{'Big Ben':30, 'Big Cannon Hall':None, 'College Column':50, 'Hackathon Laboratory':None, 'Library':None, 'Multicultural Center':None, 'Stagger Hall':30},
	'Library':{'Big Ben':None, 'Big Cannon Hall':90, 'College Column':None, 'Hackathon Laboratory':None, 'Library':None, 'Multicultural Center':None, 'Stagger Hall':20},
	'Multicultural Center':{'Big Ben':None, 'Big Cannon Hall':None, 'College Column':90, 'Hackathon Laboratory':None, 'Library':None, 'Multicultural Center':None, 'Stagger Hall':40},
	'Stagger Hall':{'Big Ben':None, 'Big Cannon Hall':80, 'College Column':90, 'Hackathon Laboratory':34, 'Library':20, 'Multicultural Center':30, 'Stagger Hall':None}
}

time_map2 = {
	'Big Ben':{'Big Ben':None, 'Big Cannon Hall':20, 'College Column':None, 'Hackathon Laboratory':40, 'Library':None, 'Multicultural Center':None, 'Stagger Hall':None},
	'Big Cannon Hall':{'Big Ben':20, 'Big Cannon Hall':None, 'College Column':None, 'Hackathon Laboratory':None, 'Library':100, 'Multicultural Center':None, 'Stagger Hall':70},
	'College Column':{'Big Ben':None, 'Big Cannon Hall':None, 'College Column':None, 'Hackathon Laboratory':60, 'Library':None, 'Multicultural Center':90, 'Stagger Hall':90},
	'Hackathon Laboratory':{'Big Ben':40, 'Big Cannon Hall':None, 'College Column':50, 'Hackathon Laboratory':None, 'Library':None, 'Multicultural Center':None, 'Stagger Hall':60},
	'Library':{'Big Ben':None, 'Big Cannon Hall':90, 'College Column':None, 'Hackathon Laboratory':None, 'Library':None, 'Multicultural Center':None, 'Stagger Hall':30},
	'Multicultural Center':{'Big Ben':None, 'Big Cannon Hall':None, 'College Column':90, 'Hackathon Laboratory':None, 'Library':None, 'Multicultural Center':None, 'Stagger Hall':30},
	'Stagger Hall':{'Big Ben':None, 'Big Cannon Hall':90, 'College Column':90, 'Hackathon Laboratory':50, 'Library':40, 'Multicultural Center':30, 'Stagger Hall':None}
}

class SearchTest(unittest.TestCase):

	def testNeighbor(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map1, 'Big Ben', 'Big Cannon Hall')
		self.assertEqual(['Big Ben', 'Big Cannon Hall'], path)
		self.assertEqual(1, expand.expand_count)

	def testDirectRoute(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map1, 'Big Ben', 'Stagger Hall')
		self.assertEqual(['Big Ben', 'Hackathon Laboratory', 'Stagger Hall'], path)
		self.assertEqual(3, expand.expand_count)

	def testExploreManyPaths(self):
		# This test explores many paths and does not assume the path to the destination is found too soon
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map1, 'Stagger Hall', 'College Column')
		self.assertEqual(['Stagger Hall', 'Hackathon Laboratory', 'College Column'], path)
		# expand all but Big Cannon and College Column
		self.assertEqual(5, expand.expand_count)

	def testDirectRouteDifferentTimes(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map2, 'Big Ben', 'Stagger Hall')
		self.assertEqual(['Big Ben', 'Big Cannon Hall', 'Stagger Hall'], path)
		self.assertEqual(3, expand.expand_count)

	def testExploreManyPathDifferentTimes(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map2, 'Stagger Hall', 'College Column')
		self.assertEqual(['Stagger Hall', 'College Column'], path)
		self.assertEqual(4, expand.expand_count)

	def testHeuristics(self):
		# You don't need to do anything with this test.
		# It was designed to verify that the distance heuristics are consistent.
		good = True
		for loc1 in dis_map:
			for loc2 in dis_map:
				for loc3 in dis_map:
					d1, d2, d3 = dis_map[loc1][loc2], dis_map[loc1][loc3], dis_map[loc2][loc3]
					if d1+d2<d3 or d1+d3<d2 or d2+d3<d1:
						print("Bad Heuristics:", loc1, loc2, loc3, d1, d2, d3)
						good = False
		self.assertTrue(good)
	
	def testGoalIsStart(self):
		#Testing to see if there are any problems that arise when making the goal stat the start state as well
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map2, 'Big Cannon Hall', 'Big Cannon Hall')
		self.assertEqual(['Big Cannon Hall'], path)
		self.assertEqual(0, expand.expand_count)
	
	def testFakeLocation(self):
		#Testing if the locations provided are valid and if it  is possible to find a location
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map2, 'Big Cannon Hall', 'Stager')
		self.assertEqual([], path)
		self.assertEqual(0, expand.expand_count)

	# def testQ1(self): 
	# 	expand.expand_count = 0
	# 	path = sc.a_star_search(dis_map, time_map2, 'Big Cannon Hall', 'Hackathon Laboratory')
	# 	self.assertEqual(['Big Cannon Hall', 'Big Ben', 'Hackathon Laboratory'], path)
	# 	self.assertEqual(2, expand.expand_count)

if __name__== "__main__": unittest.main()
