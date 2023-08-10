# Text-to-Speech App

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This is a simple Text-to-Speech Converter application built using Python and the gTTS library. It allows you to enter text, convert it to speech, play the generated audio, and delete the audio file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)


## Installation

1. Clone the repository:
   ```sh
   `git clone https://github.com/younes271/text-to-speech-app.git`
   `cd text-to-speech-app`

2.Install the required packages using pip:
  - `pip install -r requirements.txt`
  
## Usage

1. Run the application:
  `python text_to_speech_app.py`
  The application window will appear with a text entry area and buttons to convert text to speech, play audio, and delete audio files.

## Dependencies
  > Python (>=3.6)
  > pygame (2.1.1.post1): Used for audio playback.
  > gTTS (2.2.3): Google Text-to-Speech library for generating speech from text.
