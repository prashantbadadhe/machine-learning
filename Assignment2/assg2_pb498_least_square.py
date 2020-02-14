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
	eta=0.0001
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

##calculate error outside the loop
error=0.0
for i in range (rows):
    if(trainlabels.get(i) != None):
        error += ( dotProduct(w,data[i]) - trainlabels.get(i) )**2

#initialize flag and iteration parameters
flag = 0
k=0

#begin iteration
while(flag != 1):
    k+=1
    delf = []
    for i in range(cols):
        delf.append(0)
    for i in range(rows):
        if(trainlabels.get(i) != None):
            dp = dotProduct(w, data[i])
            for j in range (cols):
                delf[j] += (dp - trainlabels.get(i)) * data[i][j]

##update
    for j in range(cols):
        w[j] = w[j] - getGradientLearningRate()*delf[j]

##compute error
    currError = 0
    for i in range (rows):
        if(trainlabels.get(i) != None):
            currError += ( dotProduct(w,data[i]) - trainlabels.get(i) )**2

#    print("Current Error: "currError,k)
    if error - currError < 0.001:
        flag = 1
    error = currError
#end of While loop

for i in range(rows):
    if(trainlabels.get(i) == None):
        dp = dotProduct(w, data[i])
        if(dp > 0):
            print("1",i)
        else:
            print("0",i)