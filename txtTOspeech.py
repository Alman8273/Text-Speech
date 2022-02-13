from sre_parse import State
from tkinter import *
from gtts import gTTS
from playsound import playsound



root = Tk()
root.geometry('350x300')
root.resizable(0,0) #no resize
root.config(bg = '#939c86')
root.title('Text to Speech') 

#header
Label(root, text = 'Text to Speech!' , font='arial 20 bold' , bg ='#939c86').pack()
Label(root, text = 'Enter a word, phrase or sentence \n and listen to it turn to audio!' , font='arial 14' , bg ='#939c86').pack()
Label(root, text = 'After you input, just press "PLAY"' , font='arial 10' , bg ='#939c86').pack()
Label(root, text = 'Press "CLEAR" to reset text' , font='arial 10' , bg ='#939c86').pack()

#text variable
Msg = StringVar()

#Entry - make place holder (disabled on click)
def click(event) :
    entry_field.config(state=NORMAL)
    entry_field.delete(0, END)
    
entry_field = Entry(root,textvariable = Msg, bd='4', width ='50', relief=FLAT)
entry_field.insert(0, "Enter text here...")
entry_field.place(x=20 , y=180)
entry_field.config(state = DISABLED)
entry_field.bind("<Button-1>", click)

#functions
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('speech.mp3')
    playsound('speech.mp3')
    #print(speech)
    
def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, width =4).place(x=95, y=220)
Button(root, text = 'CLEAR', font='arial 15 bold', command = Reset).place(x=185, y =220)

root.mainloop()
