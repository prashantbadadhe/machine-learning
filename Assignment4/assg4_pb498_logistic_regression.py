import sys
import random
import math

def sigmoid(v):
    if v < 0:
        return 1 - 1 / (1 + math.exp(v))
    return 1 / (1 + math.exp(-v))

def normalize(datafile):
    max = []
    min = []
    # writeData = open("normalized","w")
    for i in range(len(datafile[0])):
        max.append(0)
        min.append(0)
        
    for j in range(len(datafile)):
        for k in range(len(datafile[0])-1):
            if (datafile[j][k] > max[k]) :
                max[k] = datafile[j][k]
            if (datafile[j][k] < min[k]) :
                min[k] = datafile[j][k]

    for i in range(len(datafile)):
        for j in range(len(datafile[0])-1):
            if (max[j] - min[j] != 0):
                datafile[i][j] = (datafile[i][j] - min[j])/(max[j] - min[j])
    return datafile

##define function dotProduct
def dotProduct(list1, list2):
    dp = 0
    for j in range(len(list1)):
        dp += list1[j] * list2[j]
    return dp

FILE_MODE_READ="r";

#read data file as list
def readTestDataFileAsList(testDataFileName):
    file = open(testDataFile,FILE_MODE_READ)
    testData = []
    line = file.readline()

    while(line != '') : #read
        arr = line.split()
        arrLen = len(arr)
        tempArr = []
        for j in range(0, arrLen, 1):
            tempArr.append(float(arr[j]))
            if j == (arrLen-1) :
                tempArr.append(float(1))
        testData.append(tempArr)
        line = file.readline()
    return testData  

#read train lables file as map
def readTrainLabelFileAsMap(filename):
    trainlabels = {}
    n=[]
    n.append(0)
    n.append(0)
    file=open(filename,FILE_MODE_READ)
    line=file.readline()
    while(line != '') : #read
        a = line.split()
        trainlabels[int(a[1])] = int(a[0])
        line = file.readline()
        n[int(a[0])] += 1        
    return trainlabels  

##read data file
testDataFile=sys.argv[1]
trainLabelfile=sys.argv[2]

data=readTestDataFileAsList(testDataFile)
trainlabels=readTrainLabelFileAsMap(trainLabelfile)

rows = len(data)
cols = len(data[0])

## #check if normalising is required
maxd = 0
mind = 0
normal = 0
for i in range(cols):
    maxd = max(data[0])
    if (maxd > 1):
        normal = 1

if normal == 1 :
    data = normalize(data)

##initialize w
w = []
for j in range(cols):
    w.append(0)
    w[j] = (0.02 * random.uniform(0,1)) - 0.01

##initialize delf
delf = []
for i in range(cols):
    delf.append(0)

##gradient descent learning rate.
eta = 0.01

#initialize flag and iteration parameters
flag = 0
k=0
ydp = 0

##calculate error outside the loop
error=0.0
# class1cost = 0
# class2cost = 0
for i in range (rows):
    if(trainlabels.get(i) != None):
        ydp = (trainlabels.get(i))*dotProduct(w,data[i])
        dp = dotProduct(w,data[i])
        y = trainlabels.get(i)
        sigm = (1/(1 + math.exp(-1*dp)))
        error += (-y*math.log(sigm))-((1-y)*math.log((1-sigm))) 
        

#begin iteration
while(flag != 1):
    k+=1
    delf = []
    for i in range(cols):
        delf.append(0)

##compute gradient
    for i in range(rows):
        if(trainlabels.get(i) != None):
            dp = dotProduct(w, data[i])
            ydp = (trainlabels.get(i)*dotProduct(w,data[i]))
            y = trainlabels.get(i)
            sigm = (1/(1 + math.exp(-1*dp)))
            for j in range (cols):                
                delf[j] += (-y + sigm) * data[i][j]

##update
    for j in range(cols):
        w[j] = w[j] - eta*delf[j]

##compute error
    currError = 0
    for i in range (rows):
        if(trainlabels.get(i) != None):
            ydp = (trainlabels.get(i))*dotProduct(w,data[i])
            dp = dotProduct(w, data[i])
            y = trainlabels.get(i)
            sigm = (1/(1 + math.exp(-1*dp)))
            currError += (-y*math.log(sigm))-((1-y)*math.log((1-sigm))) 
    
    ##check objective
    if abs(error - currError) < 0.00000001:
        flag = 1
    error = currError


#print("count",k)
# print("w =",w)

normw = 0
for j in range((cols-1)):
   normw += w[j]**2
   print(w[j])

normw = (normw)**0.5
print("||w||=", normw)

distanceOrigin = w[(len(w)-1)] / normw
print("d =",distanceOrigin)

for i in range(rows):
    if(trainlabels.get(i) == None):
        dp = dotProduct(w, data[i])
        if dp > 0.5:
            print("1",i)
        else:
            print("0",i)