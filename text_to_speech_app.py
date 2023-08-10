import os
import pygame
import tkinter as tk
from gtts import gTTS

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech Converter")

        # Create a label to guide the user
        self.label = tk.Label(root, text="Enter text:")
        self.label.pack()

        # Create a text area for the user to input multiple lines of text
        self.text_entry = tk.Text(root, height=5, width=40)
        self.text_entry.pack()

        # Create a button to convert the entered text to speech
        self.convert_button = tk.Button(root, text="Convert to Speech", command=self.convert_to_speech)
        self.convert_button.pack()

        # Create a button to play the generated audio
        self.play_button = tk.Button(root, text="Play Audio", command=self.play_audio)
        self.play_button.pack()

        # Create a button to delete the generated audio file
        self.delete_button = tk.Button(root, text="Delete Audio", command=self.delete_audio)
        self.delete_button.pack()

    def convert_to_speech(self):
        # Retrieve the text from the text area
        text = self.text_entry.get("1.0", "end-1c")
        
        # Generate speech from the text using gTTS
        tts = gTTS(text, lang='en')
        tts.save('audio.mp3')

    def play_audio(self):
        pygame.mixer.init()
        pygame.mixer.music.load('audio.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)

    def delete_audio(self):
        # Stop audio playback and wait for the end event to be triggered
        pygame.mixer.music.stop()
        pygame.event.wait(pygame.USEREVENT)
        
        # Delete the generated audio file
        os.remove('audio.mp3')

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
