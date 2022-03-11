# from tkinter import N


class isSafe:
    def __init__(self, maze, x, y) -> None:
        N=4
        if(x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1):
	        return True
        

        
        
