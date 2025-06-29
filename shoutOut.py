# from gtts import gTTS
# import os

# # Get user input
# mytext = input("Enter the text you want to convert to speech: ")

# # Set language
# language = 'en'

# # Convert to speech
# myobj = gTTS(text=mytext, lang=language, slow=False)

# # Save to file
# myobj.save("welcome.mp3")

# # Play the file (Windows)
# os.system("start welcome.mp3")


# from gtts import gTTS
# import os

# # Available language options (can be expanded)
# languages = {
#     "en": "English",
#     "hi": "Hindi",
#     "es": "Spanish",
#     "fr": "French",
#     "de": "German"
# }

# def show_language_options():
#     print("\n🌐 Available languages:")
#     for code, name in languages.items():
#         print(f"{code} : {name}")

# while True:
#     show_language_options()
#     lang = input("\nEnter language code (or 'exit' to quit): ").strip().lower()

#     if lang == "exit":
#         print("Goodbye! 👋")
#         break

#     if lang not in languages:
#         print("❌ Invalid language code. Try again.")
#         continue

#     user_input = input("Enter the text you want to convert to speech (or type 'exit' to quit): ")

#     if user_input.lower() == "exit":
#         print("Goodbye! 👋")
#         break

#     try:
#         tts = gTTS(text=user_input, lang=lang, slow=False)
#         filename = "output.mp3"
#         tts.save(filename)
#         os.system(f"start {filename}")  # Windows
#     except Exception as e:
#         print(f"⚠️ Error: {e}")
        
        
from gtts import gTTS
import os
import sys
import webbrowser

# Available language options
languages = {
    "en": "English",
    "hi": "Hindi",
    "es": "Spanish",
    "fr": "French",
    "de": "German"
}

def show_language_options():
    print("\n🌐 Available languages:")
    for code, name in languages.items():
        print(f"{code} : {name}")

while True:
    show_language_options()
    lang = input("\nEnter language code (or 'exit' to quit): ").strip().lower()

    if lang == "exit":
        print("Goodbye! 👋")
        break

    if lang not in languages:
        print("❌ Invalid language code. Try again.")
        continue

    user_input = input("Enter the text you want to convert to speech (or type 'exit' to quit): ").strip()

    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    try:
        # Create MP3
        tts = gTTS(text=user_input, lang=lang, slow=False)
        mp3_filename = "output.mp3"
        tts.save(mp3_filename)

        # Create HTML
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Text to Speech Output</title>
            <style>
                body {{
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 50px;
                }}
                h1 {{
                    color: #333;
                }}
                p {{
                    color: #555;
                }}
                audio {{
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <h1>Text to Speech Output</h1>
            <p><strong>Language:</strong> {languages[lang]}</p>
            <p><strong>Text:</strong> {user_input}</p>
            <audio controls autoplay>
                <source src="{mp3_filename}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
        </body>
        </html>
        """

        html_filename = "output.html"
        with open(html_filename, "w", encoding="utf-8") as f:
            f.write(html_content)

        # Open in browser
        file_path = os.path.abspath(html_filename)
        url = f"file://{file_path}"
        webbrowser.open(url)

        print(f"✅ HTML page created and opened in your browser.")

    except Exception as e:
        print(f"⚠️ Error: {e}")
