# Programming Project - Common Voice & Whisper

How to run:

## 1 - Get 1000 random mp3 files from the italian common voice data:

Python script to select 1000 random mp3 audio files 
* take_1000_random_mp3_validated.py
* take_1000_random_mp3_invalidated.py

To get the result the following files are needed:
* clips folder with all the mp3 data (downloaded from common voice italian)

Output:
* clips_folder_1000_randomized_invalidated with 1000 invalidated mp3 files in it
* clips_folder_1000_randomized_validated with 1000 validated mp3 files in it   
  


## 2 - Whisper Transcripts

Python script to get the Whisper transcripts - ca. 5 hours:
* whisper_csv_output.py

To get the results the following files are needet:
* 1000 random mp3 files taken from common voice (clips_folder_1000_randomized)

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

Output files of the 2 python scripts:
* count_validated.png
* count_invalidated.png
