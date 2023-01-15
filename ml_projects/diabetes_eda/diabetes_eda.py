import codecademylib3
import pandas as pd
import numpy as np

# code goes here
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())

#number of features
print(len(diabetes_data.columns))

#number of observations
print(len(diabetes_data))

#check for null values
print(diabetes_data.isnull().sum())
# print(diabetes_data.info())

#summary statistics
print(diabetes_data.describe())

#clean data
diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.nan)

#check for null values
print(diabetes_data.isnull().sum())
print(diabetes_data.info())

#investigate missing data
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

#check the datatypes of each variable
print(diabetes_data.dtypes)

#dig deeper on the Outcome variable. The values look fishy
print(diabetes_data.Outcome.unique())

#fix the outcome values, replace the O's with 0s and change the datatype to int
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O', 0)
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype('int64')
print(diabetes_data.dtypes)


