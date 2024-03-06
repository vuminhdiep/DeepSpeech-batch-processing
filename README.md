# DeepSpeech-batch-processing
## Reference Link:
https://github.com/mozilla/DeepSpeech-examples/tree/r0.9/batch_processing

https://deepspeech.readthedocs.io/en/latest/

## Goal: Run DeepSpeech on a folder of wav audio files and transcribe to json files.

## Requirement: Python 3.6
### Step 1: Create virtual environment to run python 3.6
https://dfordatascience.wordpress.com/2021/04/22/how-to-create-python-3-6-virtual-environment-on-ubuntu-20-04/

https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/

```python3.6 -m venv my-env```

### Step 2: Activate virtual environment and install dependencies


```source $HOME/tmp/deepspeech-gpu-venv/bin/activate```

```pip3 install -r requirements.txt```

### Step 3: Run convert_48khz_to_16khz.py to resample audio files to 16000 khz, take an input folder and generate an output folder of audio files
```python3 convert_48khz_to_16khz.py```

### Step 4: Run driver.py to batch processing an audio folder and output corresponding json files. 

#### Note that the json files will be created in the same folder as the audio files --dirname.

Format: ./driver.py --model {path_to_DeepSpeech_model} --scorer {path_to_DeepSpeech_scorer} --dirname {path_to_audio_folder}

```
./driver.py --model ./models/deepspeech-0.9.3-models.pbmm  --scorer ./models/deepspeech-0.9.3-models.scorer --dirname ./audio/VLD/
```

This command will run individually commands like:
```
./driver.py --model ./models/deepspeech-0.9.3-models.pbmm  --scorer ./models/deepspeech-0.9.3-models.scorer --audio ./audio/VLD/VLD_se0_ag2_f_01_1.wav --json
```
### Step 5: Run json_to_txt.py to convert the transcribed json files to corresponding txt files with only the content from json. Check ```VLD_se0_ag2_f_01_1.json``` and ```VLD_se0_ag2_f_01_1.txt``` to see the example format of transcribed files

```python3 json_to_txt.py```
