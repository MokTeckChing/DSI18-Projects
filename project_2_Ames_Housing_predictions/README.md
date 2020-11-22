 ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2: Ames Housing Sale Price Prediction

### Problem Statement

A real estate company in Ames, Iowa, wants create an interactive webpage where potential clients could get a rough estimate of the sale price a house by entering a set of parameters.

The company is requresting for a regression model based on the Ames Housing Dataset that will predict the rough price of a house at sale, with no more than 25 features.

As a requirement, the company has set up a Kaggle competition, and requested that scores be submitted there as a measure of accuracy.

### Executive Summary

The Ames dataset consists of 2051 rows with 81 Columns, with a mix of Nominal, Ordinal and Scalar data. A data dictionary was provided along with the dataset to better explain the categoriacal variables. 

These set of notebooks aim to create a workable linear regression production model for the prediction of housing sale prices with 25 selected features.

Exploratory Data Analysis was done, revealing that some columns of the dataset contained high skews, missing values and errors. Further examiation revealed the presense of several colinear features. These factors were sense-made of and handled during data cleaning, and factor selection was performed.


### Data Dictionary

Refer to <a href = "http://jse.amstat.org/v19n3/decock/DataDocumentation.txt">here</a> for the data dictionary. 


### Conclusion

The final Ridge regression model has 25 Features and a mean RMSE of 23752 on unseen data. It's public and private kaggle scores were 28919.01006 and 30388.85877 respectively. 

The model was successfully built, but suffers from the limits imposed on the task (only linear regression, 25 features). The test scores designated by the company also exhibit discrepancies, and should be further examined.

