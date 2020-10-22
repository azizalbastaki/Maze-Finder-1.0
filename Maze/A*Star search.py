from processText import importMaze, mazePointer

testObject = importMaze("mazefile")
environment = testObject.processThis()
finger = mazePointer(environment)
frontier = []
frontierValues = []
explored = []
result = ""
#ADD COORDINATES AFTER CHECKING THE START AND GOAL
def checkClose(coordinate):
    number = 0
    if [coordinate[0],coordinate[1]+1] in explored:
        number+=1
    if [coordinate[0],coordinate[1]-1] in explored:
        number+=1
    if [coordinate[0]+1,coordinate[1]] in explored:
        number+=1
    if [coordinate[0]-1,coordinate[1]] in explored:
        number+=1
    return number
def Search(numofsteps):
    global result
    if len(finger.nearbyFreeSpaces("G")) == 1: #If the goal is bordering this space
        result = finger.nearbyFreeSpaces("G")[0]
        explored.append(finger.currentPosition)
    else:
        newPlaces = finger.nearbyFreeSpaces("F") #finds the free spaces bordering
        for i in newPlaces:
            if i in explored: #Skips the ones already visited
                pass
            else:
                frontier.append(i)
                frontierValues.append([finger.findDistance(i),numofsteps])

Search(1)
while result == "":
    explored.append(finger.currentPosition)
    try:
        bestNumber = (24**24)**24
        bestIndex = -1
        steps = 0
        for i in range(0,len(frontier)):
            if frontierValues[i][0]+frontierValues[i][1] < bestNumber:
                bestNumber = frontierValues[i][0]+frontierValues[i][1]
                bestIndex = i
        tempStep = frontierValues[bestIndex][1]
        finger.moveTo(frontier[bestIndex])
        frontier.pop(bestIndex)
        frontierValues.pop(bestIndex)
        Search(tempStep+1)
    except:
        pass
def tracingPath():
    initialExplored = explored
    proceed = True
    newExplored = []
    exploredCount = len(initialExplored)
    while proceed == True:
        for i in initialExplored:
            finger.moveTo(i)
            if len(finger.nearbyFreeSpaces("G")) == 1:
                pass
            elif (len(finger.nearbyFreeSpaces("S")) == 1) and (len(finger.nearbyFreeSpaces("F")) > 0):
                pass
            elif checkClose(i) > 1:
                pass
            elif checkClose(i) == 1:
                initialExplored.remove(i)
            else:
                print(checkClose(i))

        if len(initialExplored) == exploredCount:
            proceed = False
        else:
            exploredCount = len(initialExplored)
    return initialExplored
exploredArray = []
def recreateMaze(array,newArray):
    for y in range(len(environment)): #Recreates the maze, fills in 'E' in where the AI has visited.
        holder = ""
        for x in range(len(environment[y])):
            if [x,y] in array:
                holder+= "E"
            else:
                holder+= str(environment[y][x])
        newArray.append(holder)
recreateMaze(explored,exploredArray)
tracedFinal = []
recreateMaze(tracingPath(),tracedFinal)

def createResult(mazeList,title,append): #Creating the file
    file = open("resultfile",append)
    string = title + " \n F - Free \n O - Occupied \n S - Starting point \n G - Goal \n E - Path/visited \n (Abdulaziz Albastaki 2020) \n \n (top left coordinate - 0,0) \n Final Solution  \n"
    final = tracingPath()
    for i in tracedFinal:
        string+= "\n" + str(i)
    string+= "\n \n All spots visited \n"
    for i in exploredArray:
        string+= "\n" + str(i)
    string+= "\n \n Original problem \n"
    for i in environment:
        string+= "\n" +str(i)

    file.write(string)
    file.close()

createResult(exploredArray,"A* SEARCH", "w")
