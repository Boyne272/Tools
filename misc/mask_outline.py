# -*- coding: utf-8 -*-
"""
author: Richard Bonye (github Boyne272)
Last updated on Mon Oct  7 10:32:24 2019
"""
# needs fixing to be stand alone
# imports need to be corrected

def _outline(self, diag=True, original=False, multi=True):
    """
    Take the stored mask and use a laplacian convolution to find the
    outlines for plotting. diag decides if diagonals are to be
    included or not, original decides if the original mask should
    be used or not.
    multi is an option to do horizontal, vertical and multi_directional
    laplacians and combine them. This is a safer method as particular
    geometries can trick the above convolution.
    """
    # select the correcy arrays based on the options given
    lap = self._laplacian_8 if diag else self._laplacian_4
    mask = self.mask if not original else self.orig_mask

    # do the convolution to find the edges
    conv = convolve2d(mask, lap, mode='valid').astype(bool)

    if multi:
        conv2 = convolve2d(mask, self._laplacian_h,
                           mode='valid').astype(bool)
        conv3 = convolve2d(mask, self._laplacian_v,
                           mode='valid').astype(bool)
        conv = (conv + conv2 + conv3).astype(bool)


    # pad back boarders to have same shape as original image
    conv = np.pad(conv, 1, 'edge')

    return conv.astype(float)
