# pip install SpeechRecognition
# pip install pyttsx3
# pip install pywhatkit
# pip install wikipedia

import speech_recognition as sr
import pyttsx3 #use to change text to speech 
import pywhatkit
import wikipedia
import datetime

s = sr.Recognizer()
phone_numbers = {'rahul':'8054014585','gayan':'9996860206'}
bank_acc_number = {"tt":"123456"}

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            s.adjust_for_ambient_noise(source)  
            print('Listening... Ask now...')  
            audioin = s.listen(source, timeout=3, phrase_time_limit=5) 
            # audioin = s.listen(source)
            my_text = s.recognize_google(audioin) 
            my_text = my_text.lower()
            print(f"You said: {my_text}")  # Print or return the result to see the output
            speak(my_text)
            
            # ask to play song
            if 'play' in my_text:
                my_text = my_text.replace('play','')
                speak('playing'+ my_text)
                pywhatkit.playonyt(my_text)
            # ask date
            elif 'date' in my_text:
                today = datetime.date.today()
                speak(today)
            # ask time
            elif 'time' in my_text:
                now = datetime.datetime.now().strftime("%H:%M")
                speak(now)
            # ask details about any person 
            elif 'who is ' in my_text:
                person = my_text.replace('who is','')
                info  = wikipedia.summary(person,1)
                speak(info)
            # ask phone numbers
            elif"phone number" in my_text:
                names=list(phone_numbers)
                print(names)
                for name in names:
                    if name in my_text:
                        print(name +"phone_number is " + phone_numbers[name])
                        speak(name +"phone_number is " + phone_numbers[name])
                        
                        
            else:
                speak("Sorry, I didn't understand that. Please try again.")
                        
            
            # ask personal bank account number
            if "account number" in my_text:
                banks = list(bank_acc_number)
                for bank in banks:
                    if bank in my_text:
                        print(bank + "bank account number is" + bank_acc_number[bank])
                        speak(bank + "bank account number is" + bank_acc_number[bank])
                
            
            
    except Exception as e:
        print(f"Error in capturing microphone: {e}")
        

speak(" iam Listning to you")
commands()