from preprocess_da import (
    Read_data_file,
    Drop_unnecessary_features,
    Check_data_type
)
from config import COLS_TO_DROP



file_path = input("Enter CSV file path: ")

df = Read_data_file(file_path)

if df is not None:

    print("\nOriginal Dataset:")
    print(df.head())

    print("\nData Type Report:")
    print(Check_data_type(df))

    df = Drop_unnecessary_features(df, COLS_TO_DROP)

    print("\nDataset After Removing Unnecessary Features:")
    print(df.head())