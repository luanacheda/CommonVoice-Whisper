import os
import shutil
import pandas as pd

''' This program take 1000 mp3 files form the 'clips' folder randomly (based on the invalidated.tsv file) and producs a new folder containg these 1000 rand files'''

# Define the file paths and folder paths
tsv_file_path = 'invalidated.tsv'  # replace with the path to your TSV file
clips_folder_path = 'clips'  # replace with the path to your folder containing the mp3 files
destination_folder_path = 'invalidated_10_prova'  # replace with the path to the destination folder

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder_path, exist_ok=True)

# Read the TSV file
df = pd.read_csv(tsv_file_path, sep='\t')

# Randomly sample rows
sampled_df = df.sample(n=1000)  # Change `n` to the number of rows you want to sample, e.g., 1000

# Initialize a counter for the number of files copied
file_count = 0

# Iterate over the 'path' column in the sampled DataFrame
for path_value in sampled_df["path"]:
    # Construct the full path of the source file
    source_file_path = os.path.join(clips_folder_path, os.path.basename(path_value))

    if os.path.isfile(source_file_path):
        # Copy the file to the destination folder
        shutil.copy(source_file_path, destination_folder_path)
        file_count += 1

# Print the number of files copied
print(f'{file_count} mp3 files have been copied to {destination_folder_path}')
