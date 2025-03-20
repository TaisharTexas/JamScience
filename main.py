import os
import pandas as pd

# Path to dataset (update based on extracted files)
DATASET_DIR = os.path.expanduser("~/.cache/kagglehub/datasets/robikscube/flight-delay-dataset-20182022/versions/4")

# List available files
files = os.listdir(DATASET_DIR)
print(f"Available dataset files: {files}")

# Example: Load a CSV file (change filename accordingly)
csv_file = next((f for f in files if f.endswith('.csv')), None)
if csv_file:
    df = pd.read_csv(os.path.join(DATASET_DIR, csv_file))
    print(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns")
else:
    print("No CSV files found in dataset directory.")