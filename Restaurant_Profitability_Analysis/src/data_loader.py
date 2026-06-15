import pandas as pd

def load_data(file_path):
    """
    Load restaurant dataset
    """
    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    df = load_data("data/restaurant_data.csv")

    print("Dataset Loaded Successfully")
    print(df.head())
    print("\nShape:", df.shape)