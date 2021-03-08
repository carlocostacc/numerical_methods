from matplotlib import pyplot as plt
import numpy as np
# Ri = Yi - f(Xi; Ao, ... , An)
# squared error R1^2 + R2^2 + ... + Rm^2 = SE
def linear_regression(arrayofx, arrayofy, A0, A1):
    modelarr = []
    for x in arrayofx:
        modelarr.append(A0 + A1 * x)
    print("the model array for the linear regression using the A0 value ", A0, " and the A1 value", A1," is :")
    print(modelarr)
    residualarr = []
    print("here is how the residual array was calculated")
    for x in range(len(modelarr)):
        print("position ", x,": ", arrayofy[x], " - ", modelarr[x], " = ", arrayofy[x] - modelarr[x])
        residualarr.append(arrayofy[x] - modelarr[x])
    print(residualarr)
    squarederror = 0
    print("how the squared error was found")
    for x in residualarr:
        print("SE = ", squarederror," + ", x, " * ", x )
        squarederror = squarederror + x*x
    print("the squared error is equal to : ", squarederror)
    plt.scatter(arrayofx,arrayofy)
    xmin = min(arrayofx)
    xmax = max(arrayofx)
    x = np.linspace(xmin, xmax, 100)
    y = A0 + x*A1
    plt.plot(x,y)
    plt.show()
def errorminimization(arrayofx, arrayofy):
    xy = []
    xpower2 = []
    for x in range(len(arrayofx)):
        xy.append(arrayofx[x]*arrayofy[x])
    print("xy values are", xy)
    for x in arrayofx:
        xpower2.append(x*x)
    print("the x^2 values are ", xpower2)
    somofarrayx = 0
    somofarrayy = 0
    somofxy = 0
    somofxpower = 0
    for x in range(len(arrayofx)):
        somofarrayx += arrayofx[x]
        somofarrayy += arrayofy[x]
        somofxy += xy[x]
        somofxpower += xpower2[x]
    print("the som of the x is : ", somofarrayx)
    print("the som of the array y is ",somofarrayy)
    print("the some of the xy is ", somofxy)
    print("the som of the xpower2 is ", somofxpower)
    m = len(arrayofx)
    A1 = ((m * somofxy) - (somofarrayx * somofarrayy))/((m * somofxpower) - (somofarrayx * somofarrayx))
    print("the value of A1 = ", A1)
    A0 = (1/m) * somofarrayy - A1*(1/m)*somofarrayx
    print("the value of A0 = ", A0)
    return A0, A1



def exponential_regression(arrayofx, arrayofy):
    for y in range(len(arrayofy)):
        arrayofy[y] = np.log(arrayofy[y])
    print("we first compute the ln of the y values")
    print(arrayofy)
    A0 , A1 = errorminimization(arrayofx, arrayofy)
    linear_regression(arrayofx, arrayofy, A0, A1)

def power_regression(arrayofx, arrayofy):
    for y in range(len(arrayofy)):
        arrayofy[y] = np.log(arrayofy[y])
        arrayofx[y] = np.log(arrayofx[y])
    print("we first compute the ln of the x and y values")
    print("x: ",arrayofx)
    print("y: ",arrayofy)
    A0, A1 = errorminimization(arrayofx, arrayofy)
    linear_regression(arrayofx, arrayofy, A0, A1)pwd