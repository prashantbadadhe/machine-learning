import sys
import random
import math

def readData(datafile):
    f = open(datafile)
    data = []
    l = f.readline()

    ### Read Data ###
    while (l != ''):
        a = l.split()
        l2 = []
        for j in range(0, len(a), 1):
            l2.append(float(a[j]))
        data.append(l2)
        l = f.readline()
    f.close()    
    return data

datafile = sys.argv[1]
data=readData(datafile)
rows = len(data)
cols = len(data[0])
print(data)

## get k 
k = int(sys.argv[2])

## initialize m 
m = []
col = []
for j in range(cols):
    col.append(0)

for i in range(k):
    m.append(col)

random1 = 0

for c in range(k):
    random1=random.randrange(0,(rows-1))
    m[c] = data[random1]

#print("initial m",m)

## classifying the points 
labels = {}
diff = 1

prev = [[0]*cols for x in range(k)]

d =[]

md =[]
for c in range(k):
    md.append(0)
n = []
for c in range(k):
    d.append(0.1)
for c in range(k):
    n.append(0.1)
totald =1
clusters=[]

while ((totald) > 0):
    for i in range(rows):
        d =[]

        for c in range(k):
            d.append(0)
        for c in range(k):
            for j in range(cols):
                d[c] += ((data[i][j] - m[c][j])**2)
        for c in range(0, k, 1):
            d[c] = (d[c])**0.5
        mind=0
        mind = min(d)
        #print(mind)
        #print(d[0],d[1],d[2])
        for c in range(k):
            if(d[c]== mind):
                labels[i] = c
                
                n[c]+=1
                break
                

    ## compute means 
    m = [[0]*cols for x in range(k)]
    col = []
    #print m

    for i in range(rows):
        for c in range(k):
            if(labels.get(i) == c):
                for j in range(cols):
                
                    temp =  m[c][j]
                    temp1 =  data[i][j]
                    m[c][j] = temp + temp1

                    
    for j in range(cols):
        for i in range(k):
            m[i][j] = m[i][j]/n[i]

    clusters = [int(x) for x in n]       # data in each cluster
    n=[0.1]*k

    ## compute dance between means 
    md = []
    for c in range(k):
        md.append(0)
    for c in range(k):
        for j in range(cols):
            md[c]+=float((prev[c][j]-m[c][j])**2)

        md[c] = (md[c])**0.5
    #print(md)
    prev=m
    totald = 0
    for b in range(len(md),1):
        totald += md[b]           #dist between m

#### classify datapoints  
for i in range(rows):
    print(labels[i],i)