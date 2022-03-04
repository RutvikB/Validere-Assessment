import os
import pathlib
import numpy as np
import pandas as pd 


def main():
    """
    """
    data = pd.read_csv("data/database.csv")

    print(data)

if __name__ == "__main__":
    main()