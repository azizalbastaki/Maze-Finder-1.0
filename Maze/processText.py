#code to process the mazefile file.
class importMaze:
    def __init__(self,maze):
        self.fileLines = []
        self.fileName = maze
        self.switch = False
        self.toBeReturned = []
    def processThis(self):
        f = open(self.fileName,"r")
        for x in f:
            self.fileLines.append(x[:-1])
        f.close()
        for i in self.fileLines:
            if self.switch == True:
                if str(i) == "END":
                    self.switch = False
                else:
                    self.toBeReturned.append(i)
            else:
                if str(i) == "START":
                    self.switch = True
        return self.toBeReturned
    
class mazePointer:
    def __init__(self,mazearray):
        self.Sample = mazearray
        self.initialPosition = []
        self.goalLocation = []

        for y in range(0, len(self.Sample)):
           for x in range(0,len(self.Sample[y])):
                if str(self.Sample[y][x]) == "S":
                    self.initialPosition = [x,y]
                elif str(self.Sample[y][x]) == "G":
                    self.goalLocation = [x,y]


        self.currentPosition = self.initialPosition
    def whatIs(self,xcoordinate,ycoordinate):
        return (self.Sample[ycoordinate])[xcoordinate]
    def nearbyFreeSpaces(self,search):
        self.freeSpaces = []
        if self.whatIs(self.currentPosition[0]-1,self.currentPosition[1]) == search:
            self.freeSpaces.append([self.currentPosition[0]-1,self.currentPosition[1]])
        if self.whatIs(self.currentPosition[0]+1,self.currentPosition[1]) == search:
            self.freeSpaces.append([self.currentPosition[0]+1,self.currentPosition[1]])
        if self.whatIs(self.currentPosition[0],self.currentPosition[1]-1) == search:
            self.freeSpaces.append([self.currentPosition[0],self.currentPosition[1]-1])
        if self.whatIs(self.currentPosition[0],self.currentPosition[1]+1) == search:
            self.freeSpaces.append([self.currentPosition[0],self.currentPosition[1]+1])
        return self.freeSpaces

    def moveTo(self,position):
        self.currentPosition = position

    def greedBFS(self):
        array = []
        for y in range(0,len(self.Sample)):
            newRow = []
            for x in range(0,len(self.Sample[y])):
                if str(self.Sample[y][x]) == "F":
                    xDigit = (((self.goalLocation[0] - x)**2)**0.5)
                    yDigit = (((self.goalLocation[1] - y)**2)**0.5)
                    newRow.append(str(xDigit+yDigit))
                else:
                    newRow.append(str(self.Sample[y][x]))
            array.append(newRow)
        return array
    def findDistance(self,position):
        return (((self.goalLocation[0] - position[0])**2)**0.5) + (((self.goalLocation[1] - position[1])**2)**0.5)