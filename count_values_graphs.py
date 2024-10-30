#Script updated 30.10.2024

import pandas as pd
import matplotlib.pyplot as plt

df_in = pd.read_csv('cer_wer_invalidated.csv', encoding='utf-8')
count_zeros_in = (df_in['cer'] == 0).sum()

df_val = pd.read_csv('cer_wer_validated.csv', encoding='utf-8')
count_zeros_val = (df_val['cer'] == 0).sum()


# Plot CER invalidated
# Load the CSV file
df = pd.read_csv('cer_wer_invalidated.csv')

# Replace 'column_name' with the name of the column containing values from 0 to 1
column_name = 'cer'

# Create a new Series with the rounded values, without changing the original data
rounded_values = df[column_name].round(1)

# Plot the histogram of the rounded values
plt.figure(figsize=(10, 6))
rounded_values.value_counts(sort=False).sort_index().plot(kind='bar')

# Adding labels and title
plt.xlabel('Rounded Values')
plt.ylabel('Count')
plt.title(f'Count of Values in {column_name}: invalidated')

# Show the plot

plt.savefig('count_invalidated_cer.png')

plt.show()

# Plot CER validated
# Load the CSV file
df1 = pd.read_csv('cer_wer_validated.csv')

# Replace 'column_name' with the name of the column containing values from 0 to 1
column_name = 'cer'

# Create a new Series with the rounded values, without changing the original data
rounded_values1 = df1[column_name].round(1)

# Plot the histogram of the rounded values
plt.figure(figsize=(10, 6))
rounded_values1.value_counts(sort=False).sort_index().plot(kind='bar')

# Adding labels and title
plt.xlabel('Rounded Values')
plt.ylabel('Count')
plt.title(f'Count of Values in {column_name}: validated')

# Show the plot

plt.savefig('count_validated_cer.png')

plt.show()

# Plot WER invalidated
# Load the CSV file
df = pd.read_csv('cer_wer_invalidated.csv')

# Replace 'column_name' with the name of the column containing values from 0 to 1
column_name = 'wer'

# Create a new Series with the rounded values, without changing the original data
rounded_values = df[column_name].round(1)

# Plot the histogram of the rounded values
plt.figure(figsize=(10, 6))
rounded_values.value_counts(sort=False).sort_index().plot(kind='bar')

# Adding labels and title
plt.xlabel('Rounded Values')
plt.ylabel('Count')
plt.title(f'Count of Values in {column_name}: invalidated')

# Show the plot

plt.savefig('count_invalidated_wer.png')

plt.show()

# Plot WER validated
# Load the CSV file
df = pd.read_csv('cer_wer_validated.csv')

# Replace 'column_name' with the name of the column containing values from 0 to 1
column_name = 'wer'

# Create a new Series with the rounded values, without changing the original data
rounded_values = df[column_name].round(1)

# Plot the histogram of the rounded values
plt.figure(figsize=(10, 6))
rounded_values.value_counts(sort=False).sort_index().plot(kind='bar')

# Adding labels and title
plt.xlabel('Rounded Values')
plt.ylabel('Count')
plt.title(f'Count of Values in {column_name}: validated')

# Show the plot

plt.savefig('count_validated_wer.png')

plt.show()
