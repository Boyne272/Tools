# -*- coding: utf-8 -*-
"""
author: Richard Bonye (github Boyne272)
Last updated on Mon Sep 23 12:46:42 2019
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#
## Grab some test data.
#X, Y, Z = axes3d.get_test_data(0.05)
#
## Plot a basic wireframe.
#ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
#
#plt.show()


def uniform_surface_polt(X, Y, Z):
    'Xs, Ys are 1d arrays, Z is a 2d array'
    
    assert X.size * Y.size == Z.size, 'Dimension mistmatch'
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    XX, YY = np.meshgrid(X, Y)
    ax.plot_surface(XX, YY, Z, cmap=plt.cm.coolwarm,
                    linewidth=0, antialiased=False)

    plt.show()
    
    return ax


def surface_func_plot(X, Y, func):
    return uniform_surface_polt(X, Y, func(*np.meshgrid(X, Y)))


def imshow_3d(ax, img, height):
    
    X, Y = np.meshgrid(np.arange(img.shape[0]),
                       np.arange(img.shape[1]))
    Z = np.ones_like(img) * height
    
    ax.plot_surface(X, Y, Z, cmap='gray', rstride=1, cstride=1,
                    facecolors=plt.cm.Greys(img), shade=False)


if __name__ == '__main__':
    
#    # uniform_surface_polt demo
#    Xs, Ys = np.arange(0,10), np.arange(1, 11)
#    Zs = np.stack([np.arange(i, i+10) for i in range(10)])
#    uniform_surface_polt(Xs, Ys, Zs)
#    
#    # surface_func_plot demo
#    f = lambda x,y: (x+y)**2
#    surface_func_plot(Xs, Ys, f)
    
    
    # make an image above its 2d surface
    from skimage.io import imread
    from skimage.filters import gaussian
    
    img = imread('butterfly.tif', as_gray=True)
    reduced_img = gaussian(img[000:100, 350:450], sigma=2)
    plt.imshow(gaussian(img, sigma=2), cmap='Greys_r')
    plt.axis('off')
    
    x = np.arange(reduced_img.shape[0])
    y = np.arange(reduced_img.shape[1])
    
    ax = uniform_surface_polt(x, y, reduced_img)
    
    imshow_3d(ax, reduced_img, 1.5)
    
    ax.axis('off')
    ax.set_zlim(0, 2)
    
#    plt.imshow(img)
    