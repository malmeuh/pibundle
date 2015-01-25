__author__ = 'benjamin'

import sys
sys.path.insert(0, '../framework')

import frameFinder
import frameGrabber
import os
import time

ref_pict_path = os.path.abspath("ref_picts")
test_pict_path = os.path.abspath("test_picts")

# Find and load all the reference pictures
ref_frame_source = frameGrabber.PictsFile(ref_pict_path)
ref_picts = ref_frame_source.get_pict_list()

test_frame_source = frameGrabber.PictsFile(test_pict_path)
test_picts = test_frame_source.get_pict_list()

# Test the finder
frame_finder = frameFinder.FrameFinder()
frame_finder.declare_ref_frames(ref_picts)

for pict in test_picts:
    time_start = time.time()
    frame_finder.find_pict_pose(pict)
    time_stop = time.time()
    print "Took {:.2f} seconds to find".format(time_stop - time_start)

