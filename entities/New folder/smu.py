from safe import IsSafe

class solveMazeUtil:
    def intt(maze, x, y, sol) -> bool:
        N=4
        if x == N - 1 and y == N - 1 and maze[x][y]== 1:
            sol[x][y] = 1
            return (True)

        isSafe = IsSafe.SafeOrNot(maze, x, y)
        if isSafe == (True):
            if sol[x][y] == 1:
                return False
            
            sol[x][y] = 1
            

            if solveMazeUtil.intt(maze, x + 1, y, sol) == True:
                return (True)

            if solveMazeUtil.intt(maze, x, y + 1, sol) == True:
                return (True)
        
            if solveMazeUtil.intt(maze, x - 1, y, sol) == True:
                return (True)
            
            if solveMazeUtil.intt(maze, x, y - 1, sol) == True:
                return (True)
        
            sol[x][y] = 0
            return (False)