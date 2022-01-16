import argparse
import os
import sys

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

IMAGE_FORMATS = {'.png', '.jpg', '.jpeg'}
FONT_TYPE = 'arial.ttf'

"""
Example usage:
python generator.py --files_path ../../assets/vanilla/classes/zoomed/ --height_out 1080 --width_out 1920 --sub_width 75 --sub_height 75 --width_buffer 60 --height_buffer 40 --strip_pattern Class --outfile ../../dist/vanilla_class_out.png

"""

def main():
    text = "Generic tool for creating an image gallery"

    parser = argparse.ArgumentParser(description=text, usage = "generate[options]")
    # Lots of args so add as 'optional' but make them required
    parser.add_argument("--files_path", help="Path to folder of images to generate gallery for", type=str, required=True)
    parser.add_argument("--outfile", help="Path to output image", type=str, required=True)
    parser.add_argument("--height_out", help="Height of output image in px", type=int, required=True)
    parser.add_argument("--width_out", help="Width of output image in px", type=int, required=True)
    parser.add_argument("--sub_width", help="Width of sub images image in px", type=int, required=True)                                    
    parser.add_argument("--sub_height", help="Height of sub image in px", type=int, required=True)
    parser.add_argument("--width_buffer", help="Horizontal spacing between images", type=int)
    parser.add_argument("--height_buffer", help="Vertical spacing between images", type=int)
    parser.add_argument("--font_size", help="Size of font text", type=int, default=14)
    parser.add_argument("--disable_text", help=" The name of an image will not be written below it", action="store_true")
    parser.add_argument("--strip_pattern", help="Removes pattern from image names", type=str, default="")


    args = parser.parse_args()
    err_stack = []
    if not os.path.exists(args.files_path):
        err_stack.append("Path to images folder does not exist")
    if not (args.height_out and args.width_out and args.sub_width and args.sub_height):
        err_stack.append("One or more invalid dimensions provided")
    if args.width_out < args.sub_width or args.height_out < args.sub_height:
        err_stack.append("Output image dimensions cannot be smaller than sub image dimensions")
    if not args.outfile:
        err_stack.append("No output file specified")
    if args.width_buffer < 0 or args.height_buffer < 0:
        err_stack.append("Buffer dimensions are invalid")
    if args.height_out < 0 or args.width_out < 0 or args.sub_width < 0 or args.sub_height < 0:
        err_stack.append("Invalid output dimensions")

    if err_stack:
        newline = '\n'
        print (f""" The following error(s) were encountered {[i + newline for i in err_stack]}""")
        return

    try:
        images = [os.path.join(args.files_path, i) for i in os.listdir(args.files_path) if os.path.splitext(i)[1] in IMAGE_FORMATS]
    except Exception as e:
        print (f"Error encountered sifting images most likely due to no extension: {e}")
        return
    # print (images)
    output_image = Image.new('RGB', (args.width_out, args.height_out))
    image_drawer = ImageDraw.Draw(output_image)
    image_font = ImageFont.truetype(FONT_TYPE, args.font_size) # This can throw depending on your system
    image_font_color = (255, 255, 255)
    image_iter = iter(images)
    exhausted = False

    for y in range(args.height_buffer, args.height_out, args.sub_height + args.height_buffer):
        if exhausted:
            # print ("No more images remaining")
            break
        for x in range(args.width_buffer, args.width_out, args.sub_width + args.width_buffer):
            next_image_path = next(image_iter, None)
            if next_image_path is None:
                exhausted = True
                break
            try:
                with Image.open(next_image_path) as im:
                    im.thumbnail((args.sub_width, args.sub_height))
                    output_image.paste(im, (x, y))
                    image_name = os.path.splitext(os.path.basename(next_image_path))[0].replace(args.strip_pattern, "")
                    if not args.disable_text:
                        image_drawer.text( (x, y + 4 + args.sub_height), image_name, image_font_color, font=image_font)
            except Exception as e:
                print (f"Error occurred pasting image {next_image_path}: {e}")
        
    output_image.save(args.outfile)
    print (f"Successfully wrote {args.outfile}")


if __name__ == "__main__":
    main()
