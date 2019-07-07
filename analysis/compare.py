import os, random
from analysis.feature_extractor import *
from analysis.matcher import Matcher

def compare_two_images(firstImagePath, secondImagePath):
    files = [secondImagePath]
    # getting 3 random images 
    
    batch_extractor(files)

    ma = Matcher('features.pck')
    
    s = firstImagePath
    names, match = ma.match(s)
    return match[0]

