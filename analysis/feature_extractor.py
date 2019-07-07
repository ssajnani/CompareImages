import cv2
import numpy as np
import scipy
from imageio import imread
import _pickle as cPickle
import random
import os
import matplotlib.pyplot as plt
import pickle

''' Feature extractor
@param image_path string
@param vector_size int
@return numpy matrix of features
'''
def extract_features(image_path, vector_size=32):
    try:
        image = imread(image_path, pilmode="RGB")
        # Using SURF because it has been demostrated as it is among the best feature detectors: 
        # https://www.researchgate.net/publication/314285930_Comparison_of_Feature_Detection_and_Matching_Approaches_SIFT_and_SURF
        alg = cv2.xfeatures2d.SURF_create(400)
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print('Error: ', e)
        return None
    except Exception as e:
        print('Error: ', e)
        return None

    return dsc


''' Feature extractor
@param image_path string
@param vector_size int
@return numpy matrix of features
'''
def batch_extractor(images_path, pickled_db_path="features.pck"):
    result = {}
    for f in images_path:
        print('Extracting features from image %s' % f)
        name = f.split('/')[-1].lower()
        result[name] = extract_features(f)
    
    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)
