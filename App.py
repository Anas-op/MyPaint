import tkinter as tk #import library 
from tkinter import *
from time import time, sleep
import time
from PIL import Image
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox as mb





localtime = time.asctime( time.localtime(time.time()) )

width = 200
height = 200
color=None
s=None
size=5


colors = {
    "White":"white",
    "Green": "green",
    "Red": "red",
    "Cyan": "cyan",
    "Magenta": "magenta",
    "Yellow": "yellow",
    "Black": "black",
	"Gold": "gold",
	"LightBlue":"lightblue",
	"Lime":"lime",
	"Blue":"blue",
	"darkGreen":"darkgreen",
	"darkGrey":"darkgrey",
    "Grey":"grey",
	"Orange":"orange",
	"SkyBlue":"deepskyblue",
	"FireBrick":"firebrick",
	"DarkViolet":"darkviolet",
	"DarkMagenta":"darkmagenta",
	"DarkPink":"deeppink",
	"Brown":"brown",
	 "Pink":"pink",
}

Sizes={

    'Small':5,
    'Medium':15,
    'Large':25
}

cursors=['spraycan', 'circle']


colorSelected=colors['Black']



def sendMail (auto=True):
    import win32com.client as win32 
    import pathlib
    import os

    a=str(pathlib.Path().absolute())   #converts path in string
    convertedPath=a.replace(os.sep, '/')             #replace \ with / and put the path in variable c
    pathWork='/Projects/Work.png'                    #defining the path of saved work
    fullPath=(convertedPath+pathWork)               #concatenate project path with saved work path and saving them into a variable                               
    #print(fullPath)  this is atest
    outlook = win32.Dispatch('outlook.application')
    attachment=fullPath                                   #assigning fullPath to attachment
    mail = outlook.CreateItem(0)
    mail.To = ""
    mail.Subject = "My Paint Project"
    mail.HtmlBody = "Hey, take a look at my drawing!"
    mail.Attachments.Add(attachment)                               #getting the path to attach the Work
    if auto:
        mail.Display(True)
    else:
        mail.open 

def message():
    mb.showinfo('Completed','Work has been succesfully saved in your Projecs folder!')
    root.title('Work saved')
    sleep(2)
    root.title('My Paint')

def saveWork():
    canvas1.postscript(file="./Projects/tmp/Progetto_TMP.eps")
    
    root.title('Saving...')
    root.after(2000,message)
    img = Image.open("./Projects/tmp/Progetto_TMP.eps")
    i=img.save("./Projects/Work.png", "png")
    return i
    
def colorSelection(value):
    global colorSelected
    colorSelected = value
    global size
    size = Sizes['Small']
    smallBar['bg']=colors['Black']
    LargeBar['bg']=colors['White']
    MediumBar['bg']=colors['White']
    canvas1['cursor']=cursors[0]

def sizeSelection(s):
       global size
       size = s

def on_enter(event):
    
    sizeBar['bg']= colors['darkGrey']
    

    
def on_leave(event):
   
    sizeBar['bg']= colors['White']



def Rubber(value):
     global colorSelected
     global size
     size=5
     colorSelected = value
     smallBar['bg']=colors['Black']
     LargeBar['bg']=colors['White']
     MediumBar['bg']=colors['White']
     canvas1['cursor']=cursors[1]

def selectedBar(v,sz):
    global size
    size=sz
    bar=v
    if bar==smallBar:
         bar['bg']=colors['Black']
         LargeBar['bg']=colors['White']
         MediumBar['bg']=colors['White']
    elif bar==MediumBar:
         bar['bg']=colors['Black'] 
         smallBar['bg']=colors['White']
         LargeBar['bg']=colors['White']
    elif bar==LargeBar:
         bar['bg']=colors['Black'] 
         smallBar['bg']=colors['White']
         MediumBar['bg']=colors['White']



#def colorSelection(event):
      #  global color
      #  color=s

def clearCanvas():
    global size
    canvas1.delete("all") 
    smallBar['bg']=colors['Black']
    LargeBar['bg']=colors['White']
    MediumBar['bg']=colors['White']
    size=5
    


def paint(event):
        x1,y1=(event.x-1),(event.y-1)
        x2,y2=(event.x+size),(event.y+size)
        canvas1.create_oval(x1,y1,x2,y2,fill=colorSelected,outline=colorSelected)





HEIGHT= 650
WIDTH= 650


root=tk.Tk()  #the root contains everything
root.title('My Paint')



canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH) 
canvas.pack() 
root.geometry('+500+100')#distance based on computer screen
root.geometry('650x650')#screen size of tkinter app
root.resizable(0,0)  #not resizable

canvas1=tk.Canvas(canvas,bg=colors['White']) 
canvas1.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor="n")
canvas1.config(cursor=cursors[0])

#toolbar
toolbar = Frame(root, bg=colors['White'], height=30)
toolbar.place(relx=0, rely=0, relwidth=1)

#saveButton
saveIcon = PhotoImage(file="./icons/Save-icon.png")
saveButton=tk.Button(toolbar, bg=colors['darkGrey'],width=50, command=saveWork,image=saveIcon, compound='left',text="Save", fg=colors['Black'], font=('Helvetica 18 bold',10))
saveButton.pack(side='left')

#sendButton
sendIcon = PhotoImage(file="./icons/Mail-icon.png")
sendButton=tk.Button(toolbar, bg=colors['darkGrey'], width=50, command=sendMail,image=sendIcon, compound='left',text='Send' ,fg=colors['Black'], font=('Helvetica 18 bold',10) )
sendButton.pack(side='left')

#Selection bar in the upper
bar=tk.Frame(root, bg=colors['Grey'], border=5)
bar.place(relx=0, rely=0.04, relwidth=1, relheight=0.15)


#colors selection buttons
color1=tk.Button(bar, bg=colors['Black'], height=1, width=1, command=lambda *args: colorSelection(colors['Black'])) 
color1.grid(row=0,column=0, pady=5, padx=5)

color2=tk.Button(bar, bg=colors['Green'], height=1, width=1, command=lambda *args: colorSelection(colors['Green'])) 
color2.grid(row=1,column=0, pady=5, padx=5)


color3=tk.Button(bar,bg=colors['Red'],  height=1, width=1, command=lambda *args: colorSelection(colors['Red'])) 
color3.grid(row=0,column=1, pady=5, padx=5)

color4=tk.Button(bar, bg=colors['Cyan'],  height=1, width=1, command=lambda *args: colorSelection(colors['Cyan'])) 
color4.grid(row=1,column=1, pady=5, padx=5)

color5=tk.Button(bar, bg=colors['Magenta'],  height=1, width=1, command=lambda *args: colorSelection(colors['Magenta'])) 
color5.grid(row=0,column=2, pady=5, padx=5)

color6=tk.Button(bar, bg=colors['Yellow'],  height=1, width=1, command=lambda *args: colorSelection(colors['Yellow']))
color6.grid(row=1,column=2, pady=5, padx=5)

color7=tk.Button(bar, bg=colors['Gold'], height=1, width=1, command=lambda *args: colorSelection(colors['Gold'])) 
color7.grid(row=0,column=3, pady=5, padx=5)

color8=tk.Button(bar, bg=colors['LightBlue'], height=1, width=1, command=lambda *args: colorSelection(colors['LightBlue'])) 
color8.grid(row=1,column=3, pady=5, padx=5)

color9=tk.Button(bar, bg=colors['Lime'], height=1, width=1, command=lambda *args: colorSelection(colors['Lime'])) 
color9.grid(row=0,column=4, pady=5, padx=5)

color10=tk.Button(bar, bg=colors['Blue'], height=1, width=1, command=lambda *args: colorSelection(colors['Blue'])) 
color10.grid(row=1,column=4, pady=5, padx=5)

color11=tk.Button(bar, bg=colors['darkGreen'], height=1, width=1, command=lambda *args: colorSelection(colors['darkGreen'])) 
color11.grid(row=0,column=5, pady=5, padx=5)

color12=tk.Button(bar, bg=colors['darkGrey'], height=1, width=1, command=lambda *args: colorSelection(colors['darkGrey'])) 
color12.grid(row=1,column=5, pady=5, padx=5)

color13=tk.Button(bar, bg=colors['SkyBlue'], height=1, width=1, command=lambda *args: colorSelection(colors['SkyBlue'])) 
color13.grid(row=0,column=6, pady=5, padx=5)

color14=tk.Button(bar, bg=colors['Orange'], height=1, width=1, command=lambda *args: colorSelection(colors['Orange'])) 
color14.grid(row=1,column=6, pady=5, padx=5)

color15=tk.Button(bar, bg=colors['FireBrick'], height=1, width=1, command=lambda *args: colorSelection(colors['FireBrick'])) 
color15.grid(row=0,column=7, pady=5, padx=5)

color16=tk.Button(bar, bg=colors['DarkViolet'], height=1, width=1, command=lambda *args: colorSelection(colors['DarkViolet'])) 
color16.grid(row=1,column=7, pady=5, padx=5)

color17=tk.Button(bar, bg=colors['DarkMagenta'], height=1, width=1, command=lambda *args: colorSelection(colors['DarkMagenta'])) 
color17.grid(row=0,column=8, pady=5, padx=5)

color18=tk.Button(bar, bg=colors['DarkPink'], height=1, width=1, command=lambda *args: colorSelection(colors['DarkPink'])) 
color18.grid(row=1,column=8, pady=5, padx=5)

color19=tk.Button(bar, bg=colors['Brown'], height=1, width=1, command=lambda *args: colorSelection(colors['Brown'])) 
color19.grid(row=0,column=9, pady=5, padx=5)

color19=tk.Button(bar, bg=colors['Pink'], height=1, width=1, command=lambda *args: colorSelection(colors['Pink'])) 
color19.grid(row=1,column=9, pady=5, padx=5)

#buttons=[color1,color2,color3,color4,color5,color6]

canvas1.bind('<B1-Motion>', paint)

#rubber icon
iconRubber = PhotoImage(file="./icons/rubber.png")

#bar divisor
divBar=tk.Frame(bar, bg=colors['Black'], bd=10)
divBar.place(relx=0.42, relheight=1, relwidth=0.01)


#RUBBER
#rubber icon
iconRubber = PhotoImage(file="./icons/rubber.png")
rubber=tk.Button(bar, bg=colors['White'], height=20, width=20, image=iconRubber, command=lambda *args: Rubber(colors['White']))
rubber.grid(row=0, column=10, padx=30)





#clear work icon
clearIcon = PhotoImage(file="./icons/clear.png")
clearButton=tk.Button(bar, bg=colors['Grey'],text='Clear',fg="black",compound=LEFT, height=30, width=50, image=clearIcon, command=lambda *args: clearCanvas())
clearButton.grid(row=1, column=10, padx=30)
clearButton['border']='0'



sizeBar=tk.Frame(bar, bg=colors['White'])
sizeBar.place(relheight=1, relwidth=0.20, relx=0.80)

sizeBar.bind('<Enter>',on_enter)
sizeBar.bind('<Leave>',on_leave)





smallBar=tk.Button(sizeBar, bg=colors['Black'], height=1, width=100, command= lambda *args: selectedBar(smallBar,Sizes['Small']))
smallBar.place(relheight=0.10, relwidth=0.75, relx=0.10, rely=0.10)
MediumBar=tk.Button(sizeBar, bg=colors['Black'], height=1, width=100, command= lambda *args:selectedBar(MediumBar,Sizes['Medium']))
MediumBar.place(relheight=0.20, relwidth=0.75, relx=0.10, rely=0.30)
LargeBar=tk.Button(sizeBar, bg=colors['Black'], height=1, width=100, command= lambda *args:selectedBar(LargeBar,Sizes['Large']))
LargeBar.place(relheight=0.30, relwidth=0.75, relx=0.10, rely=0.60)











clockTime=tk.Frame(root, bg=colors['darkGrey'])
clockTime.place(rely=0.96,relx=0, relwidth=1, relheight=1)


time=tk.Label(clockTime, bg=colors['darkGrey'],text=localtime, fg=colors['Black'], font=('Helvetica 18 bold',10))
time.config(anchor="center")
time.pack()



#background

background_image = PhotoImage(file="./icons/paint.png")
background = Label(canvas, image=background_image, bd=0)
background.place(relwidth=1, relheight=1)




tk.Misc.lift(canvas1)
root.mainloop() 

































































#label=tk.Label(frame, text="this is a label", bg="yellow")   #text label widget
                                       #fill fills given space to both places up and down based on text size, expand gives position to full space or just x or just y
#label.place(relx=0.3,rely=0,relwidth=0.45,relheight=0.25)



#entry=tk.Entry(frame, font=30)   # input text label #font sets font text
#entry.place(relwidth=0.65,relheight=1)  #using grid you can define position based on columns and rows like css grid


#button=tk.Button(frame, text="test button", font=40)  #create button
#button.grid(row=0,column=0) #replaces place.()   #check manual.     side="position" describes position where i want to pack element
#button.place(relx=0.7,relwidth=0.3,relheight=1)      # using 1 we fit the element to his parent so his 


#body=tk.Frame(root, bg="grey", bd=5)
#body.place(relx=0.5, rely=0.20, relwidth=0.75, relheight=0.6, anchor='n')

#label=tk.Label(body, text="this is a label", bg="yellow") 
#label.place(relwidth=1,relheight=1)
#frame.place(relx=0.5, rely=0.1,relwidth=0.25, relheight=0.25,anchor="s")  #relwidth/ height define resolution 