#!/usr/bin/env python3
import json
import os

# Define the input and output folder paths
input_folder_path = './audio/VLD/'
output_folder_path = './transcript/hypo_text/VLD/'

# Ensure the output directory exists
os.makedirs(output_folder_path, exist_ok=True)

# Process each JSON file in the input folder
for filename in os.listdir(input_folder_path):
    if filename.endswith('.json'):
        input_file_path = os.path.join(input_folder_path, filename)
        base_filename = os.path.splitext(filename)[0]
        final_name = base_filename
        output_file_path = os.path.join(output_folder_path, f'{final_name}.txt')
       
        # Read the JSON file
        with open(input_file_path, 'r') as file:
            data = json.load(file)
       
        # Extract words from the transcripts and save them in a single string separated by spaces
        words = ' '.join([word['word'] for transcript in data['transcripts'] for word in transcript['words']])
       
        # Save the words string to a new text file
        with open(output_file_path, 'w') as file:
            file.write(words)
               
        print(f'Words extracted and saved to {output_file_path}')
