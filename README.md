# DATA-MINING-FOR-HUMAN-MOVEMENT-CLASSIFICATION-FROM-SENSOR-DATA

## Executive Summary

### Task Outline and the Dataset


The Bremen Big Data Challenge 2019 was to classify various human movements which included everyday movements and athletic movements. The Organisers provided all competing groups with sensor data recorded on one leg above and below the knee. The training data set on which each team had to train their classifier contained sensor data collected from 15 subjects. Data collected from four other subjects were used by the organisers as test dataset to evaluate the solutions provided by each participating team.\\\\For each of the subjects in both the training and the test dataset, participants were provided with data files containing the sensor reading data for various activities. One, particular activity is represented by data in a single data file where each line of the data file corresponds to the 19 sensor values measured at one time. Each sensor value is sampled at 1000 Hz which leads each column of the data file to represent a time series sensor value recording. 

### Method of Approach
The objective of our work in the Bremen Big Data Challenge is to find an optimal classifier to classify human activities based on the sensor readings provided to us. This optimal classifier, must be able to generalize its learning in the test data set with the smallest miss-classification rate we can achieve. With this goal set, our method of approach includes implementation of a full processing pipeline starting with feature extraction followed by using tree-based method for classification with subsequent steps where we also attempt to improve the performance of the classifier by careful filtration/selection of useful features and parameter tuning using Cross-Validation.

### Result
After completing the data processing pipeline and training the classifier, the classifier was used to predict the activities present in the test dataset. After each run of training and predicting, the predictions were submitted to the organisers for performance evaluation of the classifier.
Among the different models we trained, the best model has an prediction accuracy of 89.35\%.
