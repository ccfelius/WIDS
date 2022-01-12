from evaluation import RMSE
import sys

# In terminal, run by:
# python run.py filename_training_data filename_predicted_data

RMSE.evaluate(sys.argv[1], sys.argv[2])