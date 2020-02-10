#Prediction model for Happiness Index

##Introduction
Happiness_2019.csv Dataset is chosen to be trained upon and calculate Happiness Index using different
machine Learning techniques and Data Models.


##Dependencies
Python, Microsoft Azure Machine Learning Studio, Postman, C#

##Files:

There are 4 files in the folder.
happiness.py:
Deployed on the Azure web services, happiness is the request response code.
The following includes the data which is read first,summarized next. 
Further it is normalised and trained.


happiness_filtered.py:
It is the Deployed file which includes filtered data without the redundant categories and numerical value of data
on which Linear Regression Algorithms are applied and the model is trained in order to achieve the Happiness index
or " resultant score".
The purpose of this file is to operate on the cleanesty dataset possible.

Permutation_model.py:
The pupose of this file is to train the data such that effect of each Variable in the dataset is known by percentage.
And the Model is trained as accurately as possible

Training model for Happiness(Predictive):
Connected to Azure API,
This file works on a sample data set, and it is used to 
1) Depict Tablular Data set
2)Calculate "Resultant score" or the Happiness Index Accurately.
