from pydub import AudioSegment
import os

def resample_audio(input_folder, output_folder, target_sample_rate):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            # Load the audio file
            file_path = os.path.join(input_folder, filename)
            audio = AudioSegment.from_file(file_path)

            # Resample to the target sample rate
            audio = audio.set_frame_rate(target_sample_rate)

            # Save the resampled audio to the output folder
            output_path = os.path.join(output_folder, filename)
            audio.export(output_path, format="wav")

            print(f"Resampled {filename} to {target_sample_rate} Hz")

# Replace these with your input and output folder paths
input_folder = "./audio/raw_audio/VLD/"
output_folder = "./audio/VLD/"
target_sample_rate = 16000  # 16 kHz

resample_audio(input_folder, output_folder, target_sample_rate)
