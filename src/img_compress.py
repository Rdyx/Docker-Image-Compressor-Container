""" Image compression related function """

import settings
import utils


def get_image_compression_quality():
    """ Use compression quality user wants if set from arg, default to 50 """
    compression_arg = settings.COMPRESSION_QUALITY_ARG

    if compression_arg:
        return int(utils.get_arg_value(compression_arg, settings.ARGS_LIST))
    return 65
