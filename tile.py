import sys
import argparse
import random
import os
from PIL import Image

def generate_rand_grid():
    if len(sys.argv) > 1:
        p = argparse.ArgumentParser()
        p.add_argument('image_paths', nargs='+')
        args = p.parse_args()
        image_paths = args.image_paths
    else: 
        ids = random.sample(range(1, 9), 4)
        image_paths = [os.path.join('to_num',str(i) + '.png') for i in ids] 
    
    ids = [str(i) for i in ids]
    name = '-'.join(ids) + '.png'

    if os.path.exists(name):  
        return 

    images = map(Image.open, image_paths)
    widths, heights = zip(*(i.size for i in images))

    rows = 2
    cols = 2
    total_width = rows * max(widths)
    max_height = cols * max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    y_offset = 0
    images = map(Image.open, image_paths)
    for i, im in enumerate(images):
        new_im.paste(im, (x_offset,y_offset))
        x_offset = x_offset + max(widths) if (i+1) % rows != 0 else 0
        if (i+1) % cols == 0: 
            y_offset += max(heights)

    ids = [str(i) for i in ids]
    name = '-'.join(ids) + '.png'
    print("Generating", name)
    new_im.resize((720,720), Image.ANTIALIAS).save(name, "PNG")

if __name__ == "__main__":
    for i in range(0,4096):
        generate_rand_grid()