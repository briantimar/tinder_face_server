import glob
import numpy as np
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_unlabeled_profile_picture():
    """ Returns an unlabeled profile picture. 
        Currently, just selects a test image at random. """
    choices = glob.glob(ROOT_DIR + "/static/*.jpg")
    name= choices[ np.random.choice(len(choices))].split('/')[-1]
    return "/static/"+name
