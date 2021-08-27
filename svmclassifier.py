from sklearn import svm
import csv
import numpy as np
import joblib as jb

def is_number(s):
    try:
        float(s) # for int, long and float
    except ValueError:
        return False

    return True

def svmTrain():
    f = open("PositiveHaze.csv")
    csv_f = csv.reader(f)
    tList=[]
    tClass=[]
    counter=0
    for row in csv_f:
        new_list=[]
        if counter < 2:
            counter=counter+1
            continue
        for item in row:
            if not(is_number(item)):
                continue
            new_list.append(float(item))
        print(new_list)
        if len(new_list)!=5:
            print("ERROR")
            continue
        tList.append(new_list)
        tClass.append(1)
    f.close()

    f=open("NegativeHazeAndNegativeFog.csv")
    csv_f=csv.reader(f)
    counter=0
    for row in csv_f:
        new_list=[]
        if counter < 2:
            counter=counter+1
            continue
        for item in row:
            if not(is_number(item)):
                continue
            new_list.append(float(item))
        print(new_list)
        if len(new_list)!=5:
            print("ERROR")
            continue
        tList.append(new_list)
        tClass.append(0)

    f.close();   
    f=open("PositiveFog.csv")
    csv_f= csv.reader(f)
    tFogList=[]
    tFogClass=[]
    counter=0
    
    for row in csv_f:
        new_list=[]
        if counter < 2:
            counter=counter+1
            continue
        for item in row:
            if not(is_number(item)):
                continue
            new_list.append(float(item))
        print(new_list)
        if len(new_list)!=5:
            exit(2)
            continue
            
        tFogClass.append(1)
        tFogList.append(new_list)
        
    f.close()
    f=open("NegativeHazeAndNegativeFog.csv")
    csv_f=csv.reader(f)
    counter=0
    for row in csv_f:
        new_list=[]
        if counter < 2:
            counter=counter+1
            continue
        for item in row:
            if not(is_number(item)):
                continue
            new_list.append(float(item))
        print(new_list)
        if len(new_list)!=5:
            continue
        tFogClass.append(0)
        tFogList.append(new_list)
        
    svmThunder = svm.SVC()
    
    svmThunder.fit(tList,tClass)
    
    svmFog = svm.SVC()
    
    svmFog.fit(tFogList,tFogClass)
    
    jb.dump(svmThunder, "svmHaze.pkl")
    jb.dump(svmFog, "svmFog.pkl")
    
if __name__ == '__main__':
    svmTrain()
