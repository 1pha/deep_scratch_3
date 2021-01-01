class Variable:

    def __init__(self, data):
        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        f = self.creator
        if f is not None: # if f is None, then the Variable is the last node (=end of recursion)
            x = f.input # call the input before
            x.grad = f.backward(self.grad) # calculate the gradient of the function that made this Variable
            x.backward() # recursion

if __name__=="__main__":

    import numpy as np

    data = np.array(1.0)
    x = Variable(data)
    print(x.data)