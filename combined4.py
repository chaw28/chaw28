import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import pyautogui
import datetime

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    # Exiting after search
    exit()

def save_note_to_file(note_text):
    with open("notes.txt", "a") as file:
        file.write(note_text + "\n")
        print("Note saved to 'notes.txt'.")

def take_screenshot(filename):
    screenshot = pyautogui.screenshot()
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    screenshot.save(os.path.join(downloads_folder, filename))
    print("Screenshot saved in Downloads folder as", filename)

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

def main():
    tts_engine = pyttsx3.init()

    while True:
        try:
            # Get the user's choice
            print("What would you like to do? (say 'search' to search Google, 'take note' to take a note, 'screenshot' to take a screenshot, or 'exit' to exit)")
            choice = recognize_speech()

            if choice == "search":
                # Get the search query from the user through voice input
                print("Please say your search query...")
                query = recognize_speech()

                # Perform the Google search
                search_google(query)

            elif choice == "take note":
                # Take a note using voice input
                print("Please say your note...")
                note = recognize_speech()
                save_note_to_file(note)

            elif choice == "screenshot":
                # Take a screenshot
                print("Please say the filename for the screenshot:")
                filename = recognize_speech()
                if filename:
                    if filename == "":
                        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                        filename = f"screenshot_{current_time}.png"
                    else:
                        filename = filename + ".png"
                    take_screenshot(filename)

            elif choice == "exit":
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("An error occurred:", e)
            continue

if __name__ == "__main__":
    main()
