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
collection_name = 'testcollection'


#********* SET SOME VARIABLES ***********
# I felt is was easier to put the start and end values of the collection
# you ADD +1 to then end so that it stops on the previous number
# this collection will go from 1 to 500
# for these purposes this run will stop at 4
# but you can do 251,501,1001,3334(3333),100001 - careful you have enough space
# currently outputs to png
A,B = 1,5

img_catalogue,logo = [], []

print('Processing Images...')


#********* FOR LOOP ***********
# this section below is the for loop
# it runs through each image until it stops at the value stored in B
for r in range(A,B):
    a = random.choice([*range(1,5)])# select a random value from the range specified and this will be the choice for the background
    b = random.choice([*range(1,5)])
    c = random.choice([*range(1,5)])
    d = random.choice([*range(1,5)])
    e = random.choice(range(1,5))
    f = random.choice([*range(1,5)])
    g = random.choice([*range(1,5)])
    h = random.choice(range(1,5))
    i = random.choice([*range(1,5)])
    j = random.choice([*range(1,5)])

    # some images made more sense to above another layer depending on that image contents
    # so this section outputs a different order of images to use depending on the argument

    image_sequence = {
            'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,
    }

    img_list = [a,b,c,d,e,f,g,h,i,j]

    base = ipl.open(input_path+f'a{a}.png') # load background image and combine the aplha image over top of it
    img_combine = {}

    i=1
    check = 0
    #get the files
    for z in image_sequence.keys():
        if z in ['a','b']:
            value = image_sequence[z]
            if value: # if values == 0 pass
                img = ipl.open(input_path+z+f'{value}.png')
                angle = random.choice([0,90,180,270])
                img_combine[f'{z}{i}'] = pif.image_rotate(img,angle) # get the appropriate numbered image
            i += 1
        else:
            value = image_sequence[z]
            if value: # if values == 0 pass
                img_combine[f'{z}{i}'] = ipl.open(input_path+z+f'{value}.png') # get the appropriate numbered image
            i += 1


    for img in img_combine:
        base = pif.alpha_composite(img_combine[img],base) # apply the function to perform the merge of the two images
        #base.paste(img_combine[img], (0,0), img_combine[img])
    img_catalogue.append(img_list)
    pif.image_save(base,'output',f'{collection_name}{r}') # save the image
    # all the numerical values will get stored in a temp .csv file if you want to track rarity in the collection
    # create checkpoint dataset
    df = pd.DataFrame(img_catalogue,columns=['a','b','c','d','e','f','g','h','i','j',])
    df.to_csv(f'datasets/fallback_data.csv',index=False)

# the final dataset will be saved if the loop above runs to completion
collected = pd.DataFrame(img_catalogue,columns=['a','b','c','d','e','f','g','h','i','j',])
print(collected)
collected.to_csv(f'datasets/{collection_name}-collected-{A}-{B-1}.csv',index=False)
