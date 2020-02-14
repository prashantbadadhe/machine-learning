import sys
import random

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
    file=open(filename,FILE_MODE_READ)
    line=file.readline()
    while(line != '') : #read
        columns = line.split()
        if int(columns[0]) == 0:
            trainlabels[int(columns[1])] = -1
        else:
            trainlabels[int(columns[1])] = int(columns[0])
        line = file.readline()
    return trainlabels  

##initialize w
def initialize(cols):
    w = []
    for j in range(cols):
        w.append(0)
        w[j] = (0.02 * random.uniform(0,1)) - 0.01
    return w

##define function dot_product
def dotProduct(list1, list2):
    dp = 0
    refw = list1
    refx = list2
    for j in range (cols):
        dp += refw[j] * refx[j]
    return dp

##initialize Delf
def initializeDelf(cols):
    delf=[]
    for i in range(cols):
        delf.append(0)
    return delf
##set gradient descent learning rate
def getGradientLearningRate():
    eta=0.001
    return eta;

testDataFile=sys.argv[1]
trainLabelfile=sys.argv[2]
data=readTestDataFileAsList(testDataFile)
#print("\nTest Data: ",data)
rows = len(data)
cols = len(data[0])
trainlabels=readTrainLabelFileAsMap(trainLabelfile)
#print("\Train labels Data: ",trainlabels)
w=initialize(cols)
delf =initializeDelf(cols)

#initialize flag and iteration parameters
flag = 0
k=0
ydp = 0

##calculate error outside the loop
error=0.0
for i in range (rows):
    if(trainlabels.get(i) != None):
        ydp = (trainlabels.get(i))*dotProduct(w,data[i])
        error += max(0.0, (1.0 - ydp))
        
#print(error)

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
            for j in range (cols):
                 if ( ydp < 1):
                     delf[j] += (-1 * (trainlabels.get(i) * data[i][j]))
                 elif(ydp >= 1):
                     delf[j] += 0

##update
    for j in range(cols):
        w[j] = w[j] - getGradientLearningRate()*delf[j]

##compute error
    currError = 0
    for i in range (rows):
        if(trainlabels.get(i) != None):
            ydp = (trainlabels.get(i))*dotProduct(w,data[i])
            currError += max(0, (1.0 - ydp))

    # print(currError,k)    
    if abs(error - currError) < 0.000000001:
        flag = 1
    error = currError
    # print("error: ",error)
    ## calculate differences in error:

# print("count",k)
print("w =",w)

normw = 0
for j in range((cols-1)):
   normw += w[j]**2
  # print(w[j])

normw = (normw)**0.5
print("||w||=", normw)

distanceOrigin = w[(len(w)-1)] / normw
print("d =",abs(distanceOrigin))


#print("count",k)

for i in range(rows):
    if(trainlabels.get(i) == None):
        dp = dotProduct(w, data[i])
        if(dp > 0):
            print("1",i)
        else:
            print("0",i)