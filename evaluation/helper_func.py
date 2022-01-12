import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def missing_data(dataframe):
    
    """
    
    Method for calculating missing data
    input: dataframe
    output: sorted list (descending) with colname, #missing values and percentage of total values
    
    """
    
    length = len(dataframe)
    missing = []
    
    for column in dataframe.columns:
        difference = length - dataframe[column].count()
        
        if difference > 0:
            missing.append((column, difference, str('{0:.2f}'.format(difference/length*100)) +"%"))
    
    missing.sort(key = lambda x: x[1], reverse=True)
    
    return missing



def get_correlation(dataframe, colname, min_corr = 0.1):

    
    """
    
    Checks the correlations from a column with all other columns
    input: column name -> string, min_corr -> float
    output: Ordered list with correlations
    
    """
    
    print(f"Correlations of '{colname}':")
    
    correlations = []

    for i, j in dataframe.corr()[colname].iteritems():
        if abs(j) > min_corr:
            correlations.append((i, abs(j)))

    correlations.sort(key = lambda x: x[1], reverse=True)
    
    return correlations