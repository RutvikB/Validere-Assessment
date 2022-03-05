from operator import index
import os
import pathlib
import numpy as np
import pandas as pd 
from utils.utils import load_config_dict, load_data
from utils.load_config_file import load_config_file

PATH_TO_CONFIG = pathlib.Path('config') / 'config.ini'

def main():
    """
    """
    config = load_config_file(config_path= PATH_TO_CONFIG)

    data = load_data(path= str(config['path_to_accidents_data']))

    data_copy = data.copy()

    # Drop unwanted features
    for col in list(data.columns):
        for feat in list(config['unwanted_features']):
            if feat.lower() in col.lower():
                data_copy.drop(columns=col, inplace= True)

    # Convert Date-Time Features
    date_time_cols = [col for col in data_copy.columns if col.lower().endswith(config['datetime_feat_ext'])]
    for col in date_time_cols:
        data_copy[col] = pd.to_datetime(data_copy[col])

    data_copy.to_csv("preprocessed_data.csv", index= False)
    print(data)

if __name__ == "__main__":
    main()