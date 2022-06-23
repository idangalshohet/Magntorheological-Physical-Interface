from tkinter import *
from unittest import result
import serial
import time 
import pandas as pd

root = Tk()
root.title('GUI')

round = 1 #the value that it will be running through 
results = []

arduino = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=9600, timeout=1)

def name():
    global participant
    participant = input("What is your name:")
    print(participant)

### BUTTON INITATION ###

def ending(end):
    print('SESSION OVER') 
    print(end)
    ending = input('would you like to restart ')
    if (ending == 'yes'):
        global results
        results = []
        global round
        round = 1
    else:
        df = pd.DataFrame(results, columns=[participant])
        df.to_csv("./" + str(participant) + ".csv",index=False)
        


def which_button(button_press):
	# Printing the text when a button is clicked
    global results
    results.append(button_press)
    end = results
    global round
    round += 1 
    if round < 8: 
        trial = "round " + str(round) + " |"    
        arduino.write(trial.encode())
    else:
        ending(end)

    print(button_press)

def namestr(b, namespace):
    var1 = str([name for name in namespace if namespace[name] is b])
    # var2 = str([name for name in namespace if namespace[name] is lst[1]])
    # var3 = str([name for name in namespace if namespace[name] is lst[2]])
    # var4 = str([name for name in namespace if namespace[name] is lst[3]])

    output = (var1 + "|")
    return output

def colour_in(e):
    e['highlightbackground'] = 'green'
    # e[1]['highlightbackground'] = 'green'
    # e[2]['highlightbackground'] = 'green'
    # e[3]['highlightbackground'] = 'green'
    i = namestr((e), globals())  #gets the name of the variables from the argument to be sent back to arduino
    # print(type(send))
    arduino.write(i.encode())
    time.sleep(0.1)
    # print(arduino.readline().decode('ascii'))
 
def colour_out(e):
    e['highlightbackground'] = 'grey'
    # e[1]['highlightbackground'] = 'grey'
    # e[2]['highlightbackground'] = 'grey'
    # e[3]['highlightbackground'] = 'grey'
    # arduino.flushInput()
    # arduino.flushOutput()
    # print(str(e))

### BUTTON INITATION ### used to create bondary line around button 

frame1 = LabelFrame(root)
frame1.grid(column=1,row=1)
frame2 = LabelFrame(root)
frame2.grid(column=2,row=1)
frame3 = LabelFrame(root)
frame3.grid(column=3,row=1)

frame4 = LabelFrame(root)
frame4.grid(column=1,row=2)
frame5 = LabelFrame(root)
frame5.grid(column=2,row=2)
frame6 = LabelFrame(root)
frame6.grid(column=3,row=2)

frame7 = LabelFrame(root)
frame7.grid(column=1,row=3)
frame8 = LabelFrame(root)
frame8.grid(column=2,row=3)
frame9 = LabelFrame(root)
frame9.grid(column=3,row=3)


### BUTTON INITATION ###

bs=50  #button size

b1 = Button(frame1, text='1', bd=bs, highlightbackground='grey', command=lambda m='b1': which_button(m))
b1.pack()
b2 = Button(frame2, text='2', bd=bs, highlightbackground='grey', command=lambda m='b2': which_button(m))
b2.pack()
b3 = Button(frame3, text='3', bd=bs, highlightbackground='grey', command=lambda m='b3': which_button(m))
b3.pack()

b4 = Button(frame4, text='4', bd=bs, highlightbackground='grey', command=lambda m='b4': which_button(m))
b4.pack()
b5 = Button(frame5, text='5', bd=bs, highlightbackground='grey', command=lambda m='b5': which_button(m))
b5.pack()
b6 = Button(frame6, text='6', bd=bs, highlightbackground='grey', command=lambda m='b6': which_button(m))
b6.pack()

b7 = Button(frame7, text='7', bd=bs, highlightbackground='grey', command=lambda m='b7': which_button(m))
b7.pack()
b8 = Button(frame8, text='8', bd=bs, highlightbackground='grey', command=lambda m='b8': which_button(m))
b8.pack()
b9 = Button(frame9, text='9', bd=bs, highlightbackground='grey', command=lambda m='b9': which_button(m))
b9.pack()


### HOVER COMMAND ###

b1.bind("<Enter>", lambda event: colour_in(b1))  #identifies button when hovering
b1.bind("<Leave>", lambda event: colour_out(b1))

b2.bind("<Enter>", lambda event: colour_in(b2))  
b2.bind("<Leave>", lambda event: colour_out(b2))

b3.bind("<Enter>", lambda event: colour_in(b3))  
b3.bind("<Leave>", lambda event: colour_out(b3))

b4.bind("<Enter>", lambda event: colour_in(b4))  
b4.bind("<Leave>", lambda event: colour_out(b4))

b5.bind("<Enter>", lambda event: colour_in(b5))  
b5.bind("<Leave>", lambda event: colour_out(b5))

b6.bind("<Enter>", lambda event: colour_in(b6))  
b6.bind("<Leave>", lambda event: colour_out(b6))

b7.bind("<Enter>", lambda event: colour_in(b7))  
b7.bind("<Leave>", lambda event: colour_out(b7))

b8.bind("<Enter>", lambda event: colour_in(b8))  
b8.bind("<Leave>", lambda event: colour_out(b8))

b9.bind("<Enter>", lambda event: colour_in(b9))  
b9.bind("<Leave>", lambda event: colour_out(b9))

#UI START
start = 'starting program'
arduino.write(start.encode())

name()

# while name != None 
#     root.mainloop()

root.mainloop()

