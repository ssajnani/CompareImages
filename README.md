# Compare Pairs of Images Project

## Approach

1) Selected Python because it's one of the more modern and approachable languages when it comes to computer vision and image analysis.
2) Looked into the different types of image comparison. Found a stack overflow post that explained the difference between histogram comparison, template matching and feature matching. Feature matching seems to be more efficient because image comparison can be carried out invariant to transformations. Source: https://stackoverflow.com/questions/11541154/checking-images-for-similarity-with-opencv 
3) Searched for feature matching image comparison using Python and found a Medium article describing a program that uses batch iamge feature extraction and compares one image to a set of images. The feature matching technique used is the KAZE feature matching algorithm. Used this as a base to begin the project and remove the batch feature extraction to compare images on a one-to-one basis. Source: https://medium.com/machine-learning-world/feature-extraction-and-similar-image-search-with-opencv-for-newbies-3c59796bf774
4) Researched feature matching algorithms other than KAZE, and found a research paper outlining the most useful feature matching algorithms. The two most popular and effective algorithms used are Speeded Up Robust Features (SURF) and Scale-Invariant Feature Transform (SIFT), because of their invariance to scale, rotate, translation, illumination, and blur. SURF is better than SIFT in rotation invariant, blur and warp transform. SURF is 3 times faster as such a compromise of speed was made by choosing SURF as the feature extraction algorithm of choice. Source:  https://www.researchgate.net/publication/314285930_Comparison_of_Feature_Detection_and_Matching_Approaches_SIFT_and_SURF

SURF gathers features based on gradients and the defining gradients of the image are collected as key points as described in the diagram below:

![](images/feature_extraction.jpeg)

5) One class and four python module files were created. 
>>  * The most critical module was the **feature_extractor** which has a function that generates a numpy array of extracted features gathered from an image file using the SURF algorithm. 
>>  * The **Matcher** class can be used to instantiate an object with an image and its feature vector using the **feature_extractor** module. Once instantiated, the Matcher can then be used to perform a match operation on the object's self vector with the features of another image provided. The match operation is a comparison of cosine distance or distance between the points in the image vectors.
>>  * The **compare** module has a function that is used to initialize a **Matcher** object and perform a match, returning the cosine distance as a similarity value. 
>>  * The **parse_analyze** module has a function that reads in an input csv row by row takes the two values in each row and performs a compare operation using the **compare** module, the elapsed time for comparison is recorded, the output is written in an output csv. It is important to note that the output csv is updated row by row so if the input csv is N values large, the user can expect the output to be output incrementally over time, instead of at the end of the processing. 
>>  * This **parse_analyze** function is the called in the **main** module which acts as the command line argument parser for the program.  



