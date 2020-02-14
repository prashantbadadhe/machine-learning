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

def normalize(datafile):
    max = []
    min = []
   
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


testDataFile=sys.argv[1]
trainLabelfile=sys.argv[2]
data=readTestDataFileAsList(testDataFile)
data = normalize(data)
#print("\nTest Data: ",data)
rows = len(data)
cols = len(data[0])
trainlabels=readTrainLabelFileAsMap(trainLabelfile)
#print("\Train labels Data: ",trainlabels)
w=initialize(cols)
delf =initializeDelf(cols)
eta=0.001
##calculate error outside the loop
error=0.0
for i in range (rows):
    if(trainlabels.get(i) != None):
        error += ( dotProduct(w,data[i]) - trainlabels.get(i) )**2
#print("error:",error)
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

###adaptive eta 
    etaList = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
    bestobj = 100000000000000

    for n in range(0, len(etaList), 1):
        eta = etaList[n]

        ## update w
        for j in range(cols):
            w[j] = w[j] - eta*delf[j]

        ##get new error
        currError = 0
        for i in range(0, rows, 1):
            if(trainlabels.get(i) != None):
                ##update error
                currError += ( dotProduct(w,data[i]) - trainlabels.get(i) )**2

        obj = currError
        #print("currError : ",currError)

    ##update bestobj and best_eta    
        if obj < bestobj:
            bestobj = obj
            besteta = eta

    ##insert code here for w = w - eta*dellf
        for j in range(cols):
            w[j] = w[j] + eta*delf[j]
  
    ## use best eta
    if besteta != None:
        eta = besteta

##update w
    for j in range(cols):
        w[j] = w[j] - eta*delf[j]

##compute error
    currError = 0
    for i in range (rows):
        if(trainlabels.get(i) != None):
            currError += ( dotProduct(w,data[i]) - trainlabels.get(i) )**2
            
    if error - currError < 0.001:
        flag = 1
    error = currError

for i in range(rows):
    if(trainlabels.get(i) == None):
        dp = dotProduct(w, data[i])
        if(dp > 0):
            print("1",i)
        else:
            print("0",i)