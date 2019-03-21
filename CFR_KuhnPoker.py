import numpy as np

# Kuhn Poker Definitions
PASS = 0
BET = 1
NUM_ACTIONS = 2
NUM_CARDS = 3
nodeMap = {}  # Node info and Node.

class Node: 
    # Kuhn node definitions
    def __init__(self):
        self.infoSet = ""
        self.regretSum = np.zeros(NUM_ACTIONS)
        self.strategy = np.zeros(NUM_ACTIONS)
        self.strategySum = np.zeros(NUM_ACTIONS)
    
    # Get current information set mixed strategy through regret-matching.
    def getStrategy(self, realizationWeight):
        strategy = self.regretSum.copy()     # get Strategy according to regret sum.
        strategy[strategy<0] = 0             # change negatvie to 0. Only consider positive regrets
        if strategy.sum() == 0 :
            strategy = np.ones(len(strategy)) / len(strategy) # if all strategies are 0, return normal distribution.
        else:
            strategy = strategy / strategy.sum()  # normalization.
        self.strategySum += realizationWeight * strategy              # accumulate for avrage strategy.
        return strategy    
    
    # Get average infromation set mixed strategy across all training iterations
    def getAverageStrategy(self):
        avgStrategy = np.zeros(NUM_ACTIONS)
        normalizationSum = self.strategySum.sum()
        if (normalizationSum > 0):
            avgStrategy = self.strategySum / normalizationSum
        else:
            avgStrategy = 1.0 / len(self.avgStrategy)
        return avgStrategy
    
    # Get information set string representation
    def toString(self):
        return self.infoSet.ljust(6) + '  ' + str(self.getAverageStrategy())
    
def ShuffleCards():
    return np.random.permutation(NUM_CARDS)

def cfr(cards, history, p0, p1):
    plays = len(history)
    player = plays % 2
    opponent = 1 - player
    # Return payoff for terminal states
    # Payoff Matrix\
    if history == 'pp':
        return 1 if cards[player] > cards[opponent] else -1
    elif history == 'pbp' or history == 'bp':
        return 1
    elif history == 'pbb' or history == 'bb':
        return 2 if cards[player] > cards[opponent] else -2
            
    # Get information set node or create it if nonexistant
    infoSet = str(cards[player]) + history
    if infoSet in nodeMap:
        node = nodeMap[infoSet]
    else:
        node = Node()
        node.infoSet = infoSet
        nodeMap[infoSet] = node
    # For each action, recursively call cfr with additional history and probability
    strategy = node.getStrategy(p0 if player == 0 else p1)
    util = np.zeros(NUM_ACTIONS)
    nodeUtil = 0
    for a in range(NUM_ACTIONS):
        if a == 0:
            nextHistory = history + 'p'
        else:
            nextHistory = history + 'b'
        if player == 0:
           util[a] = -cfr(cards, nextHistory, p0*strategy[a], p1)
        else:
           util[a] = -cfr(cards, nextHistory, p0, p1*strategy[a])
        nodeUtil += strategy[a] * util[a]
    # For each action, compute and accumulate conterfactual regret.
    regret = util - nodeUtil
    if player == 0:
        node.regretSum += p1 * regret
    else:
        node.regretSum += p0 * regret
    return nodeUtil
    
def train():
    util = 0
    for i in range(1000000):    
        cards = ShuffleCards()
        util += cfr(cards, '', 1,1)
    print(util/1000000)
    for n in list(nodeMap.values()):
        print(n.toString())

if __name__ == '__main__':
    train()