import numpy as np
import matplotlib.pyplot as plt
num_steps=1000
stps=np.random.choice([-1,1],size=num_steps)
walk=np.cumsum(stps)
plt.plot(walk)
plt.show()