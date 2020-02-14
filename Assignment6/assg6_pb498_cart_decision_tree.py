import sys

class findGini:
    def __init__(self):
        pass
    
    def grantMyWish(self, trainX, trainY):
        
        lamp = {}
        rows = len(trainX)
        colmTrainX = list(zip(*trainX))
        
        for i, colm in enumerate(colmTrainX):
            for splitIndex in range(0, rows, 1):
                
                leftTrainY, rightTrainY = [], []
                
                splitVal = colm[splitIndex]
                
                for j, val in enumerate(colm):
                    if val < splitVal:
                        leftTrainY.append(trainY[j])
                    else:
                        rightTrainY.append(trainY[j])
                
                lsize = len(leftTrainY)
                rsize = len(rightTrainY)
                
                lp = sum([1 if lab == -1 else 0 for lab in leftTrainY])
                rp = sum([1 if lab == -1 else 0 for lab in rightTrainY])

                if lsize == 0:
                    term1 = 0
                else:
                    lterm1 = lsize/rows
                    lterm2 = lp/lsize
                    lterm3 = 1 - (lp/lsize)
                    
                    term1 = lterm1 * lterm2 * lterm3
                
                if rsize == 0:
                    term2 = 0
                else:
                    rterm1 = rsize/rows
                    rterm2 = rp/rsize
                    rterm3 = 1 - (rp/rsize)
                    
                    term2 = rterm1 * rterm2 * rterm3
                
                ginie =  term1 + term2
                print("gini: ",ginie)
                leftTrainX = []
                for val in colm:
                    if val < splitVal:
                        leftTrainX.append(val)
                
                if len(leftTrainX) != 0:
                    leftMax = max(leftTrainX)
                else:
                    leftMax = splitVal
                
                mainSplit = (leftMax + splitVal)/2
                
                if ginie not in lamp.keys():
                    lamp[ginie] = [[i, mainSplit]]
                else:
                    lamp[ginie].append([i, mainSplit])

        wish = min(lamp.keys())
        
        return lamp[wish]

################ DEFINING HYPERPARAMETERS AND FILE PATHS ################

dataFile = sys.argv[1]
labelFile = sys.argv[2]

################ DATA PRE-PROCESSING ################

data = open(dataFile, encoding='utf-8').readlines()
data = [line.strip().split() for line in data]
data = [list(map(float, line)) for line in data]

trainlabels = open(labelFile, encoding='utf-8').readlines()
trainlabels = [line.strip().split(' ') for line in trainlabels]
trainlabels = [list(map(int, line)) for line in trainlabels]

trainX, trainY = [], []
trainIndex = []

for (label, i) in trainlabels:
    trainX.append(data[i])

    if label == 1:
        trainY.append(1)
    else:
        trainY.append(-1)

    trainIndex.append(i)

testX = []
testIndex = [i for i in range(len(data)) if i not in trainIndex]

if len(testIndex) == 0:
    testIndex = trainIndex

else:
    for i in testIndex:
        testX.append(data[i])

if len(testX) == 0:
    testX = trainX

################ TRAINING MODEL ################
# print("trainX: ",trainX)
# print("trainY: ",trainY)
myGinie = findGini()
wish = myGinie.grantMyWish(trainX, trainY)

for (k, s) in wish:
    print(k, s)