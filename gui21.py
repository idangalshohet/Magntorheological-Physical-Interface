from tkinter import *
from unittest import result
import serial
import time 
import pandas as pd

root = Tk()
root.title('GUI')

# var = StringVar()
# var = round 

round = 1 #the value that it will be running through 
results = [] #participant answers
lastside = None  #tracks the last corner for more intuative mouse interactions 

arduino = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=9600, timeout=1)

def name():
    global participant
    participant = input("What is your name:")
    lname.config(text = str(participant))

### BUTTON INITATION ###

def back():
    
    global round
    if round > 1:
        round -= 1 
        llabel.config(text = 'round ' + str(round))

def ending(end):
    print('SESSION OVER') 
    print(end)
    # ending = input('would you like to restart ')
    # if (ending == 'yes'):
    #     global results
    #     results = []
    #     global round
    #     round = 1
    # else:
    df = pd.DataFrame(results, columns=[participant])
    df.to_csv("./" + str(participant) + ".csv",index=False)   


def which_button(button_press):
	# Printing the text when a button is clicked
    global results
    results.append(button_press)
    end = results
    global round
    round += 1 
    llabel.config(text = 'Round ' + str(round))
    if round <= 18: 
        trial = "round " + str(round) + " |"    
        arduino.write(trial.encode())
    else:
        ending(end)

    print(button_press)

def namestr(lst, namespace):
    var1 = str([name for name in namespace if namespace[name] is lst[0]])
    var2 = str([name for name in namespace if namespace[name] is lst[1]])
    # var3 = str([name for name in namespace if namespace[name] is lst[2]])
    # var4 = str([name for name in namespace if namespace[name] is lst[3]])
    global output
    corner = [var1, var2]
    cornerfind(corner)
    output = (var1 + var2 + "|")
    return output

def colour_in(e):
    e[0]['highlightbackground'] = 'green'
    e[1]['highlightbackground'] = 'green'
    # e[2]['highlightbackground'] = 'green'
    # e[3]['highlightbackground'] = 'green'
    i = namestr((e), globals())  #gets the name of the variables from the argument to be sent back to arduino
    arduino.write(i.encode())
    time.sleep(0.1)
 
def colour_out(e):
    e[0]['highlightbackground'] = 'grey'
    e[1]['highlightbackground'] = 'grey'


    
def cornerfind(l):
    global lastcorner
    global b2in
    global b4in
    global b5in
    global b6in
    global b8in
    if ("['b1']" in l) or ("['b4']" in l) or ("['b7']" in l): 
        # print('left side')
        lastside = 'left'
        b2in = [b1,b2]
        b5in = [b4,b5]
        b8in = [b7,b8]
    elif ("['b3']" in l) or ("['b6']" in l) or ("['b9']" in l): 
        # print('right side')
        lastside = 'right'
        b2in = [b2, b3]
        b5in = [b5, b6]
        b8in = [b8, b9]
    else:
        print('none found')

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

frame10 = LabelFrame(root)  #place to put name and back button 
frame10.grid(column=1, row=4, columnspan=3)


### BUTTON INITATION ###

bs=50  #button size

b1 = Button(frame1, text='1', bd=bs, highlightbackground='grey', command=lambda m='1': which_button(m))
b1.pack()
b2 = Button(frame2, text='2', bd=bs, highlightbackground='grey', command=lambda m='2': which_button(m))
b2.pack()
b3 = Button(frame3, text='3', bd=bs, highlightbackground='grey', command=lambda m='3': which_button(m))
b3.pack()

b4 = Button(frame4, text='4', bd=bs, highlightbackground='grey', command=lambda m='4': which_button(m))
b4.pack()
b5 = Button(frame5, text='5', bd=bs, highlightbackground='grey', command=lambda m='5': which_button(m))
b5.pack()
b6 = Button(frame6, text='6', bd=bs, highlightbackground='grey', command=lambda m='6': which_button(m))
b6.pack()

b7 = Button(frame7, text='7', bd=bs, highlightbackground='grey', command=lambda m='7': which_button(m))
b7.pack()
b8 = Button(frame8, text='8', bd=bs, highlightbackground='grey', command=lambda m='8': which_button(m))
b8.pack()
b9 = Button(frame9, text='9', bd=bs, highlightbackground='grey', command=lambda m='9': which_button(m))
b9.pack()

llabel = Label(frame10, text = 'Round 1', font = ("helvetica", 18))
llabel.grid(column=1, row=1, pady=5, padx = 5)
lname = Label(frame10, text = 'Insert Name', font = ("helvetica", 18))
lname.grid(column=2, row=1, pady=5, padx = 5)
bback = Button(frame10, text='back', command=lambda: back())
bback.grid(column=3, row=1, pady=5)




### HOVER COMMAND ###

b2in = [b1,b2]  #inital button hover outputs 
b4in = [b4,b5]
b5in = [b1,b2]
b6in = [b5,b6]
b8in = [b7,b8]

b1.bind("<Enter>", lambda event: colour_in([b1,b2]))  #identifies button when hovering
b1.bind("<Leave>", lambda event: colour_out([b1,b2]))

b2.bind("<Enter>", lambda event: colour_in(b2in))  
b2.bind("<Leave>", lambda event: colour_out(b2in))
  
b3.bind("<Enter>", lambda event: colour_in([b2,b3]))  
b3.bind("<Leave>", lambda event: colour_out([b2,b3]))

b4.bind("<Enter>", lambda event: colour_in([b4,b5]))  
b4.bind("<Leave>", lambda event: colour_out([b4,b5]))

b5.bind("<Enter>", lambda event: colour_in(b5in))  
b5.bind("<Leave>", lambda event: colour_out(b5in))

b6.bind("<Enter>", lambda event: colour_in([b5,b6]))  
b6.bind("<Leave>", lambda event: colour_out([b5,b6]))

b7.bind("<Enter>", lambda event: colour_in([b7, b8]))  
b7.bind("<Leave>", lambda event: colour_out([b7, b8]))

b8.bind("<Enter>", lambda event: colour_in(b8in))  
b8.bind("<Leave>", lambda event: colour_out(b8in))

b9.bind("<Enter>", lambda event: colour_in([b8, b9]))  
b9.bind("<Leave>", lambda event: colour_out([b8, b9]))

#UI START
start = 'starting program'
arduino.write(start.encode())

name()
root.mainloop()

