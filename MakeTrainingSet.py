class Interval:
    def __init__(self,start,end,data):
        self.startIndex = start
        self.endIndex = end
        self.dataSet = data

    def makeVector(self):
##                                                          
        #return self.dataSet                                     
        return (self.dataSet[self.prevInterval().startIndex[0]][self.prevInterval().startIndex[1]] + self.dataSet[self.startIndex[0]][self.startIndex[1]],
                self.dataSet[self.startIndex[0]][self.startIndex[1]],
                self.dataSet[self.startIndex[0]][self.startIndex[1]] + self.dataSet[self.endIndex[0]][self.endIndex[1]],
                self.dataSet[self.endIndex[0]][self.endIndex[1]],
                self.dataSet[self.endIndex[0]][self.endIndex[1]] + self.dataSet[self.nextInterval().endIndex[0]][self.nextInterval().endIndex[1]],
                self.isWordBoundary())
                                                

    def isWordBoundary(self):
            if self.dataSet[self.startIndex[0]][self.startIndex[1]+1] == ' ' or self.dataSet[self.startIndex[0]][self.startIndex[1]+1] == '\n':
                return 1
            return 0

    def nextInterval(self):
        #place the new endIndex next to the new startIndex, then check if se need to move it forward to do existencec of a space or new line
        newStartIndex = self.endIndex
        newEndIndex = (self.endIndex[0], self.endIndex[1]+1)
        if self.dataSet[self.endIndex[0]][newEndIndex[1]] == '\n':
            newEndIndex = (newEndIndex[0]+1, 0)
        elif self.dataSet[newEndIndex[0]][newEndIndex[1]] == ' ':
            newEndIndex = (newEndIndex[0],newEndIndex[1]+2)
        return Interval(newStartIndex, newEndIndex, self.dataSet)

    def prevInterval(self):
        #reverse of nextInterval
        newEndIndex = self.startIndex
        if self.startIndex[1] == 0: #Currently at first interval of the line
            newStartIndex = (self.startIndex[0]-1, len(self.dataSet[self.startIndex[0]-1])-2)
        else:
            newStartIndex = (self.startIndex[0],self.startIndex[1]-1)
        if self.dataSet[newStartIndex[0]][newStartIndex[1]] == ' ':
            newStartIndex = (newStartIndex[0],newStartIndex[1]-2)
        return Interval(newStartIndex, newEndIndex, self.dataSet)

    def hasNext(self):
        if self.endIndex == (len(self.dataSet)-1,len(self.dataSet[len(self.dataSet)-1])-2):
            return False
        return True

def makeTrainingSet(dataSet):
                interval = Interval((0,0),(0,1),dataSet)
                interval = interval.nextInterval() #We can't start at the first interval because we need a four character window, and doing it this way allows us to ckeck for a word boundary here or not.
                trainingSet = []
                while interval.hasNext():
                    trainingSet = trainingSet + [interval.makeVector()]
                    interval = interval.nextInterval()
                return trainingSet

def makeProbabilityDictionary(trainingSet):
                dict = {}
                for i in range(5):
                    for j in range(len(trainingSet)):
                        try:
                            dict[trainingSet[j][i]][trainingSet[j][5]] = dict[trainingSet[j][i]][trainingSet[j][5]] + 1
                        except KeyError:
                            dict[trainingSet[j][i]] = [0,0]
                            dict[trainingSet[j][i]][trainingSet[j][5]] = dict[trainingSet[j][i]][trainingSet[j][5]] + 1
                return dict
