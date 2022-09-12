import time
import stories
import random
from pynput.keyboard import Controller

keyboard = Controller() 

def type_string_with_delay(string):
    for character in string: 
        keyboard.type(character)  
        delay = random.uniform(.03, .1)  
        time.sleep(delay)  

def type_string(string):
    keyboard.type(string)  


for i in range (len(stories.story)):
    print(str(i) + ": " + stories.story[i]["title"])
prompt = int(input("Which prompt needs to be typed? "))
prompt = stories.story[prompt]["content"]

speed = int(input("Enter 0 for fast, or anything else for very fast: "))
time.sleep(2)

if speed == 0:
    type_string_with_delay(prompt)
else:
    type_string(prompt)

