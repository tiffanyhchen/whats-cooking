import csv
import pandas as pd

# Convert File to CSV
df = pd.read_json('train.json')
df.to_csv('training_data.csv')

# Clean CSV File
data = []
with open('training_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        ingredients = row[3].strip("[]").replace("'", "")
        row[3] = ingredients
        data.append(row)

with open('training_data.csv', 'w') as f:
    # Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerows(data)

