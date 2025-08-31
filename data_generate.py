import pandas as pd
import os

# CREATE DEFAULT DATAFRAME
data = {'Vorname': ['Jürgen', 'Danilo', 'Marcel'],
    'Alter': [16, 10, 20],
    'Stadt': ['Frankfurt', 'München', 'Berlin']
}

df = pd.DataFrame(data)

# Adding new row for second version of data
new_row = {'Vorname': 'Sudarshan', 'Age': 11, 'Stadt': 'Ingolstadt'}
df.loc[len(df.index)] = new_row

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, "info.csv")

df.to_csv(file_path, index=False)

print(f"CSV file created and stored at location {file_path}")



