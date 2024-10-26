import numpy as np
import os
import string
import sys
from skimage.io import imread
from sklearn.model_selection import ShuffleSplit
from TFANN import ANNC

FP = './'
TFP = os.path.join(FP, 'Train.csv')
A, Y, T, FN = [], [], [], []
MAX_CHAR = 256
print("succes")
with open(TFP) as F:
    for Li in F:
        FNi, Yi = Li.strip().split(',')                     #filename,string
        T.append(Yi)
        A.append(imread(os.path.join(FP, 'db', FNi)))
        Y.append(list(Yi) + [' '] * (MAX_CHAR - len(Yi)))   #Pad strings with spaces
        FN.append(FNi)
    print("succes for !")
print("open success !!!")
np.stack(A) 
np.stack(Y) 
np.stack(T) 
np.stack(FN)
print("acces")
NC = len(string.ascii_letters + string.digits + ' ')
MAX_CHAR = 64
IS = (14, 640, 3)       #Image size for CNN
ws = [('C', [4, 4,  3, NC // 2], [1, 2, 2, 1]), ('AF', 'relu'), 
      ('C', [4, 4, NC // 2, NC], [1, 2, 1, 1]), ('AF', 'relu'), 
      ('C', [8, 5, NC, NC], [1, 8, 5, 1]), ('AF', 'relu'),
      ('R', [-1, 64, NC])]
#Create the neural network in TensorFlow
c = ANNC(IS, Y, batchSize = 64, learnRate = 5e-5, maxIter = 32, reg = 1e-5, tol = 1e-2, verbose = True, name = "cnnc1")
if not c.RestoreModel('TFModel/', 'ocrnet'):
    print("erreur!!!")

#Fit the network
c.fit(A, Y)
#The predictions as sequences of character indices
YH = np.zeros((Y.shape[0], Y.shape[1]), dtype = np.int)
for i in np.array_split(np.arange(A.shape[0]), 32): 
    YH[i] = np.argmax(c.predict(A[i]), axis = 2)
#Convert from sequence of char indices to strings
PS = [''.join(CS[j] for j in YHi) for YHi in YH]
for PSi, Ti in zip(PS, T):
    print(Ti + '\t->\t' + PSi)