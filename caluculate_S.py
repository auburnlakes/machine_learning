import numpy as np;
'''
Computes the S matrix.
    Syntax:
    S=calculate_S(X)
    Input:
    X: nxd data matrix with n vectors (rows) of dimensionality d
    n: number of rows in X
    m: output number of columns in S
    
    Output:
    Matrix S of size nxm
    S[i,j] is the inner-product between vectors X[i,:] and X[i,:]
    '''


def calculate_S(X,n,m):
    
    assert n == X.shape[0] 

    S = np.zeros((n,m))
    
    #S = np.arange(n * m).reshape(n,m)
    S = np.repeat(X.reshape((700,100)), 8, axis = 1)


    print ("the s matrix is {} ".format(S))

    return S

def calculate_S_dimensions():
    X = np.random.rand(700,100) # define random inputs
    Z = np.random.rand(800,100) # define random inputs
    n,d1=X.shape
    m,d2=Z.shape    
    S1 = calculate_S(X, n, m) # compute distances from your solutions
    o1,o2=S1.shape
    return (o1==n) and (o2==m)
print(calculate_S_dimensions())
