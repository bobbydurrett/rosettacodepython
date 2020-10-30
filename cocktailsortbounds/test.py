A = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]

beginIdx = 0
endIdx = len(A) - 1

while beginIdx <= endIdx:
    print('A = {0}'.format(A))
    print('beginIdx = {0} endIdx = {1}'.format(beginIdx,endIdx))
    newBeginIdx = endIdx
    newEndIdx = beginIdx
    for ii in range(beginIdx,endIdx):
        print('first loop ii = {}'.format(ii))
        if A[ii] > A[ii + 1]:
            print('swap A[ii+1], A[ii] = {0},{1}'.format(A[ii+1], A[ii]))
            A[ii+1], A[ii] = A[ii], A[ii+1]
            print('A = {0}'.format(A))
            newEndIdx = ii
            
    endIdx = newEndIdx

    for ii in range(endIdx,beginIdx-1,-1):
        print('second loop ii = {}'.format(ii))
        if A[ii] > A[ii + 1]:
            print('swap A[ii+1], A[ii] = {0},{1}'.format(A[ii+1], A[ii]))
            A[ii+1], A[ii] = A[ii], A[ii+1]
            print('A = {0}'.format(A))
            newBeginIdx = ii
    
    beginIdx = newBeginIdx + 1

print(A)
