import os
from utils.file_utils import read_input as ri


def read_input(example):
    if 'tests' in os.getcwd():
        return ri(os.path.join('../examples', example))
    else:
        return ri(os.path.join('examples', example))
