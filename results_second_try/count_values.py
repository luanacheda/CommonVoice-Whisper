import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('cer_wer_invalidated.csv', encoding='utf-8')
count_zeros_in = (df['wer'] == 0).sum()

df = pd.read_csv('cer_wer_validated.csv', encoding='utf-8')
count_zeros_val = (df['wer'] == 0).sum()

print(count_zeros_val)
print(count_zeros_in)


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

plt.savefig('count_invalidated.png')

plt.show()


# Load the CSV file
df1 = pd.read_csv('cer_wer_validated.csv')

# Replace 'column_name' with the name of the column containing values from 0 to 1
column_name = 'wer'

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

plt.savefig('count_validated.png')

plt.show()

