import numpy as np
# the values col and rows are the values of the matrix A


def backward_error(A,ans,Xr, cols, rows):

    print("matrix A is the coeficient matrix\n", A)

    print("matrix B is \n", ans)

    print("\nthe matrix Xr is \n", Xr)

    c = A.dot(Xr)
    print("\nthe matrix multiplication between A and Xr\n", c)

    final = np.subtract(c, ans)
    print("\nthe solution is of the substraction of AXr and B\n", final)

    comp = 0
    for x in range(rows):
        value = final[x]
        if value < 0:
            value = value * -1
        if value >= comp:
            comp = value
            print("\nthe biggest absolute value of the operation AXr - B is \n", comp)

    inf = 0
    for x in range(rows):
        value = ans[x]
        if value < 0:
            value = value*-1
        if value >= inf:
            inf = value
            print("\nthe biggest value of b is\n", inf)

    print("\nthe backward error is ", comp/inf)



