""" Image redimension related function """

import sys

import settings
import utils


def get_new_dimensions(img, axis, arg, args_list, ratio):
    """ Calculated new image dimensions """
    wanted_axis_dimension = int(utils.get_arg_value(arg, args_list))
    new_calculated_axis_dimension = wanted_axis_dimension * ratio

    if axis == 'width':
        return img.resize([wanted_axis_dimension, int(new_calculated_axis_dimension)])
    return img.resize([int(new_calculated_axis_dimension), wanted_axis_dimension])


def resize_image_from_command_args(
        image, height_width_ratio, width_height_ratio, img_width, img_height,
        height_resize_setting, width_resize_setting, args_list_setting,
):
    """ Check used arguments and resize image depending on provided values """

    if (
        height_resize_setting and not width_resize_setting and
        img_height > int(utils.get_arg_value(height_resize_setting, args_list_setting))
    ):
        image = get_new_dimensions(
            image, 'height', height_resize_setting, args_list_setting, height_width_ratio
        )

    if (
        width_resize_setting and not height_resize_setting and
        img_width > int(utils.get_arg_value(width_resize_setting, args_list_setting))
    ):
        image = get_new_dimensions(
            image, 'width', width_resize_setting, args_list_setting, width_height_ratio
        )

    # In case of both args are set, first we will calculate from the longer axis
    # Then check if the other axis is matching the wanted value and recalculate if needed
    if height_resize_setting and width_resize_setting:
        # Re set image variable with image with new axis dimension
        # TODO check conditions in there, can't create bug but something looks weird
        if img_height > img_width:
            image = get_new_dimensions(
                image, 'height', height_resize_setting, args_list_setting, height_width_ratio
            )
        else:
            image = get_new_dimensions(
                image, 'width', width_resize_setting, args_list_setting, width_height_ratio
            )

        # Process the newly redimensionned image
        if img_width > int(utils.get_arg_value(width_resize_setting, args_list_setting)):
            return get_new_dimensions(
                image, 'width', width_resize_setting, args_list_setting, width_height_ratio
            )

        if img_height > int(utils.get_arg_value(height_resize_setting, args_list_setting)):
            return get_new_dimensions(
                image, 'height', height_resize_setting, args_list_setting, height_width_ratio
            )

    # If nothing matches, simply return image (Forcing resize for gif frames to get image from them)
    return image.resize([img_width, img_height])


def resize_image_from_ratio(img, ratio_arg, args_list):
    """ Resize image with a defined ratio directly """
    ratio = float(utils.get_arg_value(ratio_arg, args_list))

    return img.resize([int(img.size[0]*ratio), int(img.size[1]*ratio)])


def select_redimension_system(
    image, height_width_ratio, width_height_ratio, img_width, img_height,
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
            image, height_width_ratio, width_height_ratio, img_width, img_height,
            height_resize_setting, width_resize_setting, args_list_setting,
        )

    if ratio_setting:
        return resize_image_from_ratio(image, ratio_setting, args_list_setting)

    # Default case, no redimensionnal args have been used
    # (Forcing resize for gif frames to get image from them)
    return image.resize([img_width, img_height])
