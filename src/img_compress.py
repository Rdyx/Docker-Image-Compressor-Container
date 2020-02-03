""" Image compression related function """

import settings
import utils


def get_image_compression_quality(compression_arg=settings.COMPRESSION_QUALITY_ARG):
    """ Use compression quality user wants if set from arg, default to 65 """
    if compression_arg:
        return int(utils.get_arg_value(compression_arg))
    return 65
