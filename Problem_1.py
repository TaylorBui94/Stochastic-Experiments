import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#
def nSidedDie(p):
    N=10000
    s=np.zeros((N,1))
    n=len(p);
    print(n)
    #
    cs=np.cumsum(p)
    cp=np.append(0,cs)
    #
    for j in range(0,N):
        r=np.random.rand()
        for k in range(0,n):
            if r>cp[k] and r<=cp[k+1]:
                d=k+1
        s[j]=d
#
#plotting
    b= range(1,n+2)
    sb = len(b)
    h1, bin_edges=np.histogram(s, bins=b)
    b1=bin_edges[0:sb-1]
    plt.close('all')
    prob=h1/N
    plt.stem(b1,prob)
    # Graph labels
    plt.title('PMF for an unfair '+ str(n) + '-sided die' )
    plt.xlabel('Number on the face of the die')
    plt.ylabel('Probability')
    plt.xticks(b1)
    plt.show()


p=[0.10,  0.15,  0.20,  0.05,  0.3, 0.10, 0.1]
nSidedDie(p)
