from tkinter import *
import random
class piratename():
    originalfirst=""
    originallast=""
    firstlist=["Cap'n Fitz ","Scallywagger ", "Stupid Face ", "Blabby "]
    lastlist=["Sharkyway","Nibble","Footy","Queeker"]
    def __init__(self,firstName,lastName):
        self.originalfirst=firstName
        self.originallast=lastName
    def createname(self):
        x=random.randint(0,len(self.firstlist)-1)
        y=random.randint(0,len(self.lastlist)-1)
        return self.firstlist[x]+self.lastlist[y]
def showname():
    fn=ftext.get()
    ln=ltext.get()
    ftext.delete(0,"end")
    ltext.delete(0,"end")
    mygen=piratename(fn,ln)
    pirateoutput=mygen.createname()
    output.config(text=pirateoutput,compound=CENTER)
    
root=Tk()
root.title("Pirate Name Genorator")
myfont="Arial 20 bold"
banner=PhotoImage(file="pirate-banner.gif")
banner=banner.subsample(2,2)

title=Label(root,text="What's e'Pirate Name?",font="Arial 30 bold")
title.grid(row=0,column=0,columnspan=2)

flabel=Label(root,text="First Name",font=myfont)
flabel.grid(row=1,column=0)

llabel=Label(root,text="Last Name",font=myfont)
llabel.grid(row=2,column=0)

ftext=Entry(root,font=myfont)
ftext.grid(row=1,column=1)

ltext=Entry(root,font=myfont)
ltext.grid(row=2,column=1)

bshow=Button(root,text="Finish",font=myfont,command=showname,bg="red")
bshow.grid(row=3,column=0,columnspan=2)

output=Label(root,font="Script 30 bold",image=banner)
output.grid(row=4,column=0,columnspan=2)

mypirate=piratename("Sampson ", "Neyman ")
print(mypirate.createname())
root.mainloop()
