import glob
import random
import os
import sys
import subprocess

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from tinderAPI.utils import get_all_photo_urls, save_image_from_url
from tinderAPI.tinder_api_sms import get_recommendations

UNLABELED_STATIC_DIR = os.path.join(ROOT_DIR , 'static', 'tinder_unlabeled')
LABELED_STATIC_DIR = os.path.join(ROOT_DIR, 'static', 'tinder_labeled')


def get_test_picture():
    """ selects a test image at random. """
    choices = glob.glob(ROOT_DIR + "/static/*.jpg")
    name= random.choice(choices).split('/')[-1]
    return "/static/"+name

def clear_tinder_unlabeled_static():
    """ Clear the static dir for unlabeled tinder images"""
    for image in os.listdir(UNLABELED_STATIC_DIR):
        os.remove(os.path.join(UNLABELED_STATIC_DIR, image))

def clear_tinder_labeled_static():
    """ Clear the static dir for labeled tinder images"""
    for image in os.listdir(LABELED_STATIC_DIR):
        os.remove(os.path.join(LABELED_STATIC_DIR, image))

def download_tinder_profile_pictures():
    """ Download a set of profile pics for a single tinder user, save them to static dir"""
    recs = get_recommendations()['results']

    clear_tinder_unlabeled_static()
    ### TODO this is a terrible hack 
    person = recs[0]
    urls = get_all_photo_urls(person, size=172)
    for i in range(len(urls)):
        save_image_from_url(urls[i], 
                            os.path.join(UNLABELED_STATIC_DIR, "img%d"%i))

def get_unlabeled_profile_picture():
    choices = os.listdir(UNLABELED_STATIC_DIR)
    name = random.choice(choices)
    return "/static/tinder_unlabeled/" + name


def generate_labeled_pictures():
    """ Populate the tinder labeled static directory .
    TODO this is terrible"""
    unlabeled = os.listdir(UNLABELED_STATIC_DIR)
    if len(unlabeled) == 0:
        raise ValueError("no unlabeled images found")
    subprocess.call(["sh", os.path.join(ROOT_DIR, "docker_run.sh"), 
                        os.path.join(ROOT_DIR, "generate_labeled_pictures.py")])
    
