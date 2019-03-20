import numpy as np
import RPSGame as rps
from RegretMatchPlayer import RMPlayer

p1 = RMPlayer()
p2 = RMPlayer()
oppStrategy = np.array([0.4,0.3,0.3])

for i in range(10l0000):
    a1 = p1.getAction(p1.getStrategy())
    a2 = p2.getAction(p2.getStrategy())
    p1.updateRegetSum(a2)
    p2.updateRegetSum(a1)

print(p1.getAverageStrategy())
print(p2.getAverageStrategy())