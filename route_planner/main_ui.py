import tkinter
from tkinter import *
import location


root = tkinter.Tk()
root.title('Route Planner v1.0.0')
root.geometry('600x500')


def add_to_list():
    destination = location.Location(destinations_name_entry.get(), destinations_address_entry.get())
    listbox.insert(END, destination.address)

    destinations_name_entry.delete(0, END)
    destinations_address_entry.delete(0, END)


def remove_from_list():
    listbox.delete(listbox.curselection())


def find_route():
    print(listbox.size())


# Origins Entry Setup
origins_label = tkinter.Label(root, text='Origins', font=("Courier", 20)).place(x=0, y=0)
origins_name_label = tkinter.Label(root, text='Name/Place:', font="Courier").place(x=0, y=30)
origins_name_entry = tkinter.Entry(root).place(x=90, y=30)

origins_address_label = tkinter.Label(root, text='Address:', font="Courier").place(x=0, y=60)
origins_address_entry = tkinter.Entry(root, width=40).place(x=90, y=60)

# Destinations Entry Setup
destinations_label = tkinter.Label(root, text='Destinations', font=("Courier", 20)).place(x=0, y=110)
destinations_name_label = tkinter.Label(root, text='Name/Place:', font="Courier").place(x=0, y=140)
destinations_name_entry = tkinter.Entry(root)
destinations_name_entry.place(x=90, y=140)

destinations_address_label = tkinter.Label(root, text='Address:', font="Courier").place(x=0, y=170)
destinations_address_entry = tkinter.Entry(root, width=40)
destinations_address_entry.place(x=90, y=170)

destinations_submit_button = tkinter.Button(root, text='Add Destination', command=add_to_list).place(x=90, y=200)

# Listbox Setup
listbox = tkinter.Listbox(root, width=50)
listbox.place(x=90, y=250)
destinations_remove_button = tkinter.Button(root, text='Remove Destination', command=remove_from_list).place(x=90, y=430)

# Get Route
get_route_button = tkinter.Button(root, text='Get Route', command=find_route).place(x=90, y=460)

root.mainloop()
