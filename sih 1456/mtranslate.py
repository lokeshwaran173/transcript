import speech_recognition as sr
from googletrans import Translator

# Initialize the SpeechRecognition object
recognizer = sr.Recognizer()

# Function to transcribe and provide a corrected translation for an existing audio file
def transcribe_and_translate_audio(audio_file_path):
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)
            transcription = recognizer.recognize_google(audio_data, language="en-IN")

            print(f"Transcription (English): {transcription}")

            # Translate the transcription to English using Google Translate API
            translator = Translator()
            translation = translator.translate(transcription, src="auto", dest="en")

            print(f"Translation (English): {translation.text}")

            # Translate the transcription to Hindi using Google Translate API
            hindi_translation = translator.translate(translation.text, src="en", dest="hi")

            print(f"Translation (Hindi): {hindi_translation.text}")

    except sr.UnknownValueError:
        print("No speech detected.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

# Specify the path to your existing audio file
audio_file_path = 'modijispeech.wav'

# Call the function to transcribe and provide the translations
transcribe_and_translate_audio(audio_file_path)
