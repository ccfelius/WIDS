import pandas as pd
import math
import sys
from pandas.core.indexes.base import InvalidIndexError

# example paths
path_train = "/Users/charlottefelius/documents/wids2022/WIDS/train.csv"
path_predicted = "/Users/charlottefelius/documents/wids2022/WIDS/sample_solution.csv" 

def evaluate(path_train, path_predicted, index_first = 0, index_last = 0, random=True):

    """
    Function for evaluating ML model by RMSE
    
    input: path of training dataset, path of predicted dataset
    output: RMSE

    """

    # Read training dataset
    data = pd.read_csv(path_train)

    # Extract site_eui and cast to list
    training_data = list(data["site_eui"])

    # Throw error if invalid indices
    if index_first < 0 or index_last < 0:
        raise InvalidIndexError("Negative index")
    if index_first > index_last:
        raise InvalidIndexError("Indices are reversed")
    elif index_last > length:
        raise InvalidIndexError("Index out of bounds")

    # Read submission file, extract id and site_eui 
    predicted = pd.read_csv(path_predicted)[["id", "site_eui"]]

    # Store length of training dataset
    length = len(predicted)

    # define aggregate
    aggregate = 0;

    if random==False:

        # Infer first and last ID of predicted data
        if index_first == 0 and index_last == 0:
            index_first = int(predicted.head(1).id)
            index_last = int(predicted.tail(1).id)

        # Cast predicted to list
        predicted = list(predicted["site_eui"])

        # Take subset of training_set 
        training = training_data[index_first:index_last]

        # Iterate parallel through both lists 
        for i, j in zip(training, predicted):

            # calculate square of difference between each entry and sum
            aggregate += (i-j)**2
        
    else:

        for id_, value in predicted.iterrows():

            aggregate += (training_data[id_]-value)**2

    RMSE = math.sqrt((1/length)*aggregate)

    print(f"RMSE Score is: {RMSE}")

    return RMSE

# Testcases
# evaluate(path_train, path_predicted, 0, 99999999999)
