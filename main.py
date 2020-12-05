import tkinter
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont
from tkinter import messagebox

gas = 0
temp = 20
loc = 1
alarm_state = False
window_state = False
switch_state = False


def up_arrow_button_clicked():
    global loc
    loc = loc + 1
    update_values()


def down_arrow_button_clicked():
    global loc
    loc = loc - 1
    update_values()


def arm_button_clicked():
    global alarm_state
    if alarm_state:
        alarm_state = False
    else:
        alarm_state = True
    update_values()


def switch_button_clicked():
    global switch_state
    if switch_state:
        switch_state = False
    else:
        switch_state = True
    update_values()


def help_button_clicked():
    messagebox.showinfo("Instructions", "This is a simple monitoring and alarm system.\n" +
                        "System displays number of gas cells per 1m^3, temperature, " +
                        "if windows are closed and state of alarm.\n " +
                        "Additionally you are able to turn on/off monitoring system" +
                        "and arm the alarm")


def update_values():
    label_loc.config(text=str(loc))
    if alarm_state:
        text2 = "Arm the alarm"
        label_alarm.config(text="armed")
    else:
        text2 = "Disarm the alarm"
        label_alarm.config(text="unarmed")
    arm_button.config(text=text2)
    if switch_state:
        text3 = "Turn on"
    else:
        text3 = "Turn off"
    switch_button.config(text=text3)


root = tk.Tk()
font_style_labels = tkFont.Font(root=root, family="Helvetica", size=25)
canvas = tk.Canvas(root, height=400, width=1000, bg="#C9ECEA")
canvas.pack()

# Labels
label_location = tk.Label(root, bg="#C9ECEA", text="Current room number: ", font=font_style_labels)
label_location.place(x=50, y=50)
label_loc = tk.Label(root, bg="#C9ECEA", text=str(loc), font=font_style_labels)
label_loc.place(x=380, y=50)
label_gas = tk.Label(root, bg="#C9ECEA", text=str(gas), font=font_style_labels)
label_gas.place(x=265, y=250)
label_temp = tk.Label(root, bg="#C9ECEA", text=str(temp), font=font_style_labels)
label_temp.place(x=405, y=250)
label_window = tk.Label(root, bg="#C9ECEA", text="closed", font=font_style_labels)
label_window.place(x=525, y=250)
if alarm_state:
    text = "armed"
else:
    text = "unarmed"
label_alarm = tk.Label(root, bg="#C9ECEA", text=text, font=font_style_labels)
label_alarm.place(x=675, y=250)

# Images
up_arrow_img = ImageTk.PhotoImage(file="./icons/up_arrow.png")
down_arrow_img = ImageTk.PhotoImage(file="./icons/down_arrow.png")
gas_icon = ImageTk.PhotoImage(Image.open("./icons/gas_icon.png"))
temp_icon = ImageTk.PhotoImage(Image.open("./icons/temp_icon.jpg"))
window_icon = ImageTk.PhotoImage(Image.open("./icons/window_icon.png"))
alarm_icon = ImageTk.PhotoImage(Image.open("./icons/alarm_icon.png"))
help_icon = ImageTk.PhotoImage(Image.open("./icons/help_icon.png"))

# Buttons
up_arrow_button = tk.Button(root, command=up_arrow_button_clicked, image=up_arrow_img)
up_arrow_button.place(x=413, y=42)
down_arrow_button = tk.Button(root, command=down_arrow_button_clicked, image=down_arrow_img)
down_arrow_button.place(x=413, y=67)
help_button = tk.Button(root, image=help_icon, command=help_button_clicked)
help_button.place(x=50, y=300)
if alarm_state:
    text = "Arm the alarm"
else:
    text = "Disarm the alarm"
arm_button = tk.Button(root, text=text, font="Helvetica", command=arm_button_clicked)
arm_button.config(height=3, width=13, bg="#C9ECEA")
arm_button.place(x=700, y=300)
if switch_state:
    text = "Turn on"
else:
    text = "Turn off"
switch_button = tk.Button(root, text=text, font="Helvetica", command=switch_button_clicked)
switch_button.config(height=3, width=13, bg="#C9ECEA")
switch_button.place(x=850, y=300)

# Icons
panel = tk.Label(root, image=gas_icon)
panel.place(x=225, y=150)
panel = tk.Label(root, image=temp_icon)
panel.place(x=375, y=150)
panel = tk.Label(root, image=window_icon)
panel.place(x=525, y=150)
panel = tk.Label(root, image=alarm_icon)
panel.place(x=675, y=150)

root.mainloop()





