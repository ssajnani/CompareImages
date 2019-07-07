import os, random
from analysis.feature_extractor import *
from analysis.matcher import Matcher

def compare_two_images(first_image_path, second_image_path):
    '''
        Compare two images by calling a batch feature extractor 
        followed by a image matcher
        @param first_image_path string
        @param second_image_path string
        @return match_number float
    '''
    #Second the second image for batch feature extraction
    files = [second_image_path]
    
    batch_extractor(files)
    #After feature is extracted read the pickle file that was written
    ma = Matcher('features.pck')
    
    #Match the features of the first image with the
    #features extracted from the second image
    names, match = ma.match(first_image_path)
    return match[0]

