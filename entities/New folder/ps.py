class printSolution:
    def __init__(self,sol):
        for i in sol:
            for j in i:
                print(str(j) + " ", end ="")
            print("")