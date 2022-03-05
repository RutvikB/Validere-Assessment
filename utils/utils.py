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
        if 'DEFAULT' in config_items:
            config_items.remove('DEFAULT')

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
            data = pd.DataFrame(columns=['field_id', 'year']) 
    
    if path.endswith(".xlsx"): 
        try: 
            data = pd.read_excel(path, na_filter=True) 
        except Exception as e: 
            print("Could not load XLSX file data in the specified path.") 
            data = pd.DataFrame(columns=['field_id', 'year']) 
            
    return data


