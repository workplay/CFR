import numpy as np

"""
    Define the game of Rock-Paper-Scissors as a normal-form game.
"""

ROCK = 0
PAPER = 1
SCISSORS = 2
NUM_ACTIONS = 3

PAYOFF_MATRIX = np.array([[[ 0.,  0.], [-1.,  1.], [ 1., -1.]], \
                          [[ 1., -1.], [ 0.,  0.], [-1.,  1.]], \
                          [[-1.,  1.], [ 1., -1.], [ 0.,  0.]]])    

"""
def getPayoffMatrix():          # get payoff matrix of ROCK-PAPER-SCISSORS
    matrix = np.zeros((3,3,2))
    for i in [ROCK, PAPER, SCISSORS]:
        for j in [ROCK, PAPER, SCISSORS]:
            if (i + 1) % 3 == j:
                matrix[i,j,0] = -1
                matrix[i,j,1] = 1
            elif i == (j+1) % 3:
                matrix[i,j,0] = 1
                matrix[i,j,1] = -1                
    return matrix  
"""