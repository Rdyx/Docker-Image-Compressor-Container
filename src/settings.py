""" img_kompressor config """

import os
import sys

import utils

ARGS_LIST = sys.argv
IMG_FILE_FORMATS = ['jpg', 'jpeg', 'png', 'gif']
# IMG_FILE_FORMATS = ['gif']

CURRENT_DIRECTORY = os.getcwd()
IMG_INPUT_DIRECTORY = CURRENT_DIRECTORY + '/input/'
IMG_OUTPUT_DIRECTORY = CURRENT_DIRECTORY + '/output/'

# Verbose mode activation, remove -verbose from command to hide output informations
VERBOSE_ARG = utils.get_command_arg('--verbose', ARGS_LIST)
# Enforcing size argument
HEIGHT_RESIZE_ARG = utils.get_command_arg('--max-height', ARGS_LIST)
# Enforcing size argument
WIDTH_RESIZE_ARG = utils.get_command_arg('--max-width', ARGS_LIST)
# Compression quality argument
COMPRESSION_QUALITY_ARG = utils.get_command_arg('--quality', ARGS_LIST)
# Image ratio argument
RATIO_ARG = utils.get_command_arg('--ratio', ARGS_LIST)
