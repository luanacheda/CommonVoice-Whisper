import os
import csv
import whisper

# Load the Whisper model
model = whisper.load_model("large") # select the model

# Create a list to store the results
results = []

# Input folder containing audio files
input_folder = "invalidated" # change the input folder

# Output CSV file
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_csv = os.path.join(desktop_path, "transcriptions_large_1000_invalidated.csv") # change the name of the file

# Define decoding options with the desired language
options = whisper.DecodingOptions(language="it")

# Initialize a counter for processed files
file_counter = 0

# Iterate through audio files in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp3"):
        audio_file = os.path.join(input_folder, filename)
        
        # Transcribe the audio
        transcription = model.transcribe(audio_file, language="it")
        
        # Append the results to the list
        results.append({
            "path": filename,
            "sentence_transcript": transcription["text"]
        })
        
        # Increment the file counter
        file_counter += 1
        
        # Print a message every 100 files
        if file_counter % 100 == 0:
            print(f"{file_counter} files processed")
        

# Write the results to a CSV file
with open(output_csv, mode="w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["path", "sentence_transcript"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    for result in results:
        writer.writerow(result)

print(f"Transcriptions saved to {output_csv}")
