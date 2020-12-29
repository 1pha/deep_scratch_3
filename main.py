import numpy as np

from utils.Variable import *
from utils.Functions import *

x = Variable(np.array(10))
f = Square()
y = f(x)

print(type(y))
print(y.data)