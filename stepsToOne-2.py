

import math

def steps(n):
    values=[math.inf]
    i=1
    
    while i<=n:
        minSteps=i-1
        if i%3==0:
            if i/3 < len(values):
                minSteps=min(minSteps, values[int(i/3)]+1)
        if i%2==0:
            if i/2 < len(values):
                minSteps=min(minSteps, values[int(i/2)]+1)
        if i-1 < len(values):
            minSteps=min(minSteps,values[i-1]+1)
        
        values.append(minSteps)
        i+=1
        
    return values[n]


def greedy_steps(n):
    if n==1: return 0
    elif n%3==0: return steps(n//3) +1
    elif n%2==0: return steps(n//2)+1
    else: return steps(n-1)+1
    
    
def main():
    num=10000
    dif=0
    for i in range(num):
        dynamic=steps(i)
        greedy=greedy_steps(i)
        #print(i,": ",dynamic," ",greedy)
        if greedy!=dynamic: dif+=1
        
    print(100*dif/num,"% different values")
        
main()