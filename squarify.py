"""
partitions a rectangular image into squares and does something to each square
"""

from PIL import Image
import numpy as np
from typing import NamedTuple, Tuple
from collections import defaultdict
import random

class Square(NamedTuple):
    x_lo: int
    y_lo: int
    side: int

class Rectangle(NamedTuple):
    x_lo: int
    y_lo: int
    x_hi: int
    y_hi: int

filename = 'test.png'
im = Image.open('test.png')

width, height = im.size

array = np.zeros((height, width))
squaremembership = defaultdict(int)

# box = (left, upper, right, lower) (0,0) is upper left

def subdivide(image, box, depth):
    ## randomly pick an operation
    operations = [None, Image.ROTATE_180, Image.FLIP_LEFT_RIGHT, Image.FLIP_TOP_BOTTOM]
    op = random.choice(operations)
    

    ## apply operation
    if op:
        region = im.crop(box)
        region = region.transpose(op)
        image.paste(region, box)

    ## subdivide into [region]
        ## pick vertical split, horizontal split, quarters
    split = random.randint(0, 2)
    regions = []
    if split == 0: ## vertical
        vert = random.randint(box[0], box[2])
        regions += [(box[0], box[1], vert, box[3]), (vert, box[1], box[2], box[3])]
    elif split == 1: ## horizontal 
        horiz = random.randint(box[1], box[3])
        regions += [(box[0], box[1], box[2], horiz), (box[0], horiz, box[2], box[3])]


    ## recursively apply to region in regions with depth -1




def square_cut(rect):
    pass

def make_squares(array, squares):
    pass
