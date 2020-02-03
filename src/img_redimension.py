""" Image redimension related function """

import sys

import settings
import utils


def get_new_dimensions(img, axis, arg, args_list, ratio):
    """ Calculated new image dimensions """
    wanted_axis_dimension = int(utils.get_arg_value(arg, args_list))
    new_calculated_axis_dimension = wanted_axis_dimension / ratio

    if axis == 'width':
        return img.resize([wanted_axis_dimension, int(new_calculated_axis_dimension)])
    return img.resize([int(new_calculated_axis_dimension), wanted_axis_dimension])


def resize_image_from_command_args(
        image, height_width_ratio, width_height_ratio, img_height, img_width,
        height_resize_setting=settings.HEIGHT_RESIZE_ARG,
        width_resize_setting=settings.WIDTH_RESIZE_ARG,
        args_list_setting=settings.ARGS_LIST,
):
    """ Check used arguments and resize image depending on provided values """
    img_width = image.size[0]
    img_height = image.size[1]

    if height_resize_setting and img_height > height_resize_setting and not width_resize_setting:
        return get_new_dimensions(
            image, 'height', height_resize_setting, args_list_setting, height_width_ratio
        )

    if width_resize_setting and img_width > width_resize_setting and not height_resize_setting:
        return get_new_dimensions(
            image, 'width', width_resize_setting, args_list_setting, width_height_ratio
        )

    # In case of both args are set, first we will calculate from the longer axis
    # Then check if the other axis is matching the wanted value and recalculate if needed
    if height_resize_setting and width_resize_setting:
        if img_height > img_width:
            image = get_new_dimensions(
                image, 'height', height_resize_setting, args_list_setting, height_width_ratio
            )
        else:
            image = get_new_dimensions(
                image, 'width', width_resize_setting, args_list_setting, width_height_ratio
            )

        if img_width > int(utils.get_arg_value(width_resize_setting, args_list_setting)):
            return get_new_dimensions(
                image, 'width', width_resize_setting, args_list_setting, width_height_ratio
            )

        return get_new_dimensions(
            image, 'height', height_resize_setting, args_list_setting, height_width_ratio
        )

    # If nothing matches, simply return image
    return image


def resize_image_from_ratio(img, ratio_arg, args_list):
    """ Resize image with a defined ratio directly """
    ratio = float(utils.get_arg_value(ratio_arg, args_list))

    return img.resize([int(img.size[0]*ratio), int(img.size[1]*ratio)])


def select_redimension_system(
    image, height_width_ratio, width_height_ratio, img_height, img_width,
    height_resize_setting=settings.HEIGHT_RESIZE_ARG,
    width_resize_setting=settings.WIDTH_RESIZE_ARG,
    ratio_setting=settings.RATIO_ARG,
    args_list_setting=settings.ARGS_LIST,
):
    """ Select which redimension system will be used based on arguments provided in command """

    # Prevent user from using ratio calculation + max size value
    if (
            (height_resize_setting and ratio_setting) or
            (width_resize_setting and ratio_setting)
    ):
        sys.stdout.write(
            'Warning ! Don\'t use --ratio and --max-height or --max-width at same time.\n'
        )
        sys.stdout.flush()
        return sys.exit(1)

    if height_resize_setting or width_resize_setting:
        return resize_image_from_command_args(
            image, height_width_ratio, width_height_ratio, img_height, img_width
        )

    if ratio_setting:
        return resize_image_from_ratio(image, ratio_setting, args_list_setting)

    # Default case, no redimensionnal args have been used
    return image
