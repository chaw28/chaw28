import speech_recognition as sr
import webbrowser
import pyttsx3

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    # Exiting after search
    exit()

def save_note_to_file(note_text):
    with open("notes.txt", "a") as file:
        file.write(note_text + "\n")
        print("Note saved to 'notes.txt'.")

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
            # Get the user's choice
            print("What would you like to do? (say 'search' to search Google, 'take note' to take a note, or 'exit' to exit)")
            choice = listen()

            if choice == "search":
                # Get the search query from the user through voice input
                print("Please say your search query...")
                query = listen()

                # Perform the Google search
                search_google(query)

            elif choice == "take note":
                # Take a note using voice input
                take_note()

            elif choice == "exit":
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("An error occurred:", e)
            continue

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
    main()
