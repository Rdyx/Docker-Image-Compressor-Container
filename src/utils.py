""" Utils functions """


def get_command_arg(arg, args_list):
    """ Check if arg has been used in command line """
    return arg if arg in args_list else None


def get_arg_value(arg, args_list):
    """ Value for arg is supposed to be after the arg """
    arg_index = args_list.index(arg)
    return args_list[arg_index+1]


def get_verbose_text(image_input_name, input_image_infos, output_image_infos):
    """ Get verbose text for each compressed image """

    return 'Compressed {}.\
        Height from {}px to {}px. Width from {}px to {}px. Weight from {}b to {}b.'\
    .format(
        image_input_name,
        input_image_infos['size']['height'],
        output_image_infos['size']['height'],
        input_image_infos['size']['width'],
        output_image_infos['size']['width'],
        input_image_infos['weight'],
        output_image_infos['weight'],
    )
