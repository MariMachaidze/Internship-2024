import pandas as pd

# File path
file_path = 'path_to_save_file.csv'

# Sample rows data generator
def generate_rows():
    for i in range(1, 6):
        yield {'Column1': i, 'Column2': chr(64 + i)}  # Example data

# Function to save a DataFrame row by row
def save_row_to_csv(row, file_path):
    df = pd.DataFrame([row])
    with open(file_path, 'a') as f:
        df.to_csv(f, header=f.tell()==0, index=False)

# Iterate through the row data and save each row
for row in generate_rows():
    save_row_to_csv(row, file_path)

print("All rows saved to CSV file.")
