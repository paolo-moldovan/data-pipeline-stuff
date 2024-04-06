import pandas as pd

data = {
    "name": ["John", "Jane", "Steve", "Mary"],
    "surname": ["Doe", "Lee", "Smith", "Johnson"],
    "age": [28, 34, 45, 25]
}

df = pd.DataFrame(data)

csv_file_path = "../inputs/example_input_data.csv"

df.to_csv(csv_file_path, index=False)

csv_file_path
