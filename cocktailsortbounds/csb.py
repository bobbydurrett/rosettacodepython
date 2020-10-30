"""

Python example of

http://rosettacode.org/wiki/Sorting_algorithms/Cocktail_sort_with_shifting_bounds

based on 

http://rosettacode.org/wiki/Sorting_algorithms/Cocktail_sort#Python

"""

def cocktail(a):
    for i in range(len(a)//2):
        swap = False
        for j in range(1+i, len(a)-i):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                swap = True
        if not swap:
            break
        swap = False
        for j in range(len(a)-i-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                swap = True
        if not swap:
            break
            
            
def cocktailshiftingbounds(A):
    beginIdx = 0
    endIdx = len(A) - 1
    
    while beginIdx <= endIdx:
        newBeginIdx = endIdx
        newEndIdx = beginIdx
        for ii in range(beginIdx,endIdx):
            if A[ii] > A[ii + 1]:
                A[ii+1], A[ii] = A[ii], A[ii+1]
                newEndIdx = ii
                
        endIdx = newEndIdx
    
        for ii in range(endIdx,beginIdx-1,-1):
            if A[ii] > A[ii + 1]:
                A[ii+1], A[ii] = A[ii], A[ii+1]
                newBeginIdx = ii
        
        beginIdx = newBeginIdx + 1

            
test1 = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]
cocktail(test1)
print(test1)
 
test2=list('big fjords vex quick waltz nymph')
cocktail(test2)
print(''.join(test2))
            
test1 = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]
cocktailshiftingbounds(test1)
print(test1)
 
test2=list('big fjords vex quick waltz nymph')
cocktailshiftingbounds(test2)
print(''.join(test2))

