# Smyth Avgoustakis Light meter Website Redirector
import webbrowser
from gpiozero import Button
from guizero import App, Text
from PiAnalog import *
import time, math



# when inputting a link it doesnt have to inclue www or https://
# the link could also be a specific link showing a video or item or shop listing etc.
x = input("Put the first website you want (Has to be a full URL)\n")

y = input("Put the second website you want (Has to be a full URL)\n")

z = input("Put the third website you want (Has to be a full URL)\n")



p = PiAnalog()
button = Button(25)

multiplier = 2000 # increase to make more sensitive



def webopen(light): #hit = button press then hopefully the website opens
    global button
    if light >= 2 and light <= 4:
        print("hit")
        webbrowser.open(x)

    if light > 4 and light <= 7:
        print("hit")
        webbrowser.open(y)

    if light > 7 and light <= 10:
        print("hit")
        webbrowser.open(z)



def light_from_r(R):
    light = 1/math.sqrt(R) * multiplier
    if light > 100:
        light = 100
    if button.is_pressed:
        webopen(light)
    # Sqareroot the reading to compress the range
    return light




# group together all of the GUI code
# Update the reading
def update_reading():
    light = light_from_r(p.read_resistance())
    reading_str = "{:.0f}".format(light)
    light_text.value = reading_str
    light_text.after(200, update_reading)



app = App(title="Light Meter", width="400", height="300")
Text(app, text="Light", size=32)
light_text = Text(app, text="0", size=110)
light_text.after(200, update_reading)
app.display()
