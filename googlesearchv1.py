# Christopher Shaw
# 6/1/2024
# IT Capstone Project

# imports and creates alias for speech rec as sr
# imports web browser
import speech_recognition as sr
import webbrowser

# defines function named search_google that takes parameter query
# constructs google url using f string where query is replaced by 
# actual search query, open url to do the search
def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# defines listen function
# creates recognizer instance, sets microphone as audio source
# prompts user to say something, listens for audio
# displays audio recognized or errors
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for audio...")
        audio = r.listen(source)
        try:
            print("Audio received. Processing...")
            recognized_text = r.recognize_google(audio)
            print("You said: " + recognized_text)
            return recognized_text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

# get the search query from the user through voice input
# performs the Google search
# asks if the user wants to perform another search or error message
def main():
    while True:
        try:
            print("Please say your search query...")
            query = listen()

            search_google(query)

            choice = input("Do you want to perform another search? (yes/no): ")
            if choice.lower() != "yes":
                break
        except Exception as e:
            print("An error occurred:", e)
            continue

if __name__ == "__main__":
    main()
