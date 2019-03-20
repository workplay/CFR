"""
   Compute best response in Rock-Paper-Scissors with Regret Matching.
"""
import numpy as np

ROCK = 0
PAPER = 1
SCISSORS = 2
NUM_ACTIONS = 3

regretSum = np.zeros(NUM_ACTIONS)
strategySum = np.zeros(NUM_ACTIONS)

oppStrategy = np.array([0.3,0.4,0.3])

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

def getStrategy():
    strategy = regretSum.copy()     # get Strategy according to regret sum.
    strategy[strategy<0] = 0        # change negatvie to 0.
    if strategy.sum() == 0 :
        strategy = np.ones(len(strategy)) / len(strategy) # if all strategies are 0, return normal distribution.
    else:
        strategy = strategy / strategy.sum()  # normalization.
    global strategySum
    strategySum += strategy
    return strategy

def getAction(strategy):
    return np.random.choice(len(strategy), 1, p = strategy)  # choose one action according to mix-strategy probability distribution

def train(iterations):
    matrix = getPayoffMatrix()
    actionUtility = np.zeros(NUM_ACTIONS)
    for i in range(iterations):
        # get regret-matched mixed-strategy actions
        strategy = getStrategy()
        myAction = getAction(strategy)
        otherAction = getAction(oppStrategy)
        # compute action utilities
        actionUtility = matrix[:, otherAction, 0].reshape(NUM_ACTIONS,)
        #accumulate action regrets
        regrets = actionUtility - actionUtility[myAction]
        global regretSum 
        regretSum += regrets

def getAverageStrategy():
    avgStrategy = np.zeros(NUM_ACTIONS)
    normalizationSum = strategySum.sum()
    if (normalizationSum > 0):
        avgStrategy = strategySum / normalizationSum
    else:
        avgStrategy = 1.0 / normalizationSum
    return avgStrategy

if __name__ == '__main__':
    train(100000)
    print(getAverageStrategy())