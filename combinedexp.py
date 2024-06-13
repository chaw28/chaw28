import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import pyautogui
import datetime
import platform

def get_system_info():
    system_info = platform.uname()
    info_string = f"System: {system_info.system}, Node Name: {system_info.node}, Release: {system_info.release}, Version: {system_info.version}, Machine: {system_info.machine}, Processor: {system_info.processor}"
    return info_string

def recognize_speech(tts_engine):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        tts_engine.say("Listening for command...")
        print("Listening for command...")
        tts_engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        tts_engine.say(f"You said: {command}")
        tts_engine.runAndWait()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        tts_engine.say("Could not understand audio.")
        tts_engine.runAndWait()
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        tts_engine.say(f"Error retrieving results: {e}")
        tts_engine.runAndWait()
        print("Error retrieving results:", e)
        return ""

def search_google(tts_engine, query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    tts_engine.say("Exiting after search.")
    tts_engine.runAndWait()
    exit()

def save_note_to_file(tts_engine, note_text):
    with open("notes.txt", "a") as file:
        file.write(note_text + "\n")
        tts_engine.say("Note saved to 'notes.txt'.")
        tts_engine.runAndWait()
        print("Note saved to 'notes.txt'.")

def take_screenshot(tts_engine, filename):
    screenshot = pyautogui.screenshot()
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    screenshot.save(os.path.join(downloads_folder, filename))
    tts_engine.say("Screenshot saved in Downloads folder as " + filename)
    tts_engine.runAndWait()
    print("Screenshot saved in Downloads folder as", filename)

def main():
    tts_engine = pyttsx3.init()

    while True:
        try:
            # Get the user's choice
            tts_engine.say("What would you like to do? Say 'search' to search Google, 'take note' to take a note, 'screenshot' to take a screenshot, 'system info' to get system information, or 'exit' to exit.")
            tts_engine.runAndWait()
            print("What would you like to do? (say 'search' to search Google, 'take note' to take a note, 'screenshot' to take a screenshot, 'system info' to get system information, or 'exit' to exit)")
            choice = recognize_speech(tts_engine)

            if choice == "search":
                # Get the search query from the user through voice input
                tts_engine.say("Please say your search query...")
                tts_engine.runAndWait()
                print("Please say your search query...")
                query = recognize_speech(tts_engine)

                # Perform the Google search
                search_google(tts_engine, query)

            elif choice == "take note":
                # Take a note using voice input
                tts_engine.say("Please say your note...")
                tts_engine.runAndWait()
                print("Please say your note...")
                note = recognize_speech(tts_engine)
                save_note_to_file(tts_engine, note)

            elif choice == "screenshot":
                # Take a screenshot
                tts_engine.say("Please say the filename for the screenshot:")
                tts_engine.runAndWait()
                print("Please say the filename for the screenshot:")
                filename = recognize_speech(tts_engine)
                if filename:
                    if filename == "":
                        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                        filename = f"screenshot_{current_time}.png"
                    else:
                        filename = filename + ".png"
                    take_screenshot(tts_engine, filename)

            elif choice == "system info":
                # Get system information
                info = get_system_info()
                tts_engine.say(info)
                tts_engine.runAndWait()
                print(info)

            elif choice == "exit":
                tts_engine.say("Exiting program...")
                tts_engine.runAndWait()
                print("Exiting program...")
                break

            else:
                tts_engine.say("Invalid choice. Please try again.")
                tts_engine.runAndWait()
                print("Invalid choice. Please try again.")

        except Exception as e:
            tts_engine.say("An error occurred: " + str(e))
            tts_engine.runAndWait()
            print("An error occurred:", e)
            continue

if __name__ == "__main__":
    main()
