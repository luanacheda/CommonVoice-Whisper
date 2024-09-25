import os
import shutil
import pandas as pd

# Define the file paths and folder paths
tsv_file_path = 'validated.tsv'  # replace with the path to your TSV file
clips_folder_path = 'clips_prova'  # replace with the path to your folder containing the mp3 files
destination_folder_path = 'validated'  # replace with the path to the destination folder

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder_path, exist_ok=True)

# Read the TSV file
df = pd.read_csv(tsv_file_path, sep='\t')

# Randomly sample 1000 rows
sampled_df = df.sample(n=5)  # Setting random_state ensures reproducibility


new_directory = 'clips_prova'

# Iterate over the 'path' column in the TSV file
for path_value in df.sample["path"]:

    new_path = os.path.join(new_directory, os.path.basename(path_value))

    if os.path.isfile(new_path):
        # Copy the file to the destination folder
        shutil.copy(new_path, destination_folder_path)




print(f'{file_count} mp3 files have been copied to {destination_folder_path}')
