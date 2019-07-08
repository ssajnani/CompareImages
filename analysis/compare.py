import os, random
from analysis.feature_extractor import *
from analysis.matcher import Matcher

def compare_two_images(first_image_path, second_image_path):
    '''
        Compare two images using the matcher 
        followed by a image matcher
        @param first_image_path string
        @param second_image_path string
        @return match_number float
    '''
    #Pass second image path as a parameter,
    # Matcher initalizes the feature extraction of the second image
    ma = Matcher(second_image_path)
    
    #Match the features of the first image with the
    #features extracted from the second image
    match = ma.match(first_image_path)
    return match

