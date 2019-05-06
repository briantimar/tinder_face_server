import os 
import numpy as np
import cv2

from faces.utils import *

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
source_dir = os.path.join("static", "tinder_unlabeled")
target_dir = os.path.join("static", "tinder_labeled")

names = os.listdir(source_dir)
ims = [ get_bgr_img(os.path.join(source_dir, name)) for name in names]

rgb_ims = [bgr_to_rgb(im) for im in ims]

align, net = get_align_and_net()
brs = [pull_boxes_and_reps(im,align,net) for im in rgb_ims]

reps_only = [[face['rep'] for face in im] for im in brs]
common_rep_indices = locate_common_reps(reps_only, keep_all_singles=True)
for i in range(len(ims)):
        if common_rep_indices[i] is None:
            labeled_im = ims[i]
        else:
            user_face = brs[i][common_rep_indices[i]]
            labeled_im = annotate_image(ims[i], user_face['box'])
        cv2.imwrite(os.path.join(target_dir, names[i]), labeled_im)
