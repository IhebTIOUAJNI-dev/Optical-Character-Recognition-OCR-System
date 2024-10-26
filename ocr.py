import numpy as np
from TFANN import ANNR

A = np.random.rand(32, 4)
Y = np.random.rand(32, 1)
a = ANNR([4], [('F', 4), ('AF', 'tanh'), ('F', 1)], maxIter = 16, name = 'mlpr1')
a.fit(A, Y)
S = a.score(A, Y)
YH = a.predict(A)