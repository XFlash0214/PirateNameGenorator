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
mypirate=piratename("Sampson ", "Neyman ")
print(mypirate.createname())
