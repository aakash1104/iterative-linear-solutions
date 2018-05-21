import numpy
import sys
from pprint import pprint

MAX_ITERATIONS = 1000

"""
Jacobi() - Iterative Jacobi Method to solve a linear system of equations

@A - Square Matrix (N x N)
@b - Vector of size N x 1

Solve a linear system of the form Ax = b.
Constraint: Matrix A must be diagonally dominant

Return - The solution to the linear system
"""
def Jacobi(A, b):
    # Split A = D + R
    D = numpy.diag(A)
    R = A - numpy.diagflat(D)
    x = numpy.zeros_like(b)
    # Tolerence to check for convergence.
    limit = 1e-6 * numpy.ones_like(b);

    for i in range(0, MAX_ITERATIONS):
        x_new = ((b - numpy.dot(R, x)) / D)
        # Check for convergence
        check = (abs(x_new - x) <= limit)

        if (check[0] == True and check[1] == True):
            print i + 1, "iteration(s) for convergence"
            x = x_new
            break
        # If we don't reach tolerence limit within MAX_ITERATIONS.
        if (i == MAX_ITERATIONS - 1 and check[0] != True and check[1] != True):
            return -1

        x = x_new
    return x

def main():

    if (len(sys.argv) != 3):
        print "Usage: jacobi.py test_<num>.txt test_vector_<num>.txt"
        sys.exit(0)

    split_cols = int((sys.argv[1].split('_')[1]).split('.')[0])

    A = numpy.loadtxt(sys.argv[1], usecols=range(split_cols))
    b = numpy.loadtxt(sys.argv[2])
    # print ("A:")
    # pprint(A)
    #
    # print ("b:")
    # pprint(b)

    sol = Jacobi(A,b)

    print ("x:")
    print sol

main()
