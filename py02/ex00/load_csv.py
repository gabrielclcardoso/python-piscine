import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Loads csv file and prints its shape and content.
    in case of an error returns None
    """

    try:
        data = pd.read_csv(path)
    except Exception as e:
        print(f"Error: {e}")
        return None

    print(f"Loading dataset of dimenstions {data.shape}")
    return data


# def main():
#     print(load("life_expectancy_years.csv"))
#
#
# if __name__ == "__main__":
#     main()
