import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#
def sum2dice(N):
    
    s = np.zeros((N,1))
    for x in range(0,N):
        sevenCheck = 0
        count = 0
        
        while sevenCheck != 7:
            d1=np.random.randint(1,7)
            d2=np.random.randint(1,7)
            sevenCheck = d1 + d2
            count += 1
            
        s[x] = count

    #
    b=range(1,32) ; sb = np.size(b)
    h1, bin_edges = np.histogram(s,bins=b)
    b1=bin_edges[0:sb-1]
    plt.close('all')

    #
    fig1 = plt.figure(1)
    p1 = h1/N
    plt.stem(b1,p1)
    plt.title('Stem plot - Sum of two dice: Probability mass function')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Probability')
    plt.show()
    
N=10000
sum2dice(N)
