import sys
import requests
from PIL import Image
from io import BytesIO


def get_img(url, crop_dims=None, resize=None, return_arr=False):
    '''
    Load an image from the given url using PIL

    Parameters
    ----------
    url : string
        the url to load the image from

    crop_dims : tuple
        4-tuple defining the left, upper, right, and lower pixel

    resize : int or tuple
        scale factor to resize by or 2-tuple for new image dimension

    return_arr : bool
        if true will return a U8int numpy array instead of PIL image obj
    '''

    # get the image
    req = requests.get(url)
    img = Image.open(BytesIO(req.content))

    # crop out the given region
    if crop_dims is not None:
        img = img.crop(crop_dims)

    # resize by the given factor or absolute size
    if resize is not None:
        if isinstance(resize, int):
            img = img.resize(np.array(img.size)//resize)
        elif isinstance(resize, tuple):
            img = img.resize(resize)
        else:
            raise ValueError

    # return array if watned
    if return_arr:
        return np.array(img)
    return img


def get_imgs(urls, crop_dims=None, resize=None, return_arr=True):
    '''
    batch processor for get_img, has a progress output aswell as
    a try except statment to prevent errodius urls losing progress
    '''

    imgs = []
    for i, url in enumerate(urls):

        try:
            sys.stdout.write(f'\r {100*i/len(urls):.2f}%  Loading {url}')
            imgs.append(get_img(url, crop_dims, resize, return_arr))

        except BaseException:
            sys.stdout.write(f'\r Error on {i}th url: {url}')
            print(' ')  # forces new line
            imgs.append(None)

    return imgs
