# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:22:23 2016
Miscallaneous Files to help with counting

@author: Andris
"""
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib
import csv

def countTerms(dataArray,N_ITER):
    
    # Create Counter class
    cnt = Counter();
    
    # Cycle through the data array term by term and count
    for iter in dataArray:
        cnt[iter] += 1;
     
    # If the setting is set to ALL, then set N_ITER to max value 
    if N_ITER == 'ALL':
        N_ITER = len(cnt);
        
    # Take only the most common terms
    
    mostCommon = cnt.most_common(N_ITER);        
        
    # List all the terms and their values from the counter class into seperate arrays

    terms = [];
    values = [];

    for it in range(N_ITER):
        terms.append(mostCommon[it][0])
        values.append(mostCommon[it][1])        
        

    # Return the terms and their respective values
    return terms,values
    
def plotCountArray(labels,values,name):
    
    # Creating auxillary x array
    x = range(len(values));
    
    # Plotting the bar chart
    plt.bar(x,values, align= 'center')
    
    # Assigning labels to x axis
    plt.xticks(x,labels, rotation=90)
    matplotlib.rc('font', family='DejaVu Sans')
    
    plt.tight_layout();
    plt.savefig(name +'.tif', format='tif', dpi=300)
    plt.show();
     
    
def cleanHashtag(array):
    
    
    store = [];    
    for iter1 in range(len(array)):
        
        L1 = len(array[iter1]);
        
        if L1 != 0 :
            
            for iter2 in range(L1):
               store.append(array[iter1][iter2]['text']);
               

    return store;
            
def arangeFavAndRetweet(favorite,displayName,IDofTweet,Ntweets):
    
    # Creating an array of indices to follow sorting change    
    index = range(len(favorite));
    cln = [];
    
    # Stringing index array and values together into a single tuple
    for iter in index:
        cln.append((index[iter],favorite[iter]))
        
    # Sorting tuple based on values, keeping track of indices    
    cln = sorted(cln, key=lambda col: col[1],reverse=True);
    
    # If the setting is set to ALL, then set N_ITER to max value         
    if Ntweets == 'ALL':
        Ntweets = len(cln)
    
    # Determining and assigning properties of interest
    indices = [];
    tweetID = [];
    nameTweeter = [];
    values = [];
                
    for iter in range(Ntweets):
        indices.append(cln[iter][0]);
        values.append(cln[iter][1]);
        nameTweeter.append(displayName[cln[iter][0]]);
        tweetID.append(IDofTweet[cln[iter][0]]);
        
        
    return nameTweeter, values, tweetID, indices;
    
def printToCSV(fName,titles,*arg):    

    L1 = len(arg[0]);    
    for arg1 in arg:
        
        if len(arg1) != L1:
            raise NameError('Arrays should be the same length!!!');
    
    convert = zip(*arg);

    with open(fName, 'w', newline='',encoding='utf-8') as csvfile:
        
        spamwriter = csv.writer(csvfile, delimiter=',')
        
        if titles:
            spamwriter.writerow(titles);        

        for row in convert:
            spamwriter.writerow(row);
    
def readCSV(fname):
    
    array = [];
    
    with open(fname,'r', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter = ',', quotechar='|')
        
        for row in reader:
            array.append(row)
            
    return array;

            
def convertToArray(data,col):
    array = [];

    for it in range(len(data)):
        array.append(data[it][col])    

    return array
    
    