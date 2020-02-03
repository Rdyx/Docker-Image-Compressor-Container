""" Image compression script """

import os

from PIL import Image, ImageSequence

import settings
import utils
import img_redimension
import img_compress


def get_image_infos(img, image_path):
    """ Get image informations such as size (h,w) & its weight (byte) """
    image_size = img.size
    image_weight = os.path.getsize(image_path)

    return {
        'size': {'width': image_size[0], 'height': image_size[1]},
        'weight': image_weight,
    }


def process_image(image, height_width_ratio, width_height_ratio, img_width, img_height):
    # Trying to redimension image
    return img_redimension.select_redimension_system(
        image, height_width_ratio, width_height_ratio, img_width, img_height
    )


# Compress each image found in input folder
for image_input_name in os.listdir(settings.IMG_INPUT_DIRECTORY):
    # Check file extension and process
    if image_input_name.split('.')[-1] in settings.IMG_FILE_FORMATS:
        image_input_path = settings.IMG_INPUT_DIRECTORY+image_input_name
        image_output_path = settings.IMG_OUTPUT_DIRECTORY+image_input_name
        image = Image.open(image_input_path)

        # Get image infos such as it's dimensions and it's weight in bytes
        input_image_infos = get_image_infos(image, image_input_path)
        img_width = input_image_infos['size']['width']
        img_height = input_image_infos['size']['height']

        # Image ratios
        width_height_ratio = (img_height / img_width)
        height_width_ratio = (img_width / img_height)

        # Get number of frames in image
        n_frames = getattr(image, 'n_frames', 1)

        # "Normal" image, 1 frame (jpg, png...)
        if n_frames == 1:
            image = process_image(
                image, height_width_ratio, width_height_ratio, img_width, img_height
            )
            # Get image compression quality (Only available for jpg)
            compression_quality_value = img_compress.get_image_compression_quality()
            # Save image
            image.save(fp=(image_output_path), optimize=True, quality=compression_quality_value)
            output_image_infos = get_image_infos(image, image_output_path)

        # in the case of a multiframe image (.gif)
        else:
            frames = []

            # Process each frame as single image
            for frame in ImageSequence.Iterator(image):
                frames.append(
                    process_image(
                        frame, height_width_ratio, width_height_ratio, img_width, img_height
                    )
                )

            # Save gif, note that quality tag is not available for gifs
            frames[0].save(
                fp=(image_output_path), optimize=True, save_all=True, append_images=frames[1:]
            )
            output_image_infos = get_image_infos(frames[0], image_output_path)

        # Giving image modifications result
        if settings.VERBOSE_ARG:
            print(utils.get_verbose_text(image_input_name, input_image_infos, output_image_infos))
