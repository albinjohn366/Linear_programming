import scipy.optimize

"""Minimize the cost
cost = -x1 -1.5x2
subject to the constraints
x1 <=4
x2 <= 6
-x1 - x2 <= -8
"""

# Setting the coefficients
c = [-1, -1.5]
A = [[1, 0], [0, 1], [-1, -1]]
b = [4, 6, -8]
# Optimizing the equation to find the best  value
result = scipy.optimize.linprog(c, A_ub=A, b_ub=b)

# Printing the best value
print('The optimal value for\nx1 is: {}\nx2 is: {}'.format(round(result.x[0],
                                                                 4),
                                                           round(result.x[1],
                                                                 4)))
