import numpy as np
import scipy.linalg
import time

def gauß_rank1(A):
    n = A.shape[0]
    for j in range(n-1):
        A[j+1:n,j] = A[j+1:n,j]/A[j,j]  #Achtung mit floats
        A[j+1:n,j+1:n] = A[j+1:n,j+1:n]-(A[j+1:n,j]*A[j,j+1:n])
    R = np.triu(A)
    L = np.tril(A)
    for i in range(n):
        L[i][i] = 1
    return (L,R)

def gauß_gaxpy(A):
    n = A.shape[0]
    for j in range(n):
        for k in range(j-1):
            A[k+1:n,j] = A[k+1:n,j] - A[k][j]*A[k+1:n,k]
        A[j+1:n,j] = A[j+1:n,j]/A[j][j]
    R = np.triu(A)
    L = np.tril(A)
    for i in range(n):
        L[i][i] = 1
    return (L,R)


A = scipy.linalg.toeplitz([i for i in range(2000,0,-1)])
'''
#Gauß-Rank1
start = time.time()
B = gauß_rank1(A)
end = time.time()
A_result = B[0]*B[1]
x = np.linalg.norm(A-A_result)
print("Gauß-Rank1: Benötigte Zeit: %f, Norm des Fehlers: %f" %(end-start, x))

A = scipy.linalg.toeplitz([i for i in range(2000,0,-1)])
#Gauß-GAXPY
start = time.time()
B = gauß_gaxpy(A)
end = time.time()
A_result = B[0]*B[1]
x = np.linalg.norm(A-A_result)
print("Gauß-GAXPY: Benötigte Zeit: %f, Norm des Fehlers: %f" %(end-start, x))
'''
print(A)