__author__ = 'benjamin'

"""
Created on Thu Dec 26 15:17:59 2013

@author: benjamin lefaudeux

Find a picture position compared to a given landscape
"""

import cv2


class FrameFinder:
    _ref_frames = 0
    _poses = []
    _ref_pictures = []

    def __init__(self):
        self._ref_frames = 0
        self._poses = []
        self._ref_pictures = []

    def declare_ref_frames(self, picture_list):
        # Declare all the reference pictures, and their pose
        self._ref_pictures = picture_list
        print("Now {} reference pictures".format(len(picture_list)))

    def find_pict_pose(self, new_pict):
        #  Stupid first try : go through all of the pictures and compute a first ressemblance score
        best_match_index = 0
        best_match_score = 0
        index = 0

        for pict in _ref_pictures:
            score = self.compute_rough_score(pict, new_pict)
            if score > best_match_score:
                best_match_score = score
                best_match_index = index

            index += 1

        print("Found a match in picture {}".format(best_match_index))

        return best_match_index

    @staticmethod
    def compute_rough_score( pict1, pict2):
        return cv2.matchTemplate(pict1, pict2, method=cv2.TM_CCORR)