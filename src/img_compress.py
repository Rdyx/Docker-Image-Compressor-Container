""" Image compression script """

import os
import sys

from PIL import Image

# from src import utils
from src import utils


IMG_FILE_FORMATS = ['jpg', 'jpeg', 'png']

CURRENT_DIRECTORY = os.getcwd()
IMG_INPUT_DIRECTORY = CURRENT_DIRECTORY + '/input/'
IMG_OUTPUT_DIRECTORY = CURRENT_DIRECTORY + '/output/'

# Verbose mode activation, remove -verbose from command to hide output informations
VERBOSE = utils.get_command_arg('--verbose')
# Enforcing size argument
HEIGHT_RESIZE = utils.get_command_arg('--max-height=')
# Enforcing size argument
WIDTH_RESIZE = utils.get_command_arg('--max-width=')
# Compression quality argument
COMPRESSION_QUALITY = utils.get_command_arg('--quality=')
print(COMPRESSION_QUALITY)


def get_image_infos(img, image_path):
    """ Get image informations such as size (h,w) & its weight (byte) """
    image_size = img.size
    image_weight = os.path.getsize(image_path)

    return {
        'size': {'height': image_size[0], 'width': image_size[1]},
        'weight': image_weight,
    }


# Compress each image found in input folder
for image_input_name in os.listdir(IMG_INPUT_DIRECTORY):
    # Check file extension
    if image_input_name.split('.')[-1] in IMG_FILE_FORMATS:
        image_input_path = IMG_INPUT_DIRECTORY+image_input_name
        image_output_path = IMG_OUTPUT_DIRECTORY+image_input_name
        image = Image.open(image_input_path)

        input_image_infos = get_image_infos(image, image_input_path)

        # Compressing image
        image.save(fp=(image_output_path), optimize=True, quality=50)

        output_image_infos = get_image_infos(image, image_output_path)

        if VERBOSE:
            print(utils.get_verbose_text)
