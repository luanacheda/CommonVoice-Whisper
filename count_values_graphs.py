#Script updated 29.01.2025

import pandas as pd
import matplotlib.pyplot as plt

# df_in = pd.read_csv('cer_wer_invalidated.csv', encoding='utf-8')
# count_zeros_in = (df_in['cer'] == 0).sum()
#
# df_val = pd.read_csv('cer_wer_validated.csv', encoding='utf-8')
# count_zeros_val = (df_val['cer'] == 0).sum()

def figure(xer, set, filename):
    # Plot CER invalidated
    # Load the CSV file
    df = pd.read_csv(filename)

    # Replace 'column_name' with the name of the column containing values from 0 to 1
    column_name = xer

    # Categorize values
    df['rounded_values'] = df[column_name].apply(
        lambda x: 0.0 if x == 0 else (0.1 if 0 < x <= 0.05 else round(x, 1)))

    # Count occurrences
    value_counts = df['rounded_values'].value_counts(sort=False).sort_index()

    # Plot the histogram
    plt.figure(figsize=(10, 6))
    ax = value_counts.plot(kind='bar')

    # Adding labels and title
    plt.xlabel('Rounded Values')
    plt.ylabel('Count')
    plt.title(f'Count of Values in {column_name}: {set}')

    for p in ax.patches:
        ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='bottom')

    # Show the plot

    plt.savefig(f'count_{set}_{xer}.png')

    plt.show()


figure("cer","invalidated", "cer_wer_invalidated.csv")
figure("cer","validated", "cer_wer_validated.csv")
figure("wer","invalidated", "cer_wer_invalidated.csv")
figure("wer","validated", "cer_wer_validated.csv")

