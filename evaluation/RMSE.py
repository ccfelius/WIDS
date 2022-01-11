# Submission file has format below:
# id,site_eui
# 75757,1.3
# 75758,2.8
import pandas as pd
import math
from pandas.core.indexes.base import InvalidIndexError

# example paths
path_train = "/Users/charlottefelius/documents/wids2022/WIDS/train.csv"
path_predicted = "/Users/charlottefelius/documents/wids2022/WIDS/sample_solution.csv"

# note that training data contains 75757 entries and sample solution 9705
# this will result in an inevitable error 

def evaluate(path_train, path_predicted):

    # Read and parse the site_eui col of training dataset
    data = pd.read_csv(path_train)

    # Extract site_eui and cast to list
    training_data = list(data["site_eui"])

    # Store length of training_data
    length = len(training_data)

    # Read submission file, extract site_eui and cast to list
    predicted = list(pd.read_csv(path_predicted)["site_eui"])

    # throw error if files are not equally long
    if length != len(predicted):
        raise IndexError("Invalid length; Lists are not equally long")
    
    # calculate RMSE
    aggregate = 0;

    # Iterate parallel through both lists
    for i, j in zip(training_data, predicted):
        aggregate += (i-j)**2

    RSME = math.sqrt((1/length)*aggregate)

    print(f"RSME Score is: {RSME}")

    return RSME

evaluate(path_train, path_predicted)
