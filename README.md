# Programming Project - Common Voice & Whisper

How to run:

1 - select 1000 random mp3 audio files (run: take_1000_random_mp3_validated.py and take_1000_random_mp3_invalidated.py)
This cretaes two new folders containg 1000 rando mp3 files from the Common Voice corpus.

## 2 - Whisper Transcripts
Python script to get the Whisper transcripts - ca. 5 hours:
* whisper_csv_output.py
To get the results the following files are needet:
* mp3 data from common voice (clips folder)
Output files of the python script:
* transcriptions_large_1000_invalidated.csv
* transcriptions_large_1000_validated.csv


## 3  - CER and WER
Python scripts to get CER and WER:
* cer_wer_invalidated.py
* cer_wer_validated.py
To get the results the following files are needed:
* transcriptions_large_1000_invalidated.csv
* transcriptions_large_1000_validated.csv
Output files of the 2 python scripts
* cer_wer_invalidated.csv
* cer_wer_validated.csv

## 4 - WER and CER graphs
Python script to get a count of the WER values:
* count_values.py
To get the results the following files are needed
* cer_wer_invalidated.csv
* cer_wer_validated.csv
Output files 
