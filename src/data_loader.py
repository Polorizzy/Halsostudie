import pandas as pd

def load_data():
    df = pd.read_csv("data/health_data.csv")
    return df