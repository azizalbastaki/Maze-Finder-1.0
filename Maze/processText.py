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
        for y in range(0, len(self.Sample)):
           for x in range(0,len(self.Sample[y])):
               if str(self.Sample[y][x]) == "S":
                    self.initialPosition = [x,y]
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