import tkinter as tk
from tkinter import font
import requests
HEIGHT = 500
WIDTH = 800

def test_function(entry):
    print("This is the entry: ", entry)

#9d06b93ff194aeaf01eb292522596924
#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}

def get_weather(city):
    api_key = '9d06b93ff194aeaf01eb292522596924'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'appid': api_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=parameters)
    weather = response.json()
    label['text'] = format(weather)

def format(weather):
    try:
        name = 'NAME: ' + weather['name']
        temp = "TEMPERATURE: " + str(weather['main']['temp'])
        press = 'PRESSURE: ' + str(weather['main']['pressure'])
        wind = 'WIND: ' + str(weather['wind']['speed'])
        clouds = 'CLOUDS: ' + str(weather['clouds']['all'])
        cont = 'COUNTRY: ' + str(weather['sys']['country'])
        #icon = weather['weather']['icon']

        final_str = name+'\n'+temp+'\n'+press+'\n'+wind+'\n'+clouds+'\n'+cont

    except:
        final_str = 'There was a problem retrieving that information...'

    return final_str

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='white', font=('courier',15), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()