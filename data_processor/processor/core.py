from tabulate import tabulate
import pandas as pd

def display_results():
    staged_file_path = "../../staged_data.csv"
    data = pd.read_csv(staged_file_path)

    print(tabulate(data, headers='keys', tablefmt='psql'))

if __name__ == "__main__":
    display_results()
