from math import sqrt
import numpy as np
import scipy.linalg
import time

def Cholesky(A):
    n = A.shape[0]
    for j in range(n):
        y = 0
        for k in range(0,j):
            y = y + (A[j][k])**2
        A[j][j] = sqrt(A[j][j]-y)
        A[j+1:n,j] = (A[j+1:n,j]-np.dot(A[j+1:n,0:j],A[j,0:j]))/A[j][j]
    A = np.tril(A)
    return A


A = scipy.linalg.toeplitz([float(i) for i in range(2000,0,-1)])
start = time.time()
B = Cholesky(A)
#print(np.dot(B,B))
end = time.time()
A_result = np.matmul(B,np.transpose(B))
A = scipy.linalg.toeplitz([i for i in range(2000,0,-1)])
x = np.linalg.norm(A-A_result)
print("Cholesky: Benötigte Zeit: %f, Norm des Fehlers: %f" %(end-start, x))

#A = np.array([[4,6,-6,-4],[6,10,-14,-2],[-6,-14,83,-7],[-4,-2,-7,22]])
#print(Cholesky(A))