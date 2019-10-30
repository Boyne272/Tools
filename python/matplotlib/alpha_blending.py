# -*- coding: utf-8 -*-
"""
author: Richard Bonye (github Boyne272)
Last updated on Wed Sep 18 10:15:05 2019
"""


import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread


def alpha_blend(img_back, img_front, a_front, a_back=1.):
    """
    Creates a single rgb array for overlaying the two images with their
    relative alpha values
    """
    tmp = a_back * (1. - a_front)
    return (img_front * a_front + img_back * tmp) / (a_front + tmp)


def highlight(img, mask, color=[0., 1., 0.], alpha=0.5):
    return alpha_blend(img[mask], np.array(color), alpha)


if False:
    
    fig, axs = plt.subplots(2,2, figsize=[15, 15])
    
    img = imread('GUI/butterfly.tif') /255.
    axs[0, 0].imshow(img)
    
    mask = np.zeros_like(img)
    mask[500:, 500:, 1] = 1.
    axs[0, 1].imshow(mask)
    
    overlay = alpha_blend(img, mask, 0.5)
    axs[1, 0].imshow(overlay)
    
    
    axs[1, 1].imshow(img)
    axs[1, 1].imshow(mask, alpha=0.5)
    

if True:
    
    fig, axs = plt.subplots(2,2, figsize=[15, 15])
    
    img = imread('GUI/butterfly.tif') /255.
    axs[0, 0].imshow(img)
    
    mask = np.zeros(img.shape[:-1])
    mask[500:, 500:] = 1.
    color = 'g'
    axs[0, 1].imshow(mask)
    
    axs[1, 1].imshow(img)
    arr = np.zeros((img.shape[0], img.shape[1], 4))
    arr[mask.astype('bool')] = [0., 1., 0., 0.5]
    plt.imshow(arr)
    
    
    img[mask.astype('bool')] = alpha_blend(img[mask.astype('bool')], np.array([0., 1., 0.]), 0.5)
    axs[1, 0].imshow(img)
#    mask2 = np.zeros_like(img[:, :, 0]).astype('bool')
#    mask2[500:, 500:] = True
#    rgba = np.dstack([mask2, mask2, mask2, mask2])
#    axs[1, 1].imshow(mask)
    
    