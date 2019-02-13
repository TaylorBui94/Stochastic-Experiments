import numpy as np
def coin50(n):
    success = 0
    
    N = 100
    for i in range(0,n):
        coin=np.random.randint(0,2,N)
        heads = sum(coin)
        tails = N-heads
        #
        p_heads = heads/N
        p_tails=tails/N
        if p_heads == .5:
            success += 1
    print (success/n)

n= 100000
coin50(n)
