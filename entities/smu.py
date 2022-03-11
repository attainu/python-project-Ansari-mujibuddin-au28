from entities.safe import isSafe

class solveMazeUtil:
    def __init__(self,maze, x, y, sol):
        self.i = isSafe
        N=4
        if x == N - 1 and y == N - 1 and maze[x][y]== 1:
            sol[x][y] = 1
            return True

        if self.i(maze, x, y) == True:

            if sol[x][y] == 1:
                return None
            
            sol[x][y] = 1
            

            if solveMazeUtil(maze, x + 1, y, sol) == True:
                return True

            if solveMazeUtil(maze, x, y + 1, sol) == True:
                return True
        
            if solveMazeUtil(maze, x - 1, y, sol) == True:
                return True
            
            if solveMazeUtil(maze, x, y - 1, sol) == True:
                return True
        
            sol[x][y] = 0
            return False
            