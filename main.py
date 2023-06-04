from tkinter import *
from PIL import Image, ImageTk
import phonenumbers
import pytz
from phonenumbers import carrier, geocoder, timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime

main_window = Tk()
main_window.title("Location finder using mobile number")
main_window.geometry("805x785")
main_window.resizable(False, False)


def Track_func():
    entry_number = entry_var.get()
    number = phonenumbers.parse(entry_number)

    # country
    locate_country = geocoder.description_for_number(number, 'en')
    country.config(text=locate_country)

    # ISP(Idea, Airtel, jio)
    operator = carrier.name_for_number(number, 'en')
    sim.config(text=operator)

    # timezone
    time = timezone.time_zones_for_number(number)
    zone.config(text=time)

    # latitudes and longitudes
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(locate_country)

    lng = location.longitude
    lat = location.latitude
    latitude.config(text=lat)

    # time showing on phone
    obj = TimezoneFinder()
    result = obj.timezone_at(lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)


# icon
icon = PhotoImage(
    file="M:/MOK/Study folder/Python/GUI apps with python/Phone number finder using TKinter python/Location icon.png")
main_window.iconphoto(False, icon)

# logo
logo = PhotoImage(
    file="M:/MOK/Study folder/Python/GUI apps with python/Phone number finder using TKinter python/Location icon.png")
Label(main_window, image=logo).pack()

# header text
Label(main_window, text="ENTER NUMBER TO TRACK",
      font="Roboto 24 bold").pack()

# Search bar
s_bar = PhotoImage(
    file="M:/MOK/Study folder/Python/GUI apps with python/Phone number finder using TKinter python/violet search bar (1).png")
Label(main_window, image=s_bar).place(x=170, y=280)

# Input number
entry_var = StringVar()
entry_number = Entry(main_window, textvariable=entry_var,
                     width=22, justify="center", border=0, font="Lato 20", background="#F0EEF3")
entry_number.place(x=210, y=310)


# Search button
button_image = PhotoImage(
    file="M:/MOK/Study folder/Python/GUI apps with python/Phone number finder using TKinter python/Go_white.png")
Button(main_window, image=button_image,
       borderwidth=0, cursor="hand2", bd=0, command=Track_func).pack(pady=150)

# Bottom shape
b_shape = PhotoImage(
    file="M:/MOK/Study folder/Python/GUI apps with python/Phone number finder using TKinter python/violet_bottom_gradient-transformed (1).png")
Label(main_window, image=b_shape).place(x=0, y=450)


# Tractking information
country = Label(main_window, text="Country: ", fg="black",
                font="Lato 10 bold")
country.place(x=250, y=500)

sim = Label(main_window, text="SIM: ", fg="black",
            font="Lato 10 bold")
sim.place(x=450, y=501)

zone = Label(main_window, text="TimeZone: ", fg="black",
             font="Lato 10 bold")
zone.place(x=250, y=600)

clock = Label(main_window, text="Phone Time: ", fg="black",
              font="Lato 10 bold")
clock.place(x=450, y=600)

latitude = Label(main_window, text="Latitude: ", fg="black",
                 font="Lato 10 bold")
latitude.place(x=250, y=700)

logitude = Label(main_window, text="Longitude: ", fg="black",
                 font="Lato 10 bold")
logitude.place(x=450, y=700)


# run the window
main_window.mainloop()
