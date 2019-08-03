#                            Polynomial algebra

# This script contains functions which perform basic arithmetic operations
# on polynomials. Polynomials are represented by their coefficients in the
# form of a list. The index of the element of the list matches that of the
# degree of the polynomial i.e. polynomial written in increasing degree
# from left-to-right.

# Example: 1 + 2x + 3x^2 == [1,2,3]

f = [1,2,3]
g = [3,2,1]
h = [1,1]
p = [1]

def polynomial_addition(f,g):
    return [sum(x) for x in zip(f,g)]

def polynomial_multiplication(f,g):

    product = [0]*(len(f)+len(g)-1)

    for i in range(0,len(f)):

        for j in range(0,len(g)):

            c = f[i]*g[j]

            product[i+j] += c

    return product

# Should define functions which calculate polynomial quotient and remainder.
