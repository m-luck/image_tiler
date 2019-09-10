import sys
import argparse
import random
import os
from PIL import Image
from PIL import ImageDraw, ImageFont

def generate_rand_grid():
    if len(sys.argv) > 1:
        p = argparse.ArgumentParser()
        p.add_argument('image_paths', nargs='+')
        args = p.parse_args()
        image_paths = args.image_paths
    else: 
        ids = random.sample(range(1, 7), 6)
        image_paths = [os.path.join('to_num_b',str(i) + '.png') for i in ids] 
    
    ids = [str(i) for i in ids]
    name = '-'.join(ids) + '.png'

    if os.path.exists(name):  
        return 

    images = map(Image.open, image_paths)
    widths, heights = zip(*(i.size for i in images))

    rows = random.sample(range(1, 4), 1)[0]   
    cols = 6 // rows
    total_width = cols * max(widths)
    max_height = rows * max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    y_offset = 0
    images = map(Image.open, image_paths)
    font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Roboto-Regular.ttf")
    print(font_path)
    font = ImageFont.truetype(font_path, 50)
    for i, im in enumerate(images):
        new_im.paste(im, (x_offset,y_offset))
        ImageDraw.Draw(
            new_im # Image
        ).text(
            (x_offset + 20, y_offset + 20),  # Coordinates
            str(i+1),  # Text
            (0, 0, 0),  # Color
            font=font
            )
        print(x_offset, y_offset)
        x_offset += max(widths)
        if (i+1) % cols == 0 and i != 0: 
            y_offset += max(heights)
            x_offset = 0

    ids = [str(i) for i in ids]
    name = '-'.join(ids) + '.png'
    print("Generating", name)
    new_im.resize((total_width//3,max_height//3), Image.ANTIALIAS).save(name, "PNG")

if __name__ == "__main__":
    for i in range(0,25):
        generate_rand_grid()