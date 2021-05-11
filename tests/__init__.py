import os
from utils.file_utils import read_input as ri


def read_input(example):
    return ri(os.path.join('../examples', example))
