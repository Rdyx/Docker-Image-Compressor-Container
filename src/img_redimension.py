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
        image, height_width_ratio, width_height_ratio, img_height, img_width
):
    """ Check used arguments and resize image depending on provided values """

    if settings.HEIGHT_RESIZE_ARG and not settings.WIDTH_RESIZE_ARG:
        return get_new_dimensions(
            image, 'height', settings.HEIGHT_RESIZE_ARG, settings.ARGS_LIST, height_width_ratio
        )

    if settings.WIDTH_RESIZE_ARG and not settings.HEIGHT_RESIZE_ARG:
        return get_new_dimensions(
            image, 'width', settings.WIDTH_RESIZE_ARG, settings.ARGS_LIST, width_height_ratio
        )

    # In case of both args are set, first we will calculate from the longer axis
    # Then check if the other axis is matching the wanted value and recalculate if needed
    if settings.HEIGHT_RESIZE_ARG and settings.WIDTH_RESIZE_ARG:
        if img_height > img_width:
            image = get_new_dimensions(
                image, 'height', settings.HEIGHT_RESIZE_ARG, settings.ARGS_LIST, height_width_ratio
            )
        else:
            image = get_new_dimensions(
                image, 'width', settings.WIDTH_RESIZE_ARG, settings.ARGS_LIST, width_height_ratio
            )

        if image.size[0] > int(utils.get_arg_value(settings.WIDTH_RESIZE_ARG, settings.ARGS_LIST)):
            return get_new_dimensions(
                image, 'width', settings.WIDTH_RESIZE_ARG, settings.ARGS_LIST, width_height_ratio
            )

        return get_new_dimensions(
            image, 'height', settings.HEIGHT_RESIZE_ARG, settings.ARGS_LIST, height_width_ratio
        )

    # If nothing matches, simply return image
    return image


def resize_image_from_ratio(img, ratio_arg, args_list):
    """ Resize image with a defined ratio directly """
    ratio = float(utils.get_arg_value(ratio_arg, args_list))

    return img.resize([int(img.size[0]*ratio), int(img.size[1]*ratio)])


def select_redimension_system(image, height_width_ratio, width_height_ratio, img_height, img_width):
    """ Select which redimension system will be used based on arguments provided in command """

    # Prevent user from using ratio calculation + max size value
    if (
            (settings.HEIGHT_RESIZE_ARG and settings.RATIO_ARG) or
            (settings.WIDTH_RESIZE_ARG and settings.RATIO_ARG)
    ):
        sys.stdout.write(
            'Warning ! Don\'t use --ratio and --max-height or --max-width at same time.\n'
        )
        sys.stdout.flush()
        return sys.exit(1)

    if settings.HEIGHT_RESIZE_ARG or settings.WIDTH_RESIZE_ARG:
        return resize_image_from_command_args(
            image, height_width_ratio, width_height_ratio, img_height, img_width
        )

    if settings.RATIO_ARG:
        return resize_image_from_ratio(
            image, settings.RATIO_ARG, settings.ARGS_LIST
        )

    # Default case, no redimensionnal args have been used
    return image
