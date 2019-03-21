import numpy as np
import RPSGame as rps
from RegretMatchPlayer import RMPlayer

p1 = RMPlayer()
p2 = RMPlayer()
oppStrategy = np.array([0.4,0.3,0.3])

for i in range(100000):
    a1 = p1.getAction(p1.getStrategy())
    a2 = p2.getAction(p2.getStrategy())  # change p2.getStrategy() to a mixed strategy if to compute best response.
    p1.updateRegetSum(a2)
    p2.updateRegetSum(a1)

print(p1.getAverageStrategy())
print(p2.getAverageStrategy())