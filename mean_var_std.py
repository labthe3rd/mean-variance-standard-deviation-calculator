#Programmer     labthe3rd
#date           10/04/2023
#desc           Data analysis
import numpy as np

def calculate(list):

    print(list)
    
    # Ensure the input list has 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    print("Creating array...")
    a = np.array(list)
    b = a.reshape(3,3)
    
    #mean
    m1 = np.mean(b,axis=0).tolist()
    m2 = np.mean(b,axis=1).tolist()
    mf = np.mean(b)
    
    #Calculate Variance
    v1 = np.var(b, axis=0).tolist()
    v2 = np.var(b,axis=1).tolist()
    vf = np.var(b)
    
    #Standard Deviation
    s1 = np.std(b, axis=0).tolist()
    s2 = np.std(b, axis=1).tolist()
    sf = np.std(b)
    
    #Max
    max1 = np.max(b, axis=0).tolist()
    max2 = np.max(b, axis=1).tolist()
    maxf = np.max(b)
    
    #Min
    min1 = np.min(b, axis=0).tolist()
    min2 = np.min(b, axis=1).tolist()
    minf = np.min(b)
    
    #sum
    sum1 = np.sum(b, axis=0).tolist()
    sum2 = np.sum(b, axis=1).tolist()
    sumf = np.sum(b)
    
    output = {
        'mean': [m1,m2,mf],
        'variance': [v1,v2,vf],
        'standard deviation': [s1,s2,sf],
        'max': [max1,max2,maxf],
        'min': [min1,min2,minf],
        'sum': [sum1,sum2,sumf]
    }

    print(output)

    return output