# Imports
import time
import keyboard
from tkinter import *
from win11toast import toast

# Setup Main Window: Initial Sizing and defining

MainWindow = Tk()
MainWindow.geometry("300x345")
MainWindow.title("Water Reminder Hub")
MainWindow.resizable(False, False)

# Seting Up global variables - these may be altered throughout the program in different functions

global NotificationMessage
global DurationTime
global OpenProgramKey

# Initializing these variables - these values are the basics

NotificationMessage = "Please take a break and grab some water!"
DurationTime = 60
OpenProgramKey = "]"

# Decorating or adding to the window
def DecorateMainWindow():
    # Grabbing the global variables
    global NotificationMessage
    global DurationTime
    global OpenProgramKey

    # Defining constant vars
    backGroundColor = "#31afda"  # <-- Hex Color
    MainWindow.config(bg=backGroundColor)

    # MainWindow.grid_columnconfigure(0, weight=1) # Centers all labels

    # Functions

    # Adds a space between two labels or elements
    def Space(Row):
        Spacing = Label(MainWindow, text="", bg=backGroundColor)
        Spacing.grid(row=Row)

    def SubmitAll():
        # Grabbing the global variables
        global NotificationMessage
        global DurationTime
        global OpenProgramKey

        try:
            DurationTime = int(DurationEntry.get())
            DurationEntry.delete(0, END)
            print(DurationTime)
        except ValueError:
            print("Not a number")

        if len(MessageEntry.get()) > 0:
            NotificationMessage = MessageEntry.get()
            MessageEntry.delete(0, END)
            print(NotificationMessage)

        if len(OpenKey.get()) == 1:
            OpenProgramKey = OpenKey.get()
            OpenKey.delete(0, END)
            print(OpenProgramKey)

    def StopAll():
        quit()

    # Main Decoration

    MainWinTitle = Label(MainWindow, text="Water Reminder Hub", font=("comfortaa", 15, "bold"), fg="#1255bf",
                         bg=backGroundColor)
    MainWinTitle.grid(row=0, column=0)

    DecorationBegin = Label(MainWindow, text="╔═══━━━━──── • ────━━━━═══╗", fg="yellow", bg=backGroundColor)
    DecorationBegin.grid(row=1, column=0)

    Space(2)

    LB1 = Label(MainWindow, text="Duration (Minutes) between reminders", bg=backGroundColor, fg="black")
    LB1.grid(row=3)

    DurationEntry = Entry(MainWindow, width=5, borderwidth=3, bg="#bbd6ff", fg="black")
    DurationEntry.grid(row=4, column=0)
    DurationEntry.insert(0, str(DurationTime))

    LB2 = Label(MainWindow, text="Message in each reminder", bg=backGroundColor, fg="black")
    LB2.grid(row=5)

    MessageEntry = Entry(MainWindow, width=40, borderwidth=3, bg="#85aae2", fg="black")
    MessageEntry.grid(row=6, column=0)
    MessageEntry.insert(0, str(NotificationMessage))

    LB3 = Label(MainWindow, text="Key to re-open window", bg=backGroundColor, fg="black")
    LB3.grid(row=7)

    OpenKey = Entry(MainWindow, width=3, borderwidth=3, bg="#2f4e7f", fg="white")
    OpenKey.grid(row=8, column=0)
    OpenKey.insert(0, str(OpenProgramKey))

    Space(9)

    SubmitAll = Button(MainWindow, text="Submit", borderwidth=3, font=("Comfortaa", 10), bg="gold", fg="black",
                       command=SubmitAll)
    SubmitAll.grid(row=10, column=0)

    LB4 = Label(MainWindow, text="< Close Window to begin >", font=("Comfortaa", 7), bg=backGroundColor, fg="yellow")
    LB4.grid(row=11)

    DecorationEnd = Label(MainWindow, text="════━━━━──── • ────━━━━════", fg="yellow", bg=backGroundColor)
    DecorationEnd.grid(row=12, column=0)

    StopAllButton = Button(MainWindow, text="STOP ALL", borderwidth=3, font=("Comfortaa", 10, "bold"), bg="red",
                           fg="black", command=StopAll)
    StopAllButton.grid(row=13, column=0)

    Credits = Label(MainWindow, text="All Rights Reserved ©Michael Audi 2024", font=("Comfortaa", 8, "bold"),
                    bg=backGroundColor, fg="black")
    Credits.grid(row=14, column=0)


DecorateMainWindow()
MainWindow.mainloop()

toast('Computer: Water Break', 'Program is active working in the background! Press " ' + OpenProgramKey + ' " to re-open the program!')

while True:
    breakException = True
    print(DurationTime * 60)

    # This is simply set in a loop so that the program can constantly detect if the user is attempting to
    # re-open the hub (holding down the designated "OpenProgramKey" button)
    for i in range(DurationTime * 60 * 2):
        time.sleep(0.5)

        if keyboard.is_pressed(OpenProgramKey):  # Open back up hub
            MainWindow = Tk()
            MainWindow.geometry("300x345")
            MainWindow.title("Water Reminder Hub")

            MainWindow.resizable(False, False)

            DurationTimeBefore = DurationTime  # if they changed the duration, start timer over

            DecorateMainWindow()
            MainWindow.mainloop()

            if DurationTimeBefore != DurationTime:  # if they changed the duration, start timer over
                toast('Computer: Water Break', 'Program is active working in the background! Press " ' + OpenProgramKey + ' " to re-open the program!')
                breakException = False
                break

        print(i / 2)

    if breakException:
        toast('Computer: Water Break', NotificationMessage)
