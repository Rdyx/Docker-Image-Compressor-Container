""" Image compression script """

import os

from PIL import Image

import settings
import utils
import img_redimension
import img_compress


def get_image_infos(img, image_path):
    """ Get image informations such as size (h,w) & its weight (byte) """
    image_size = img.size
    image_weight = os.path.getsize(image_path)

    return {
        'size': {'height': image_size[0], 'width': image_size[1]},
        'weight': image_weight,
    }


# Compress each image found in input folder
for image_input_name in os.listdir(settings.IMG_INPUT_DIRECTORY):
    # Check file extension and process
    if image_input_name.split('.')[-1] in settings.IMG_FILE_FORMATS:
        image_input_path = settings.IMG_INPUT_DIRECTORY+image_input_name
        image_output_path = settings.IMG_OUTPUT_DIRECTORY+image_input_name
        image = Image.open(image_input_path)

        # Get image infos such as it's dimensions and it's weight in bytes
        input_image_infos = get_image_infos(image, image_input_path)
        img_height = input_image_infos['size']['height']
        img_width = input_image_infos['size']['width']

        # Image ratios
        height_width_ratio = (img_width / img_height)
        width_height_ratio = (img_height / img_width)

        # Trying to redimension image
        image = img_redimension.select_redimension_system(
            image, height_width_ratio, width_height_ratio, img_height, img_width
        )

        compression_quality_value = img_compress.get_image_compression_quality()

        # Save image
        image.save(fp=(image_output_path), optimize=True, quality=compression_quality_value)

        output_image_infos = get_image_infos(image, image_output_path)

        # Giving image modifications result
        if settings.VERBOSE_ARG:
            print(utils.get_verbose_text(image_input_name, input_image_infos, output_image_infos))
