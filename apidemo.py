import requests
import tkinter as tk

def fetchweather():

    API_KEY="0193d04d34cea17c333b796e3896a3f5"

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    city=t1.get()

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    response=requests.get(url)


    print(response)

    if response.status_code==200:
        result=response.json()
        # print(result)

        x=result['main']
        # print(x)

        msg=f"Weather information of city {city} is..\n"

        msg=msg+f"Temparature : {x['temp']}\n"
        msg=msg+f"Humidity : {x['humidity']}\n"
        msg=msg+f"Pressure : {x['pressure']}"
        print(msg)

        lblresult.config(text=msg,fg="blue")

    else:

        print(f"Sorry city {city} not found !!")
        lblresult.config(text="Sorry city not found !",fg="red")



window=tk.Tk()



lbl=tk.Label(window,text="Enter city name ")
lbl.place(x=100,y=50)

t1=tk.Entry(window)
t1.place(x=200,y=50)


btn=tk.Button(window,text=" Fetch Weather ",bg="green",command=fetchweather )
btn.place(x=200,y=150)


window.geometry('500x500')
window.title("Weather Info App")


lblresult=tk.Label(window,text="Result willbe displayed here")

lblresult.place(x=100,y=300)

window.mainloop()