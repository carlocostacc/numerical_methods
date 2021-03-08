import numpy as np


def forward_error(a, ans,Xr, cols, rows):
    # enter the number of cols and rows of the main matrix

    # the array a is for the matrix of coefficient
    # enter the awnsers

    r = np.linalg.solve(a, ans)

    print("\nthe r matrix is \n", r)

    print("\nthe Xr matrix is \n\n", Xr)

    final = np.subtract(r, Xr)

    print("\nthe awnser for the substraction is \n", final)

    comp = 0
    inf = 0
    for x in range(rows):
        value = final[x]
        if value < 0:
            value = value * -1
        if value >= comp:
            comp = value
            print("\nthe biggest absolute value of the operation AXr - B is \n", comp)

        value2 = r[x]
        if value2 < 0:
            value2 = value2 * -1
        if value2 >= inf:
            inf = value2
            print("\nthe biggest value of b is\n", inf)

    print("\nthe forward error is ", comp / inf)

