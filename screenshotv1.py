# Christopher Shaw
# 6/1/2024
# IT Capstone Project


# imports os to interact with operating system
# pyautogui to takes screenshots, date/time for correct date/time
# imports and gives speech rec an alias
import os
import pyautogui
import datetime
import speech_recognition as sr


# captures the screenshot
# gets the path to the downloads folder
# saves the screenshot in the downloads folder with the provided filename
def take_screenshot(filename):
    screenshot = pyautogui.screenshot()
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    screenshot.save(os.path.join(downloads_folder, filename))
    print("Screenshot saved in Downloads folder as", filename)

# defines rec speech function, initializes recognizer
def recognize_speech():
    recognizer = sr.Recognizer()

# sets microphone as audio source, prompts user for file name
# adjust for ambient noise and capture audio
    with sr.Microphone() as source:
        print("Please say the filename for the screenshot:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

# sets recognizer to use Google speech rec
# displays file name
# displays error messages
    try:
        filename = recognizer.recognize_google(audio)
        print("You said:", filename)
        return filename
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print("Error retrieving results; {0}".format(e))
        return None

# defines main function, calls speech rec function
# assigns filename variable, gets date/time to use for file name
# if audio is not recognized
def main():
    filename = recognize_speech()
    if filename:
        
        if filename == "":
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"screenshot_{current_time}.png"
        else:
            filename = filename + ".png"

# takes the screenshot
        take_screenshot(filename)

if __name__ == "__main__":
    main()
