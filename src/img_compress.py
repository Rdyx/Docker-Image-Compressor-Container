""" Image compression related function """

import settings
import utils


def get_image_compression_quality(
    compression_arg=settings.COMPRESSION_QUALITY_ARG,
    args_list_setting=settings.ARGS_LIST,
):
    """ Use compression quality user wants if set from arg, default to 50 """
    if compression_arg:
        return int(utils.get_arg_value(compression_arg, args_list_setting))
    return 65
