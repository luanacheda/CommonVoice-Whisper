import pandas as pd
import numpy as np
from typing import List
import nltk
from nltk.tokenize import word_tokenize


def wer(reference: List[str], hypothesis: List[str]) -> float:
    """Compute the Word Error Rate (WER) between a reference and a hypothesis."""
    r = len(reference)
    h = len(hypothesis)

    # Initialize the distance matrix
    dp = np.zeros((r + 1, h + 1), dtype=int)

    for i in range(r + 1):
        dp[i][0] = i
    for j in range(h + 1):
        dp[0][j] = j

    for i in range(1, r + 1):
        for j in range(1, h + 1):
            cost = 0 if reference[i - 1] == hypothesis[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                           dp[i][j - 1] + 1,  # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution

    return dp[r][h] / float(r) if r > 0 else 0.0


def cer(reference: List[str], hypothesis: List[str]) -> float:
    """Compute the Character Error Rate (CER) between a reference and a hypothesis."""
    # Join the lists of characters into single strings
    reference_join = "".join(reference)
    hypothesis_join = "".join(hypothesis)

    r = len(reference_join)
    h = len(hypothesis_join)

    # Initialize the distance matrix
    dp = np.zeros((r + 1, h + 1), dtype=int)

    for i in range(r + 1):
        dp[i][0] = i
    for j in range(h + 1):
        dp[0][j] = j

    for i in range(1, r + 1):
        for j in range(1, h + 1):
            cost = 0 if reference_join[i - 1] == hypothesis_join[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                           dp[i][j - 1] + 1,  # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution

    return dp[r][h] / float(r) if r > 0 else 0.0



# Load TSV and CSV files into DataFrames
golden_standard_df = pd.read_csv('invalidated.tsv', sep='\t', encoding='utf-8')
whisper_df = pd.read_csv('transcriptions_large_10_invalidated.csv', encoding='utf-8')

# Merge the DataFrames on 'path'
merged_df = pd.merge(golden_standard_df, whisper_df, on='path')

output_df = merged_df[['path', 'sentence', 'sentence_transcript']]

# Save to a new CSV file
output_df.to_csv('merged_sentences_val.csv', index=False, encoding='utf-8')


# Load the CSV file into a DataFrame
df = pd.read_csv('merged_sentences_val.csv', encoding='utf-8')


# Define a function to tokenize sentences
def tokenize_sentence(sentence):
    sentence = sentence.lower()  # Convert to lowercase
    return word_tokenize(sentence)


# Apply tokenization to the 'sentence' and 'sentence_whisper' columns
df['sentence_tokenized'] = df['sentence'].apply(tokenize_sentence)
df['sentence_transcript_tokenized'] = df['sentence_transcript'].apply(tokenize_sentence)

# Save the DataFrame with tokenized sentences to a new CSV file

print("Tokenized sentences saved to 'merged_sentences_tokenized.csv'.")


# Calculate WER for each pair of sentences
wer_scores = df.apply(lambda row: wer(row['sentence_tokenized'], row['sentence_transcript_tokenized']), axis=1)
df['wer'] = df.apply(lambda row: wer(row['sentence_tokenized'], row['sentence_transcript_tokenized']), axis=1)

cer_scores = df.apply(lambda row: cer(row['sentence_tokenized'], row['sentence_transcript_tokenized']), axis=1)
df['cer'] = df.apply(lambda row: cer(row['sentence_tokenized'], row['sentence_transcript_tokenized']) if row['wer'] > 0 else np.nan, axis=1)



# Compute average WER
average_wer = wer_scores.mean()
average_cer = cer_scores.mean()

df.to_csv('cer_wer_invalidated.csv', index=False)


print(f"Average WER: {average_wer:.4f}")
print(f"Average CER: {average_cer:.4f}")


