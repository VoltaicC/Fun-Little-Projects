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

for i in range (len(stories.story)):
    print(str(i) + ": " + stories.story[i]["title"])
prompt = int(input("Which prompt needs to be typed? "))
prompt = stories.story[prompt]["content"]
time.sleep(2)
type_string_with_delay(prompt)

