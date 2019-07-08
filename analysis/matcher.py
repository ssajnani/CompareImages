
import numpy as np
from analysis.feature_extractor import *
import scipy.spatial
class Matcher(object):
    '''Matcher class

    Used to generate feature vector data for an image file 
    and to compare the cosine distance between this vector data 
    and vector data of another image.

    ''' 

    def __init__(self, file_path):
        '''
        Initializes the class
        @param pickled_db_path string
        Performs a feature extraction of the file_path parameter
        and generates a vector of feature data for the 
        Matcher object
        '''
        self.matrix = []
        features = extract_features(file_path)
        self.matrix.append(features)

    def cos_cdist(self, vector):
        '''
        Calculates cosine distance
        @param vector numpyArray
        @return float
        Takes a vector and calculates the cosine distance 
        between the parameter vector and the self vector 
        '''
        # getting cosine distance between search image and images database
        v = vector.reshape(1, -1)
        return scipy.spatial.distance.cdist(self.matrix, v, 'cosine').reshape(-1)

    def match(self, image_path, topn=1):
        '''
        Matches an image to another image using cosine distance
        @param image_path string
        @param topn int (number of matches found in the pickle file since 
        we are looking for the highest match we set this to 1)
        @return tuples of image paths and image distances
        Takes a vector and calculates the cosine distance 
        between the parameter vector and the self vector 
        '''
        features = extract_features(image_path)
        img_distances = self.cos_cdist(features)
        # getting top 1 records
        nearest_ids = np.argsort(img_distances)[:topn].tolist()

        return img_distances[nearest_ids].tolist()[0]
