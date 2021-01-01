from .Variable import Variable

def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0, y1 = f(x0), f(x1)

    return (y1.data - y0.data) / (2 * eps)