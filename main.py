import os
import sys
# from entities.isSafe import isSafe
# from entities.printSolution import printSo
import entities.sm
# from entities.solveMazeUtil import solveMazeUtil

# def run():
#    printsolution=printSolution() 
#    issafe=isSafe()
#    solvemazeutil=solveMazeUtil()
	


if __name__ == "__main__":

	maze = [ [1, 0, 0, 0],
			[1, 1, 0, 1],
			[0, 1, 0, 0],
			[1, 1, 1, 1] ]
entities.sm.solveMaze(maze)			
	