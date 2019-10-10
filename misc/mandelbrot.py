import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, max_iter=80):
    '''
    Take the complex array C and return an integer array
    givning the number of interations requiered to converge
    '''
    n = np.zeros(c.shape, dtype='int') # will not be complex
    z = np.zeros_like(c) # will be complex
    for i in range(max_iter):
        z = z*z + c
        msk = abs(z) > 2
        z[msk] = c[msk] = 0
        n[msk] = i
    return n
    
if __name__ == '__main__':
    x, y = np.meshgrid(*[np.linspace(-1, 1, 2000)]*2)
    plt.figure(figsize=[15, 15])
    plt.imshow(mandelbrot1(x + 1j*y))
    plt.colorbar()
