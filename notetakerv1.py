# Christopher Shaw
# 6/1/2024
# IT Capstone Project
# Note Taker V1

import speech_recognition as sr 
import pyttsx3   

def save_note_to_file(note_text):  
    with open("mynotes.txt", "a") as file:
        file.write(note_text + "\n")
        print("Note saved to 'mynotes.txt'.")

def take_note():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    tts_engine = pyttsx3.init()

    try:
        with microphone as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for your note...")
            audio = recognizer.listen(source)

        print("Recognizing...")
        note = recognizer.recognize_google(audio)
        print(f"Your note: {note}")
        save_note_to_file(note)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        tts_engine.say("Sorry, I could not understand the audio.")
        tts_engine.runAndWait()
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        tts_engine.say(f"Could not request results; {e}")
        tts_engine.runAndWait()
    except Exception as ex:
        print(f"An error occurred: {ex}")
        tts_engine.say(f"An error occurred: {ex}")
        tts_engine.runAndWait()

if __name__ == "__main__":
    take_note()
