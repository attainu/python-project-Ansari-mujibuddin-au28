import ps
import smu

class solveMaze:
    def intt(maze) -> bool:
        sol = [ [ 0 for j in range(4) ] for i in range(4) ]
        if smu.solveMazeUtil.intt(maze, 0, 0, sol) == False:
            print("Solution doesn't exist")
            return (False)
        
        ps.printSolution(sol)
        return (True)