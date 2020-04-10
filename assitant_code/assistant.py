import speech_recognition as sr 
from playsound import playsound
from time import ctime # easy way to get the time ctime is a function ()
from gtts import gTTS
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#from datetime import date ,time
from datetime import datetime
import os
import time
#import smtplib
import wikipedia

import pyjokes

num = 1
def assistant_speaks(output): 
    global num 
  
     
    num += 1
    print("assistant : ", output) 
  
    toSpeak = gTTS(text = output, lang ='en-IN', slow = False) 
    # saving the audio file given by google text to speech 
    file = str(num)+".mp3"
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound(file, True)  
    os.remove(file) 


def record_audio():

    r = sr.Recognizer() # main command for recoginze

    with sr.Microphone() as source: # enable the microphone 
        print('say somthing')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)

        audio = r.listen(source,phrase_time_limit = 5) # actualy  listen the audio , wait for 5 second
        voice_data = ''

        #voice_data = r.recognize_google(audio) # api is use to convert the speech to text
        try:
            voice_data = r.recognize_google(audio) # api is use to convert the speech to text
        except sr.UnknownValueError:
            print('sorry, i did not get that')
        except sr.RequestError:
            print('sorry,my speech service is down')
        return voice_data
        voice_data = record_audio()





def mail():
    assistant_speaks('whats is subject')
    time.sleep(2)
    subject = record_audio()
    print(voice_data)
    assistant_speaks('whats should i say')
    time.sleep(2)
    message =record_audio()
    print(voice_data)

    import smtplib
    fromaddr = 'magarajay538@gmail.com'
    toaddrs ='Aishwarya2998@gmail.com'

    msg = 'subject:{}\n\n{}'.format(subject,message)

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your_email_add','your_email_pass')
    server.sendmail(fromaddr,toaddrs,msg)
    server.quit()
    

 











  
  
def get_audio(): 
  
    Object = sr.Recognizer() 
    audio = '' 
  
    with sr.Microphone() as source: 
        print("Speak...") 
          
        # recording the audio using speech recognition 
        audio = Object.listen(source, phrase_time_limit = 5)  
    print("Stop.") # limit 5 secs 
  
    try: 
  
        text = Object.recognize_google(audio, language ='en-IN') 
        print("You : ", text) 
        return text 
  
    except: 
  
        assistant_speaks("Could not understand your audio, PLease try again !") 
        get_audio()
        #return text


def browser_auto():
    driver = webdriver.Chrome()
    driver.get('http://www.youtube.com')


    elem =driver.find_element_by_id('search')
    assistant_speaks('what you want to listen')
    
    audio_op = get_audio()

    # audio_op = "saint motel a good song never dies"

    

    elem.send_keys(audio_op)

    button = driver.find_element_by_id('search-icon-legacy').click()


    driver.refresh() # refresh the page so that the driver doesn't have old links

    video = driver.find_elements_by_xpath("//a[contains(@id, 'video-title')]") # get the video-title id from all the a tags on the page


    links = [vid.get_attribute('href') for vid in video] # get all the href from the webElemenets
    
    driver.get(links[0]); # get the first link, can choose any link based on index

    time.sleep(200)
    driver.close()
    
    


  
  
# Driver Code 
if __name__ == "__main__": 
    assistant_speaks("What's your name,") 
    
    name = get_audio().lower()
    #if name is  None:
        #name == 'stranger'
        #assistant_speaks('Hello '+ name +'.')
    assistant_speaks('Hello '+ name + '.')
      
    while True: 
  
        assistant_speaks("What can i do for you?") 
        text = get_audio().lower()
  
        if text == 0: 
            continue

        elif 'tell me time' in str(text):
        	today = datetime.now().strftime("%H:%M:%S")
        	time_1 = str(today)
        	assistant_speaks('time is '+time_1+'.')

        elif 'who are you' in str(text):
        	assistant_speaks('hii i am your personal assistant ash i here to make your life easier')

        elif 'who made you' in str(text):
        	assistant_speaks('{} made me'.format(name))

        elif 'song' in str(text):
        	os.system('Vibe.mp3')
            #playsound('Vibe.mp3')

        elif "what's my name" in str(text):
            assistant_speaks('your name is{}'.format(name))


        elif 'email to aditya' in str(text):
            #assistant_speaks('tell me the name of person')
            mail() 
            time.sleep(0.2)

            assistant_speaks('mail send to aditya')

        elif 'jokes' in str(text):
            assistant_speaks(pyjokes.get_joke())


        elif 'wikipedia' in str(text):
            assistant_speaks('searching wikipedia...')
            text = text.replace('wikipedia','')
            result = wikipedia.summary(text,sentences=3)
            assistant_speaks('According to wikipedia')
            print(result)
            assistant_speaks(result)

        elif 'open youtube' in str(text):
            assistant_speaks('opening youtube')
            browser_auto()
            time.sleep(300)

        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
            assistant_speaks("Ok bye, "+ name+'.') 
            break

        if text == False or None:
            exit()

  
        
        







