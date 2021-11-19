import numpy as np
import pandas as pd
import random

#from IPython.display import Image as ipy
from PIL import Image as ipl
from PIL import ImageFile, ImageFilter, ImageEnhance, ImageChops, ImageOps, ImageMath, ImageStat, ImageDraw

def image_bands(img):
    bands = img.split()
    return bands[0].point(lambda x: 255 if x < 20 else 0) # alter what x is greater than

def image_blur(img,radius=2):
    return img.filter(ImageFilter.GaussianBlur(radius))# better than BLUR

def image_brightness_contrast(img,brightness=1.0,contrast=1.0,amount=0.5):
    img_b= ImageEnhance.Brightness(img)
    img_c = ImageEnhance.Contrast(img)
    return ipl.blend(img_b.enhance(brightness),img_c.enhance(contrast),amount)

def image_convert(img,mode='L'):
    # L, LA, 1(converts to halftone), P(converts to colour halftone), RGB for it to work
    return img.convert(mode)

def image_crop(img):
    # figure out how to make this square and others
    width, height = img.size
    return img.crop((width/5, height/8, width-(width/7), height-(height/5)))

def image_data(img):
    return np.array(img)

def image_channel(img,chk='r'):
    img_data = image_data(img)
    img_chn = np.zeros(img_data.shape, dtype='uint8')
    if chk == 'b':
        img_chn[:,:,2] = img_data[:,:,2]
    elif chk == 'g':
        img_chn[:,:,1] = img_data[:,:,1]
    else:
        img_chn[:,:,0] = img_data[:,:,0]
    return ipl.fromarray(img_chn)

def image_combine(img,img2):
    return ImageMath.eval("convert(min(a, b), 'L')", a=img, b=img2)

def image_edges(img):
    return img.filter(ImageFilter.FIND_EDGES)

def image_flip(img):
    img_data = image_data(img)
    img_flipped_data = np.flip(img_data, axis=1)
    return ipl.fromarray(img_flipped_data)

def image_info(img):
    print(img.format, img.size, img.mode)

def image_multiply(img1,img2):
    img1 = image_convert(img1,mode='RGB')
    img2 = image_convert(img2,mode='RGB')
    return ImageChops.multiply(img1,img2)

def image_negative(img):
    img_data = image_data(img)
    img_reversed_data = 255 - img_data
    return ipl.fromarray(img_reversed_data)

def image_overlay_color(main,colour,alpha):
    overlay = Image.new(main.mode, main.size, colour)
    bw_img = ImageEnhance.Color(main).enhance(0.0)
    return ipl.blend(bw_img, overlay, alpha)

def image_overlay_blend(main,overlay,alpha):
    #main = ImageEnhance.Color(main).enhance(0.0)
    overlay = overlay.resize((main.size[0], main.size[1]),Image.ANTIALIAS)
    return ipl.blend(main, overlay, alpha)

def image_overlay_add(main,overlay):
    overlay = overlay.resize((main.size[0], main.size[1]),Image.ANTIALIAS)
    return ImageChops.add(main,overlay,1,0)

def image_recolorize(main, black="#000099", white="#99CCFF"):
    return ImageOps.colorize(ImageOps.grayscale(main), black, white)

def image_resize(img,value=2,scale=0):
    if scale == 0:
        return img.resize((int(img.size[0] / value), int(img.size[1] / value)),ipl.ANTIALIAS)
    else:
        return img.resize((int(img.size[0] * value), int(img.size[1] * value)))

def image_rotate(img,angle=90):
    return img.rotate(angle,expand=False)

def image_dimension_match(img1,img2):
    return  img2.resize((img1.size))

def image_save(img,filepath='output',filename='image',ext='png'):
    img.save(f'{filepath}/{filename}.{ext}',quality=100)

def image_thumb(img):
    filename = img.filename.split('/')[-1]
    out = img.resize((int(img.size[0] / 30), int(img.size[1] / 30)),ipl.ANTIALIAS)
    out.save(f'images/thumbs/thumb-{filename}',quality=75)

def alter_colour(img,old_colour,new_colour):
    ro,go,bo = old_colour
    rn,gn,bn = new_colour
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            if (r, g, b) == (ro,go,bo):
                pixels[x, y] = (rn,gn,bn, a)
    return img

def alpha_composite(src, dst):
    '''
    Return the alpha composite of src and dst.

    Parameters:
    src -- PIL RGBA Image object
    dst -- PIL RGBA Image object

    The algorithm comes from http://en.wikipedia.org/wiki/Alpha_compositing
    '''
    # http://stackoverflow.com/a/3375291/190597
    # http://stackoverflow.com/a/9166671/190597
    src = np.asarray(src)
    dst = np.asarray(dst)
    out = np.empty(src.shape, dtype = 'float')
    alpha = np.index_exp[:, :, 3:]
    rgb = np.index_exp[:, :, :3]
    src_a = src[alpha]/255.0
    dst_a = dst[alpha]/255.0
    out[alpha] = src_a+dst_a*(1-src_a)
    old_setting = np.seterr(invalid = 'ignore')
    out[rgb] = (src[rgb]*src_a + dst[rgb]*dst_a*(1-src_a))/out[alpha]
    np.seterr(**old_setting)
    out[alpha] *= 255
    np.clip(out,0,255)
    # astype('uint8') maps np.nan (and np.inf) to 0
    out = out.astype('uint8')
    out = ipl.fromarray(out, 'RGBA')
    return out
