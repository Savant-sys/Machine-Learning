# from numpy import np
from numpy import *

def run():

    #Step 1 - collect the data
    #X = hours
    #Y = test score
    points = genfromtxt('data.csv', delimiter=',')

    #Step 2 - define our hyperparameters
    #how fast should our model converge?
    learning_rate = 0.0001

    #y = mx + b (slope formula)
    b = 0
    m = 0
    num_iteration = 1000

    #Step 3 - train our model
    # print ('starting gradient descent at b = {0}, m={1}, error = {2}'.format(b, m, compute_error_for_line_given_points))


if __name__ == '__main__':
    run()