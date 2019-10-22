
import numpy as np
from IPython.display import display
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
