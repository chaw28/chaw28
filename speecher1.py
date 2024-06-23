# Christopher Shaw
# 6/15/2024
# IT Capstone Project
# Speecher Program


import os    # Importing the 'os' module for operating system functionalities.
import pyttsx3   # Importing text-to-speech conversion library
import speech_recognition as sr   # Importing library for performing speech recognition, setting sr as alias.
import webbrowser   # Importing web browser module.
import pyautogui    # Importing screenshot capture module.
import datetime    # Importing datetime module.
import platform   # Importing platform information module.


# Retrieves system information using platform module.
# Returns a formatted string with system details.

def get_system_info():
    system_info = platform.uname()
    info_string = f"System: {system_info.system}, Node Name: {system_info.node}, Release: {system_info.release}, Version: {system_info.version}, Machine: {system_info.machine}, Processor: {system_info.processor}"
    return info_string

# Uses speech recognition to listen for user command.
# Returns the recognized command as lowercase string.
# Handles errors if audio cannot be understood or retrieved.

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Error retrieving results; {0}".format(e))
        return ""


# Opens a web browser with Google search results for the given query.
# Exits the program after the search.

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    exit()


# Appends the provided note_text to a file named 'notes.txt'.
# Prints a confirmation message upon successful save.

def save_note_to_file(note_text):
    with open("notes.txt", "a") as file:
        file.write(note_text + "\n")
        print("Note saved to 'notes.txt'.")


# Captures a screenshot and saves it with the specified filename or timestamp in the Downloads folder.
# Prints the filename where the screenshot is saved.

def take_screenshot(filename):
    screenshot = pyautogui.screenshot()
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    screenshot.save(os.path.join(downloads_folder, filename))
    print("Screenshot saved in Downloads folder as", filename)
    
    
# Main function to control the program flow.
# Uses speech recognition to interpret user commands and execute corresponding actions.

def main():
    tts_engine = pyttsx3.init()

    while True:
        try:
            # Get the user's choice
            print("What would you like to do? (say 'search' to search Google, 'take note' to take a note, 'screenshot' to take a screenshot, 'system info' to get system information, or 'exit' to exit)")
            choice = recognize_speech()

            if choice == "search":
                # Get the search query from the user through voice input and initiate search
                print("Please say your search query...")
                query = recognize_speech()
                search_google(query)

            elif choice == "take note":
                # Record user's note and save it to 'notes.txt'
                print("Please say your note...")
                note = recognize_speech()
                save_note_to_file(note)

            elif choice == "screenshot":
                # Capture screenshot with specified filename or timestamp
                print("Please say the filename for the screenshot:")
                filename = recognize_speech()
                if filename:
                    if filename == "":
                        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                        filename = f"screenshot_{current_time}.png"
                    else:
                        filename = filename + ".png"
                    take_screenshot(filename)

            elif choice == "system info":
                # Retrieve, display, and announce system information
                info = get_system_info()
                print(info)
                tts_engine.say(info)
                tts_engine.runAndWait()

            elif choice == "exit":  
                # Exit the program
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("An error occurred:", e)
            continue

if __name__ == "__main__":
    main()
