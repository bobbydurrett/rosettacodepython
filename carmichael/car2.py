"""

Python implementation of
http://rosettacode.org/wiki/Chernick%27s_Carmichael_numbers

"""

# use sympy for prime test

from sympy import isprime

def is_chernick(n, m):

    # U(n, m) = (6m + 1) * (12m + 1) * Product_{i=1..n-2} (2^i * 9m + 1)
    # prime factors
    
    if n < 3:
        return False
        
    # (6m + 1)
    factorminus1 = 6 * m
    factor = factorminus1 + 1
    
    if not isprime(factor):
        return False
        
    # (12m + 1) 
    
    factorminus1 *= 2
    factor = factorminus1 + 1
    
    if not isprime(factor):
        return False
        
    # Product_{i=1..n-2} (2^i * 9m + 1) 
    
    factorminus1 = 9 * m

    for i in range(1, n - 1):
        factorminus1 *= 2
        factor = factorminus1 + 1
        
        if not isprime(factor):
            return False
            
    return True
    
# from C version
        
for n in range(3,11):

    if n > 4:
        multiplier = 1 << (n - 4)
    else:
        multiplier = 1
    
    if n > 5:
        multiplier *= 5
        
        
    k = 1
    
    while True:
        m = k * multiplier
        
        if is_chernick(n, m): 
            print("a("+str(n)+") has m = "+str(m))
            break
            
        k += 1
       



