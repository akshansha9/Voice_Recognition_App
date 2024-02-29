import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from tkinter import *
import cv2

def assist():

        listener = sr.Recognizer()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)


        def talk(text):
            engine.say(text)
            engine.runAndWait()


        def take_command():
            try:
                with sr.Microphone() as source:
                    print('listening...')
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    if 'alexa' in command:
                        command = command.replace('alexa', '')
                        print(command)
            except:
                pass
            return command


        def run_alexa():
            command = take_command()
            print(command)
            if 'play' in command:
                song = command.replace('play', '')
                talk('playing ' + song)
                pywhatkit.playonyt(song)
            elif 'search' in command:
                content = command.replace('search', '')
                talk('searching ' + content)
                pywhatkit.search(content)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
            elif 'who the heck is' in command:
                person = command.replace('who the heck is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'date' in command:
                talk('sorry, I have a headache')
            elif 'are you single' in command:
                talk('I am in a relationship with wifi')
            elif 'joke' in command:
                talk(pyjokes.get_joke())
            else:
                talk('Please say the command again.')


        while True:
            run_alexa()


def imgi():
        
    image = cv2.imread("dog.jpg")
    cv2.imshow("Dog", image)
    cv2.waitKey(0)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("New Dog", gray_image)
    cv2.waitKey(0)
    inverted_image = 255 - gray_image
    cv2.imshow("Inverted", inverted_image)
    cv2.waitKey()
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    cv2.imshow("Sketch", pencil_sketch)
    cv2.waitKey(0)
    cv2.imshow("original image", image)
    cv2.imshow("pencil sketch", pencil_sketch)
    cv2.waitKey(0)

root =Tk()
root.geometry("655x333")

frame = Frame(root, borderwidth=56, bg="yellow", relief=SUNKEN)
frame.pack(side=TOP, )

b1 = Button(frame, fg="red", text="Artificial Assistant", command=assist)
b1.pack(side=LEFT, padx=53)

frame = Frame(root, borderwidth=56, bg="green", relief=SUNKEN)
frame.pack(side=TOP, )

b1 = Button(frame, fg="red", text="Image Filter", command=imgi)
b1.pack(side=LEFT, padx=53)




root.mainloop()