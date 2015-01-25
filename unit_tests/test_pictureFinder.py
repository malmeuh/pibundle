__author__ = 'benjamin'

import frameFinder
import frameGrabber

import os
import cv2

ref_pict_path = os.path.abspath("ref_picts")
test_pict_path = os.path.abspath("test_picts")

# Find and load all the reference pictures
ref_frame_source = frameGrabber.PictsFile(ref_pict_path)
ref_picts = ref_frame_source.get_pict_list()

test_frame_source = frameGrabber.PictsFile(test_pict_path)
test_picts = test_frame_source.get_pict_list()

# Test the finder
frame_finder = FrameFinder()
frameFinder.declare_ref_frames(ref_picts)

for pict in test_picts:
    frameFinder.find_pict_pose(pict)

