# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:42:32 2016

@author: ddan
"""

import Tkinter as tk

#Creating a window
app = tk.Tk()
app.title('Pomodoro Timer')
#app.geometry('450x300+200+200')

#Creating Frames
top_left = Frame(app)
top_right= Frame(app)
bottom_frame = Frame(app)
top_left.grid(row=0,column=0)
top_right.grid(row=0,column=1)
bottom_frame.grid(columnspan=2)

labelText = StringVar()
labelText.set('Click this button')
label1 = Label(top_left,textvariable=labelText) #height controls position of the text
label1.pack()

button1 = tk.Button(top_right,text='hello')
button1.pack(side='bottom')

starting_value=StringVar()
starting_value.set('25')
working_time = tk.Spinbox(bottom_frame,from_=0,to=60,textvariable=starting_value)
working_time.pack()

app.mainloop()


#def count_down():
#    # start with 2 minutes --> 120 seconds
#    for t in range(120, -1, -1):
#        # format as 2 digit integers, fills with zero to the left
#        # divmod() gives minutes, seconds
#        sf = "{:02d}:{:02d}".format(*divmod(t, 60))
#        #print(sf)  # test
#        time_str.set(sf)
#        root.update()
#        # delay one second
#        time.sleep(1)
