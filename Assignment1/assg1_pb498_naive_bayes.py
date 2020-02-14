import sys

#read file as list
def readFileAsList(filename,mode):
	data=[]
	file=open(filename,mode)
	line=file.readline()
	while (line != ""):
		columns=line.split()
		arrRowData =[]
		for i in range (0,len(columns),1):
			arrRowData.append(float(columns[i]))
		data.append(arrRowData)
		line=file.readline()
	file.close()	
	return data	

#read file as map
def readFileAsMap(filename,mode):
	data={}
	file=open(filename,mode)
	line=file.readline()
	while (line != ""):
		columns=line.split()
		data[int(columns[1])] = int(columns[0])
		line=file.readline()
	file.close()	
	return data	


testDataFile=sys.argv[1]
trainLabelfile=sys.argv[2]
FILE_MODE_READ="r";
testData=readFileAsList(testDataFile,FILE_MODE_READ)
print("\nTest Data: ",testData)

rows=len(testData)
cols=len(testData[0])
#Read labels from file
labels=readFileAsMap(trainLabelfile,FILE_MODE_READ)
print("\nlabels: ",labels)
mean0=[]
mean1=[]
for i in range (0,cols,1):	
	mean0.append(0)
	mean1.append(0)
n0=0.0000001
n1=0.0000001
#summing up the row data and storing in mean0 and mean1 classes
for i in range(0,rows,1):
	#If labels==0
	if (labels.get(i) != None and labels.get(i) == 0):
		n0+=1
		for j in range (0,cols,1):
			print("\n\ttestData[",i,",",j,"] = ",testData[i][j])
			print("\n\tmean0[",j,"] = ",mean0[j])
			mean0[j] += testData[i][j]
			print("\n\tAfter Addition mean0 = ",mean0)

	#If labels==1
	if (labels.get(i) != None and labels.get(i) == 1):
		n1+=1
		for j in range (0,cols,1):
			mean1[j] += testData[i][j]

#Calculate means 			
for j in range (0,cols,1):
	mean0[j] /= n0
	mean1[j] /= n1

print ("\nMeans are:\n\tmean0=",mean0,"\n\tmean1=",mean1)

var0=[]
var1=[]
for i in range (0,cols,1):
	var0.append(0.00000001)
	var1.append(0.00000001)

#summing up the row data and storing in meanO and mean1 classes
for i in range(0,rows,1):
	if (labels.get(i) != None and labels.get(i) == 0):
		for j in range (0,cols,1):
			var0[j] += ((mean0[j] - testData[i][j])**2)
	if (labels.get(i) != None and labels.get(i) == 1):
		for j in range (0,cols,1):
			var1[j] += ((mean1[j] - testData[i][j])**2)

#Calculate Variance
for j in range (0,cols,1):
	var0[j] /= n0
	var1[j] /= n1
print("\nVariances are:\n\tvar0=",var0,"\n\tvar1=",var1)
print("\n****Output****\nLabel : Row Id");
for i in range (0,rows,1):
	w0=0
	w1=0	
	if (labels.get(i) == None):
		for j in range (0,cols,1):
			w0 += ((mean0[j] - testData[i][j])**2)/var0[j]
			w1 += ((mean1[j] - testData[i][j])**2)/var1[j]		
		if (w0 > w1):	
			print("1\t",i)
		else:
			print("0\t",i)
