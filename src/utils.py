""" Utils functions """
import sys


def get_command_arg(arg):
    """ Check if arg has been used in command line """
    return arg in sys.argv


def get_verbose_text(image_input_name, input_image_infos, output_image_infos):
    """ Get verbose text for each compressed image """
    return 'Compressed {}. Height from {}px to {}px, width from {}px to {}px, weight from {}b to {}b.'\
        .format(
            image_input_name,
            input_image_infos['size']['height'],
            output_image_infos['size']['height'],
            input_image_infos['size']['width'],
            output_image_infos['size']['width'],
            input_image_infos['weight'],
            output_image_infos['weight'],
        )
