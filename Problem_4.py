import numpy as np

#
def password(m):

    N = 1000
    check = 0
 
    n = np.power(26,4)
    for i in range (0,N):
        p = np.random.randint(0,n)
        H = np.random.randint(0,n,m)
        if p in H:
            check += 1        
    print(check/N)
#


m = 80000
k = 7
password(m*k)
