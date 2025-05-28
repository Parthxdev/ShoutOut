from gtts import gTTS
import os

# Get user input
mytext = input("Enter the text you want to convert to speech: ")

# Set language
language = 'en'

# Convert to speech
myobj = gTTS(text=mytext, lang=language, slow=False)

# Save to file
myobj.save("welcome.mp3")

# Play the file (Windows)
os.system("start welcome.mp3")
