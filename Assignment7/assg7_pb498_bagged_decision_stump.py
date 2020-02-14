import sys
import random

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
                # print("gini: ",ginie)
                leftTrainX = []
                for val in colm:
                    if val < splitVal:
                        leftTrainX.append(val)
                
                if len(leftTrainX) != 0:
                    leftMax = max(leftTrainX)
                else:
                    leftMax = splitVal
                
                mainSplit = (leftMax + splitVal)/2
                
                lamp[ginie] = [i, mainSplit]

        wish = min(lamp.keys())
        
        return lamp[wish]
    
    def getBootstrappedData(self, data, labels):
      
        bootstrappedData = []
        bootstrappedLabels = []
        
        for _ in range(int(len(data))):
            idx = random.randint(0, len(data)-1)
            bootstrappedData.append(data[idx])
            bootstrappedLabels.append(labels[idx])
        
        return bootstrappedData, bootstrappedLabels
    
    def getLabels(self, trainX, trainY, splitCol, splitVal):
             
        left, right = 0, 0
        
        trainCol = list(list(zip(*trainX))[splitCol])
        
        for i, val in enumerate(trainCol):
            if val < splitVal:
                left += trainY[i]
            else:
                right += trainY[i]
     
        if left >= 0:
            leftLab = 1
        else:
            leftLab = -1
        
        if right >= 0:
            rightLab = 1
        
        else:
            rightLab = -1
        
        return [leftLab, rightLab]

    def bagging(self, trainX, trainY, testX, iterations = 100):
     
        if len(trainX) != len(trainY):
            raise ValueError('Data and labels dimensions mismatch')
        
        if type(iterations) != int:
            raise ValueError('iterations should be interger type')
        
        predictions = [0] * len(testX)
        
        for _ in range(iterations):
            
            data, labels = self.getBootstrappedData(trainX, trainY)
            
            splitCol, splitVal = self.grantMyWish(data, labels)
            
            leftLabel, rightLabel = self.getLabels(data, labels, splitCol, splitVal)
            
            testXCol = list(list(zip(*testX))[splitCol])
            
            for i, val in enumerate(testXCol):
                if val < splitVal:
                    predictions[i] += leftLabel
                else:
                    predictions[i] += rightLabel
        
        results = []
        
        for i, pred in enumerate(predictions):
            if pred >= 0:
                results.append(1)
            else:
                results.append(0)
        
        return results        

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
myGinie = findGini()
predictions = myGinie.bagging(trainX, trainY, testX, iterations=100)

for pred, idx in zip(predictions, testIndex):
    print(pred, idx)