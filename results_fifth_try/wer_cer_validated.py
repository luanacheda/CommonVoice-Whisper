#Script updated 20.11.2024

import pandas as pd
import numpy as np
from typing import List
import nltk
from nltk.tokenize import word_tokenize
import os
import regex as re






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

def cer(reference: str, hypothesis: str) -> float:
    """Compute the Character Error Rate (CER) between a reference and a hypothesis."""
    # Join the lists of characters into single strings


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



# Load TSV and CSV files into DataFrames
golden_standard_df = pd.read_csv('validated.tsv', sep='\t', encoding='utf-8')
whisper_df = pd.read_csv('transcriptions_large_1000_validated.csv', encoding='utf-8')

# Merge the DataFrames on 'path'
merged_df = pd.merge(golden_standard_df, whisper_df, on='path')

output_df = merged_df[['path', 'sentence', 'sentence_transcript']]

# Save to a new CSV file
output_df.to_csv('sentences_validated_whisper_intermediate.csv', index=False, encoding='utf-8')


# Load the CSV file into a DataFrame
df = pd.read_csv('sentences_validated_whisper_intermediate.csv', encoding='utf-8')


# Define a function to tokenize sentences
def tokenize_sentence_wer(sentence):
    sentence = str(sentence)
    sentence_lower = sentence.lower()
    sentence_tok_perc = re.sub("%", " percento", sentence_lower)
    sentence_tok = re.sub(r"[^\w+\s'-]", "", sentence_tok_perc)
    return word_tokenize(sentence_tok)


characters = []

# Define a function to tokenize sentences
def tokenize_sentence_cer(sentence):
    sentence = str(sentence)
    for character in sentence:
        if not character.isalnum():
            characters.append(character)

    sentence_lower = sentence.lower().strip()  # Convert to lowercase
    sentence_tok_perc = re.sub("%", " percento", sentence_lower)
    sentence_tok = re.sub(r"[^\w+\s'-]", "", sentence_tok_perc)
    sentence_tok_nodoublespace = re.sub("  ", " ", sentence_tok)
    return sentence_tok_nodoublespace


# Apply tokenization to the 'sentence' and 'sentence_whisper' columns
df['sentence_tokenized_wer'] = df['sentence'].apply(tokenize_sentence_wer)
df['sentence_transcript_tokenized_wer'] = df['sentence_transcript'].apply(tokenize_sentence_wer)

df['sentence_tokenized_cer'] = df['sentence'].apply(tokenize_sentence_cer)
df['sentence_transcript_tokenized_cer'] = df['sentence_transcript'].apply(tokenize_sentence_cer)



# Calculate WER for each pair of sentences
wer_scores = df.apply(lambda row: wer(row['sentence_tokenized_wer'], row['sentence_transcript_tokenized_wer']), axis=1)
df['wer'] = df.apply(lambda row: wer(row['sentence_tokenized_wer'], row['sentence_transcript_tokenized_wer']), axis=1)

cer_scores = df.apply(lambda row: cer(row['sentence_tokenized_cer'], row['sentence_transcript_tokenized_cer']), axis=1)
df['cer'] = df.apply(lambda row: cer(row['sentence_tokenized_cer'], row['sentence_transcript_tokenized_cer']), axis=1)



average_wer = wer_scores.mean()
average_cer = cer_scores.mean()
df.at[0, 'average WER'] = average_wer
df.at[0, 'average CER'] = average_cer

df.to_csv('cer_wer_validated.csv', index=False)

os.remove("sentences_validated_whisper_intermediate.csv")

print(f"Average WER: {average_wer:.4f}")
print(f"Average CER: {average_cer:.4f}")

#print(set(characters))


