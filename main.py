import numpy as np

from utils.Variable import *
from utils.Functions import *

f = Square()
g = Exp()

x = Variable(np.array(0.5))
fx = f(x)
gfx = g(fx)
print(gfx.data)