import json
import logging


def load_config_dict(config_path: str) -> dict:
    """
        Loads the config.ini file from the specified path, as a dictionary.
        Args:
            path_to_config_file: String containing path to Config file.
        Returns:
            dict: The config file in a dict format.
        """
    from configparser import ConfigParser

    config = ConfigParser()
    config.optionxform = str
    config.read(config_path)
    config_items = config.sections()
    if "DEFAULT" in config_items:
        config_items.remove("DEFAULT")

    config_dict = {}
    for item in config_items:
        config_dict.update({item: {}})
        for parameter, value in config[item].items():
            config_dict[item].update({parameter: value})

    return config_dict


def load_data(path: str):
    """ 
    Function to load the data in the specified path as a 
    Pandas DataFrame. 
    Args: 
        path: the path to the CSV or XLSX file. 
    Returns:
        A pandas DataFrame.
    """
    import pandas as pd

    if path.endswith(".csv"):
        try:
            data = pd.read_csv(path, na_filter=True)
        except Exception as e:
            print("Could not load CSV file data in the specified path.")
            data = pd.DataFrame(columns=["field_id", "year"])

    if path.endswith(".xlsx"):
        try:
            data = pd.read_excel(path, na_filter=True)
        except Exception as e:
            print("Could not load XLSX file data in the specified path.")
            data = pd.DataFrame(columns=["field_id", "year"])

    return data


def preprocess_phmsa_data(config_path: str):
    import pandas as pd
    from utils.load_config_file import load_config_file

    config = load_config_file(config_path=config_path)

    data = load_data(path=str(config["path_to_accidents_data"]))

    data_copy = data.copy()

    # Drop unwanted features
    for col in list(data.columns):
        for feat in list(config["unwanted_features"]):
            if feat.lower() in col.lower():
                data_copy.drop(columns=col, inplace=True)

    # Convert Date-Time Features
    date_time_cols = [
        col
        for col in data_copy.columns
        if col.lower().endswith(config["datetime_feat_ext"])
    ]
    for col in date_time_cols:
        data_copy[col] = pd.to_datetime(data_copy[col])

    # Make sure Latitude values are Positive as USA falls North of the equator
    data_copy[config["latitude_feature"]] = data_copy[config["latitude_feature"]].abs()

    # Make sure Longitude values are Negative as USA falls on the West of the Prime Meridian
    data_copy[config["longitude_feature"]] = (
        data_copy[config["longitude_feature"]].abs() * -1
    )

    data_copy.to_csv("preprocessed_data.csv", index=False)

    return data_copy

