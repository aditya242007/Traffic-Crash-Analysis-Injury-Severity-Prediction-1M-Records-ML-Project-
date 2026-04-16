# Data Preprocessing Script

import pandas as pd

# Add your data preprocessing code here

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    # Example preprocessing steps
    data.dropna(inplace=True)
    return data
