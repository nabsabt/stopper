import time
import sys
import tkinter as tk
height = 600
width = 400


parentWindow = tk.Tk()
canvas = tk.Canvas(parentWindow, height=height, width=width)
canvas.place()

frame = tk.Frame(parentWindow, bg='#a3a3a3')
frame.place(relwidth = 1, relheight = 1)
####################################################################################################
#####################******************************************#####################################

minute = 0
second = 0
greybg = '#a3a3a3'
darkgreybg = '#424242'

minLabel = tk.Label(frame, bg=greybg, width=2, text=minute, font=("Impact", 16))
minLabel.place(relx=0.45, rely=0.2, anchor='center')

doubledotLabel = tk.Label(frame, bg=greybg, width=1, text=':', font=("Impact", 16))
doubledotLabel.place(relx=0.5, rely=0.2,  anchor='center')

secLabel = tk.Label(frame, bg=greybg, width=2, text=second, font=("Impact", 16))
secLabel.place(relx=0.55, rely=0.2,  anchor='center')

def basicStopper():
    for x in range(59):
        x += 1
        time.sleep(1)
        sys.stdout.flush()
        secLabel.configure(text=x)

startButton = tk.Button(frame,bg=darkgreybg,fg='white',text='Start',command=basicStopper)
startButton.place(relx=0.5, rely=0.4, anchor='center')



#####################******************************************#####################################
####################################################################################################

parentWindow.minsize(height=height, width=width)
parentWindow.mainloop()

