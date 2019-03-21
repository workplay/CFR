import numpy as np
import RPSGame as rps


class RMPlayer:
    def __init__(self):
        self.regretSum = np.zeros(rps.NUM_ACTIONS)
        self.strategySum = np.zeros(rps.NUM_ACTIONS)

    def getStrategy(self):
        strategy = self.regretSum.copy()     # get Strategy according to regret sum.
        strategy[strategy<0] = 0             # change negatvie to 0. Only consider positive regrets
        if strategy.sum() == 0 :
            strategy = np.ones(len(strategy)) / len(strategy) # if all strategies are 0, return normal distribution.
        else:
            strategy = strategy / strategy.sum()  # normalization.
        self.strategySum += strategy              # accumulate for avrage strategy.
        return strategy    

    def getAction(self, strategy):
        return np.random.choice(len(strategy), 1, p = strategy)  # choose one action according to mix-strategy probability distribution

    def updateRegetSum(self, oppAction):
        matrix = rps.PAYOFF_MATRIX
        strategy = self.getStrategy()
        myAction = self.getAction(strategy)
        # %% TODO: 
        # Warning: for symtric game, it's ok to write this way.
        # But need to change it to
        # matrix[oppAction, :, 1] for general games.
        actionUtility = matrix[:, oppAction, 0].reshape(rps.NUM_ACTIONS,)  
        # %%
        
        regrets = actionUtility - actionUtility[myAction]
        self.regretSum += regrets
        
    def getAverageStrategy(self):
        avgStrategy = np.zeros(rps.NUM_ACTIONS)
        normalizationSum = self.strategySum.sum()
        if (normalizationSum > 0):
            avgStrategy = self.strategySum / normalizationSum
        else:
            avgStrategy = 1.0 / len(self.avgStrategy)
        return avgStrategy
