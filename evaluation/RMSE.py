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

def evaluate(path_train, path_predicted):

    """
    Function for evaluating ML model by RMSE
    
    input: path of training dataset, path of predicted dataset
    output: RMSE

    """
    
    # Read and parse the site_eui col of training dataset
    data = pd.read_csv(path_train)

    # Extract site_eui and cast to list
    training_data = list(data["site_eui"])

    # Store length of training_data
    length = len(training_data)

    # Read submission file, extract site_eui and cast to list
    predicted = pd.read_csv(path_predicted)[["id", "site_eui"]]

    # Infer first and last ID of predicted data
    index_first = int(predicted.head(1).id)
    index_last = int(predicted.tail(1).id) + 1

    # Cast predicted to list
    predicted = list(predicted["site_eui"])

    # Take subset of training_set 
    training = training_data[index_first:index_last]

    # calculate RMSE
    aggregate = 0;

    # Iterate parallel through both lists
    for i, j in zip(training, predicted):
        aggregate += (i-j)**2

    RSME = math.sqrt((1/length)*aggregate)

    print(f"RSME Score is: {RSME}")

    return RSME

evaluate(path_train, path_predicted)
