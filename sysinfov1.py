# Christopher Shaw
# 6/2/2024
# IT Capstone Project

import speech_recognition as sr
import platform
import pyttsx3

def get_system_info():
    system_info = platform.uname()
    info_string = f"System: {system_info.system}, Node Name: {system_info.node}, Release: {system_info.release}, Version: {system_info.version}, Machine: {system_info.machine}, Processor: {system_info.processor}"
    return info_string

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)
        try:
            print("Command received. Processing...")
            command = r.recognize_google(audio).lower()
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

def main():
    tts_engine = pyttsx3.init()

    while True:
        try:
            # Get the user's command
            print("What would you like to do? (say 'system info' to get system information or 'exit' to exit)")
            command = listen()

            if command == "system info":
                # Get system information
                info = get_system_info()
                print(info)
                tts_engine.say(info)
                tts_engine.runAndWait()
                # Exiting after showing system info
                break

            elif command == "exit":
                print("Exiting program...")
                break

            else:
                print("Invalid command. Please try again.")

        except Exception as e:
            print("An error occurred:", e)
            continue

if __name__ == "__main__":
    main()
