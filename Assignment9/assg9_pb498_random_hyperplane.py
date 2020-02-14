import sys
from math import sqrt
from sklearn import svm
import random
from sklearn.model_selection import cross_val_score

def readTestDataFile(datafile):
    f=open(datafile)
    merged_data=[]  
    l=f.readline()   
    while (l != ''): 
        a=l.split()
        l2=[]
        for j in range(0, len(a), 1):
            l2.append(float(a[j]))
        merged_data.append(l2)
        l=f.readline()
    f.close()
    return merged_data

def readLabelFile(labelfile):
    f=open(labelfile)
    trainlabels= {}  
    l=f.readline()   
    while(l != ''):
        a=l.split()
        trainlabels[int(a[1])] = int(a[0])
        l=f.readline()     
    f.close() 
    return trainlabels    


def dotProduct(w, x):
    dp = 0.0
    for wi, xi in zip(w, x):
        dp += wi * xi
    return dp
        
def sign(x):
    if(x > 0):
        return 1
    elif(x < 0):
        return -1
    return 0

datafile = sys.argv[1]
labelfile = sys.argv[2]
k = int(sys.argv[3])
merged_data=readTestDataFile(datafile)
trainlabels=readLabelFile(labelfile)

data=[]
testdata=[]
prow = []
for i in range(0,len(merged_data),1):
    if(trainlabels.get(i)==None):
        testdata.append(merged_data[i])
        prow.append(i)
    else:
        data.append(merged_data[i])

noRows=len(data)
noCols =len(data[0])

labels=list(trainlabels.values())
dataSets=data
testDataSets=testdata

w = []
for i in range(0, k, 1):
    w.append([])
    for j in range(0, noCols, 1):
        w[i].append(random.uniform(-1, 1))
        


z = []
for i, data in enumerate(dataSets):
    z.append([])
    for j in range(0, k, 1):
        
        z[i].append(sign(dotProduct(w[j], data)))
    
z1 = []
for i, data in enumerate(testDataSets):
    z1.append([])
    for j in range(0, k, 1):
        
        z1[i].append(sign(dotProduct(w[j], data)))


#------------------------------------------------------------
print('Original data')
svm_model = svm.SVC(kernel='linear', C=0.1, gamma=1) 
svm_model.fit(dataSets, labels)

p_labels = svm_model.predict(testDataSets)

scores_o = cross_val_score(svm_model, dataSets, labels, cv=5)
scores_o[:]=[1-x for x in scores_o]
print("Best error for orginal data: ",scores_o.min())

# print('Predicted labels using Original Datapoints')

# for i in range(len(p_labels)):
#     print(int(p_labels[i]), prow[i])
#------------------------------------------------------------
print('Random hyperplanes data')
model = svm.SVC(kernel='linear', C=0.1, gamma=1) 
model.fit(z, labels)

training_labels = model.predict(z)

scores = cross_val_score(model, z, labels, cv=5)
scores[:]= [1-x for x in scores]
print("Best error for new features data: ",scores.min())

# p_labels = model.predict(z1)

# print('Predicted labels using Random hyperplanes')

# for i in range(len(p_labels)):
#     print(int(p_labels[i]), prow[i])
#-------------------------------------------------------------        
