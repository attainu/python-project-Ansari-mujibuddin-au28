class IsSafe:
    def __init__(self, maze, x, y):
        pass


    def SafeOrNot(maze, x, y):
        N=4
        
        if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
            return (True)
        print("This is the maze output")
        return (False)