
from numpy import append
import sm

N = int(input("enter num 4 ="))



if __name__ == "__main__":

	maze = [ [1, 0, 0, 0],
			[1, 1, 0, 1],
			[0, 1, 0, 0],
			[1, 1, 1, 1] ]
			
	sm.solveMaze.intt(maze)

