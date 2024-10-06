import numpy as np

def calculate_R(Z, n, m):
    '''
    function calculate_R(Z)

    Computes the R matrix.
    Syntax:
    R=calculate_R(Z)
    Input:
    Z: mxd data matrix with m vectors (rows) of dimensionality d
    n: output number of rows in Z
    m: number of rows in Z

    Output:
    Matrix R of size nxm
    R[i,j] is the inner-product between vectors Z[j,:] and Z[j,:]
    '''
    assert m == Z.shape[0]
    # Square all the values in R

    Q = np.sum(np.square(Z), axis=1)
    R = np.tile(np.array([Q]).T, (1, n)).T
    print("R is :", R.shape, R.size)
    return R

    # YOUR CODE HERE
    raise NotImplementedError()


def calculate_R_dimensions():
   X = np.random.rand(7,10) # define random inputs
   Z = np.random.rand(8,10) # define random inputs
   n,d1=X.shape
   m,d2=Z.shape
   R1 = calculate_R(Z, n, m) # compute distances from your solutions
   print ("the shape of R1 is :", R1.shape)
   o1,o2=R1.shape
   print(" the values of o1, o2 are: ", o1, 'and', o2)
   return (o1==n) and (o2==m)


print(calculate_R_dimensions())

