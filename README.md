# Compare Pairs of Images Project

## Approach

1) Selected Python because it's one of the more modern and approachable languages when it comes to computer vision and image analysis.
2) Looked into the different types of image comparison. Found a stack overflow post that explained the difference between histogram comparison, template matching and feature matching. Feature matching seems to be more efficient because analysis can be carried out invariant to transformations. Source: https://stackoverflow.com/questions/11541154/checking-images-for-similarity-with-opencv 
3) Searched for feature matching image comparison using Python and found a Medium article describing a program that uses batch iamge feature extraction and compares one image to a set of images. The feature matching technique used is the KAZE feature matching algorithm. Used this as a base to begin the project and remove the batch feature extraction to compare images on a one-to-one basis. Source: https://medium.com/machine-learning-world/feature-extraction-and-similar-image-search-with-opencv-for-newbies-3c59796bf774
4) Researched feature matching algorithms other than KAZE, and found a research paper outlining the most useful feature matching algorithms. The two most popular and effective algorithms used are Speeded Up Robust Features (SURF) and Scale-Invariant Feature Transform (SIFT), because of their invariance to scale, rotate, translation, illumination, and blur. SURF is better than SIFT in rotation invariant, blur and warp transform. SURF is 3 times faster as such a compromise of speed was made by choosing SURF as the feature extraction algorithm of choice. Source:  https://www.researchgate.net/publication/314285930_Comparison_of_Feature_Detection_and_Matching_Approaches_SIFT_and_SURF
5) 
