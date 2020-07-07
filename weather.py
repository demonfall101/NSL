import tkinter as tk
from tkinter import font
import requests

height = 500
width = 600

def test_function(entry):
	print("this is the entry:", entry)

def format_response(weather):
        try:
                name = weather['name']
                desc = weather['weather'][0]['description']
                temp = weather['main']['temp']

                final_str = ( ('City: ' + (str(name))) + '\n' + ('Condidions: ' + (str(desc))) + '\n' + ('Temperature: ' + (str(temp)) + '°F') )
        except:
                final_str = 'There was a problem retrieving that information'

        return final_str

def get_weather(city):
	weather_key = '0de26de28cadc201d0bd90f9331eccd8'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params= params)
	weather = response.json()

	label['text'] = format_response(weather)

# key: 0de26de28cadc201d0bd90f9331eccd8
# url: api.openweathermap.org/data/2.5/forecast

root = tk.Tk()

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

backgroundimage = tk.Frame(bg='#9933ff')
backgroundimage.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#5b84d7', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font = ('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font = ('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lowerframe = tk.Frame(root, bg='#5b84d7', bd=10)
lowerframe.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lowerframe, font = ('Courier', 18))
label.place(relwidth=1, relheight=1)

root.mainloop()
