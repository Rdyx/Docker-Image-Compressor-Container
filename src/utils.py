""" Utils functions """

import settings


def get_command_arg(arg, args_list_settings):
    """ Check if arg has been used in command line """
    return arg if arg in args_list_settings else None


def get_arg_value(arg, args_list_settings):
    """ Value for arg is supposed to be after the arg """
    if arg in args_list_settings:
        arg_index = args_list_settings.index(arg)
        return args_list_settings[arg_index+1]


def get_verbose_text(image_input_name, input_image_infos, output_image_infos):
    """ Get verbose text for each compressed image """

    return 'Compressed {}.\
        Width from {}px to {}px. Height from {}px to {}px. Weight from {}b to {}b.'\
    .format(
        image_input_name,
        input_image_infos['size']['width'],
        output_image_infos['size']['width'],
        input_image_infos['size']['height'],
        output_image_infos['size']['height'],
        input_image_infos['weight'],
        output_image_infos['weight'],
    )
