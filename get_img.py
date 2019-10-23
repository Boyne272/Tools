import sys
import requests
import numpy as np
from PIL import Image
from io import BytesIO

def get_img(url, crop_dims=None, return_arr=False):

    # get the image
    req = requests.get(url)
    img = Image.open(BytesIO(req.content))

    # crop out the center
    if crop_dims is not None:
        img = img.crop(crop_dims)
                    
    # return array if watned
    if return_arr:
        return np.array(img)
    return img

def get_imgs(urls, return_arr=False):

    imgs = []
    for i, url in enumerate(urls):
        try:
            sys.stdout.write(f'\r {100*i/len(urls):.2}%  Loading {url}')
            imgs.append(get_img(url, return_arr=True))
        except BaseException:
            sys.stdout.write(f'\r Error on {i}th url: {url}')
            print(' ') # forces new line
            imgs.append(None)
    
    return imgs
