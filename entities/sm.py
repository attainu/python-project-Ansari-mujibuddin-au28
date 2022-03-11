
from entities.ps import printSolution
from entities.smu import solveMazeUtil


class solveMaze:
    def __init__(self, maze) -> None:
        self.p = printSolution
        self.m = maze
        self.s = solveMazeUtil
        sol = [ [ 0 for j in range(4) ] for i in range(4) ]
        if self.s(self.m, 0, 0, sol) == False:
            print("Solution doesn't exist");
            return False
        
        self.p(sol)
        return True	

