def load_config_file(config_path: str) -> dict:
    """
    Returns the config file loaded from the specified path, as a dictionary.
    """
    import configparser
    import pathlib
    converters = {
        "list_int": lambda x: [int(i.strip()) for i in x.split(",")],
        "int_none": lambda x: None if x.lower() == "none" else int(x),
        "list_str": lambda x: [i.strip() for i in x.split(",")],
        "pathlib": lambda x: pathlib.Path(x),
    }

    config_data = configparser.ConfigParser(converters=converters)
    config_data.read(config_path)
    config_file = {}

    # Paths config
    section = "paths"
    config_file["path_to_accidents_data"] = config_data.getpathlib(
        section, "path_to_accidents_data"
    )

    # Preprocessing config
    section = 'preprocessing'
    config_file['unwanted_features'] = config_data.getlist_str(
        section, 'unwanted_features'
    )
    config_file['datetime_feat_ext'] = config_data.get(
        section, 'datetime_feat_ext'
    )

    return config_file