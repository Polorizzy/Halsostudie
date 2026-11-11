import pandas as pd
from pathlib import Path

def load_data():
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "Data" / "health_data.csv"

    df = pd.read_csv(file_path)
    return df