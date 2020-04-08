
import speech_recognition as sr 
#import time
from playsound import playsound
from gtts import gTTS
import os


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
        exit() 
        #return text






def respond():
	import time
	#import unittest
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	driver = webdriver.Chrome()
	driver.get('http://www.youtube.com')


	elem =driver.find_element_by_id('search')
	#time.sleep(5)
	assistant_speaks('put the query')
	audio_op = get_audio()

	time.sleep(2)
	elem.send_keys(audio_op)
	#elem.click()
	time.sleep(2)
	button = driver.find_element_by_id('search-icon-legacy').click()
	
	
	

if __name__ == "__main__":
	import time
	#import unittest
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	driver = webdriver.Chrome()
	driver.get('http://www.youtube.com')


	elem =driver.find_element_by_id('search')
	assistant_speaks('put the query')
	
	audio_op = get_audio()

	time.sleep(2)

	#time.sleep(2)
	elem.send_keys(audio_op)
	#elem.click()
	#time.sleep(2)
	button = driver.find_element_by_id('search-icon-legacy').click()

	#song = driver.find_element_by_id('mouseover-overlay').click()
	#time.sleep(2)
	video = driver.find_element_by_id('video-title')
	link = video.get_attribute('/watch?v=9Q1kbzcCX1M')
	link.click() 




















