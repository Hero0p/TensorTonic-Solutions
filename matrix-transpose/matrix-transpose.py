import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    a = np.asarray(A)
    n, m = a.shape

    ans = np.zeros((m,n))
    for i in range(n):
        for j in range(m):
            ans[j,i] = a[i,j]
    return ans
            
