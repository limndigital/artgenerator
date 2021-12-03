# !/usr/bin/env python
# coding: utf-8
# go to the discord for support
# ## Art Generator Todd McCullough (culla)

import numpy as np
import pandas as pd
import random

# from IPython.display import Image as ipy
# this library is used to combine the imported layers and outputs the final image
from PIL import Image as ipl
from PIL import ImageFile, ImageFilter, ImageEnhance, ImageChops, ImageOps, ImageMath, ImageStat, ImageDraw

# this imports a random assortment of python functions making use of different Pillow functions
import pil_image_functions as pif

# you should place all of you layered images in the input folder and name them as shown in the example folder if you are new to coding
# if you know what you're doing, alter what you want and how you want
# get the images
input_path = 'input/'

# change this to your collection name - this will be outputted to the image file. I would advise against using spaces.
collection_name = 'abstrktI'


#********* SET SOME VARIABLES ***********
# I felt is was easier to put the start and end values of the collection
# you ADD +1 to then end so that it stops on the previous number
# this collection will go from 1 to 500
# for these purposes this run will stop at 4
# but you can do 251,501,1001,3334(3333),100001 - careful you have enough space
# currently outputs to png
A,B = 1,501

img_catalogue,logo = [], []

print('Processing Images...')

def get_random_blendmode(img1,img2,flt):

    lines_thin = pif.image_negative(pif.image_edges(img1))
    img_m_1 = pif.image_colour_filter(img1,channel='c',amount=flt)
    img_m_2 = pif.image_colour_filter(img2,channel='m',amount=flt)

    blend_modes = {
        'a col thin' : pif.image_filter(img1,lines_thin,mode='a',style='col',amount=flt),
        'm c mix' : pif.image_filter(img_m_1,img_m_2,mode='c',style='mix',amount=flt),
        'a mix' : pif.image_filter(img1,img2,mode='a',style='mix',amount=flt),
        'b mix' : pif.image_filter(img1,img2,mode='b',style='mix',amount=flt),
        'c mix' : pif.image_filter(img1,img2,mode='c',style='mix',amount=flt),
        'g mix' : pif.image_filter(img1,img2,mode='g',style='mix',amount=flt),
        'm mix' : pif.image_filter(img1,img2,mode='m',style='mix',amount=flt),
        'r mix' : pif.image_filter(img1,img2,mode='r',style='mix',amount=flt),
        'y mix' : pif.image_filter(img1,img2,mode='y',style='mix',amount=flt),
    }

    bm_list = [x for x in blend_modes.keys()]
    k = random.choice(bm_list)

    return blend_modes[k],k

more_passes = {}

#********* FOR LOOP ***********
# this section below is the for loop
# it runs through each image until it stops at the value stored in B
for r in range(A,B):

    img_combine = {}

    def composite_layer(letter,num):
        img_combine[f'{num}'] = ipl.open(f'lines/{letter}{num}.png') # get the appropriate numbered image

    linelist = [*range(1,22)]
    random.shuffle(linelist)
    linelist = linelist[:4]

    image_list = [*range(A,B)]
    random.shuffle(image_list)
    image_list.remove(r)

    img1_path = f'{input_path}{collection_name}{r}.png'
    img2_num = random.choice(image_list)# select a random value from the range specified and this will load the composite image
    img2_path = f'{input_path}{collection_name}{img2_num}.png'

    img1 = ipl.open(img1_path)
    img2 = ipl.open(img2_path)

    new_img,k = get_random_blendmode(img1,img2,random.choice([0.75,0.85,0.95,1]))

    #print(f'{r} {k}')

    letter_dict = {
        'a col thin' : 'e',
        'a mix thin' : 'b',
        'a col' : 'b',
        'a mix' : 'b',
        'm m mix' : 'c',
        'm c mix' : 'c',
        'b col' : 'a',
        'b mix' : 'b',
        'c col' : 'e',
        'c mix' : 'e',
        'g col' : 'c',
        'g mix' : 'd',
        'm col' : 'e',
        'm mix' : 'e',
        'r col' : 'a',
        'r mix' : 'b',
        'y col' : 'b',
        'y mix' : 'b',

    }
    letter = letter_dict[k]

    new_img = new_img.convert('RGBA')

    passes = random.choice([1,2,3,4])
    for i in range(passes):
        composite_layer(letter,linelist[i])

    for k in img_combine:
        new_img = pif.alpha_composite(img_combine[k],new_img) # apply the function to perform the merge of the two images


    pif.image_save(new_img,'output',f'{collection_name}{r}') # save the image

print('Processing complete.')
