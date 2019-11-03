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


greybg = '#a3a3a3'
darkgreybg = '#424242'

minLabel = tk.Label(frame, bg=greybg, width=2, text=0, font=("Impact", 16))
minLabel.place(relx=0.45, rely=0.2, anchor='center')

doubledotLabel = tk.Label(frame, bg=greybg, width=1, text=':', font=("Impact", 16))
doubledotLabel.place(relx=0.5, rely=0.2,  anchor='center')

secLabel = tk.Label(frame, bg=greybg, width=2, text=0, font=("Impact", 16))
secLabel.place(relx=0.55, rely=0.2,  anchor='center')

resetIsPressed = 0

def basicStopper():
    minute = 0
    second = 0
    for x in range(second, 1200):
        if second==60:
            second = 0
            minute+=1

        secLabel.configure(text=second)
        minLabel.configure(text=minute)

        parentWindow.update()

        second += 1

        time.sleep(1)
    if resetIsPressed == 1:
        return 0

def resetStopper():
    resetIsPressed = 1
    minute = 0
    second = 0
    secLabel.configure(text=second)
    minLabel.configure(text=minute)
    sys.exit()


startButton = tk.Button(frame,bg=darkgreybg,fg='white',text='Start',command=basicStopper)
startButton.place(relx=0.3, rely=0.4, anchor='center')

stopButton = tk.Button(frame, bg=darkgreybg, fg='white', text='Stop')
stopButton.place(relx=0.5, rely=0.4, anchor='center')

resetButton = tk.Button(frame, bg=darkgreybg, fg='white', text='Reset', command=resetStopper)
resetButton.place(relx=0.7, rely=0.4, anchor='center')


#####################******************************************#####################################
####################################################################################################

parentWindow.minsize(height=height, width=width)
parentWindow.mainloop()
