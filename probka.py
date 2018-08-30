from Tkinter import *      

 

global ap

 

def zamknij():

    print ap.imie.get(),'jest',

    if ap.opis:

        if ap.kobieta.get() == YES:

            for i in range(0,len(ap.opis)):

                ap.opis[i]=ap.opis[i][:-1]+'a'

        if len(ap.opis) == 1:

            print ap.opis[0]

        else:

            for i in range(0,len(ap.opis)-1):

                print ap.opis[i]+',',

            print 'a przede wszystkim',ap.opis[len(ap.opis)-1]

    else:

        print "jaki jest"

    ap.quit()

    ap.master.destroy()

 

def dopisz(jaki):

    ap.opis.append(jaki)

 

class Aplikacja(Frame):             

    def __init__(aplikacja, nadrzedna=None):

        Frame.__init__(aplikacja, nadrzedna)  

        aplikacja.grid()                   

        aplikacja.przygotuj()

        aplikacja.opis=[]

       

    def przygotuj(aplikacja):

        aplikacja.imie = Entry (aplikacja)

        aplikacja.imie.insert(0,"On")

        aplikacja.imie.grid(row=0,column=0,columnspan=3,sticky=E+W)

        aplikacja.kobieta = IntVar()

        aplikacja.plec = Checkbutton(aplikacja, text='Kobieta',

                  variable=aplikacja.kobieta)

        aplikacja.plec.grid(row=1,column=0,columnspan=3,sticky=E+W)

        aplikacja.przyciski=()

        epitety=['wielki','wspanialy','drogi','mocarny','genialny',

'perfekcyjny','nieomylny','idealny','niezastapiony']

        for i in range(9):

          aplikacja.przyciski=aplikacja.przyciski+\

                (Button ( aplikacja, text=epitety[i],

                command=lambda x=epitety[i]:dopisz(x) ),)

aplikacja.przyciski[i].grid(row=2+i/3,

column=i%3,sticky=E+W)        

 

        aplikacja.koniec = Button ( aplikacja, text="Koniec",

            command=zamknij )

        aplikacja.koniec.grid(row=5,column=0,columnspan=3,sticky=E+W)        

 

ap = Aplikacja()                   

ap.master.title("Sympatyk")

ap.mainloop() 

 