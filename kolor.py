#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.1'
__comment__ = 'Obliczanie honorarium Architekta'
 
__inputs__ = [
    'Honorarium za usługi projektowe: ',
    'Honorarium za nadzór autorski: ',
    'Honorarium za usługi dodatkowe: ',
]




'''
W=HP+HN+HD
HP – honorarium Architekta za usługi projektowe – wg punktu 5;
HN – honorarium za nadzór autorski – wg punktu 6;
HD – honorarium za usługi dodatkowe – wg punktu 7;
'''
def wynarch(HP, HN, HD):
 
    WA = HP+HN+HD
 
    return 'Wynagrodzenie architekta: %s PLN' % WA


 
'''
5. HONORARIUM ZA USŁUGI PROJEKTOWE – HP
Honorarium ustalane jest jako procent od przewidywanego kosztu budowy obiektu wg wzoru:
HP = K x W x P
gdzie:
K – koszt budowy – wg punktu 5.1;
W – wskaźnik procentowy – wg punktu 5.2.
P – mnożnik za powiększenia i pomniejszenia zakresu prac projektowych w stosunku do standardowych wymagań – wg punktu 5.3.
Honorarium (HP), dla inwestycji obejmującej więcej niż jeden obiekt wylicza się jako sumę honorariów dla poszczególnych obiektów z doliczeniem 3 – 10% za ich wzajemną koordynację.
'''
def wynHP():
 
    oblHP = Kb * WskP * mnP
 
    return oblHP

'''
5.1. Ustalanie kosztu budowy – K
5.1.1. Koszt budowy winien być oszacowany rzetelnie i w uzgodnieniu z Klientem. W podstawie wyceny należy uwzględnić wszystkie te, i tylko te, składniki, które mają odzwierciedlenie w projekcie.
5.1.2. Na koszt budowy13 (K) składają się14:
Kp – koszty przygotowania terenu – niwelacja, rozbiórki, przebudowa infrastruktu-ry kolidującej z inwestycją, przygotowanie placu budowy,
Ko – koszty budowy obiektów – wszystkie podstawowe i pomocnicze obiekty w pełnym zakresie (architektura, konstrukcja, instalacje),
Kt – koszty zagospodarowania terenu (DFA, drogi, sieci i przyłącza, oświetlenie, zieleń).
K = Kp + Ko + Kt
'''
def kosztBud():
 
    oblKb = Kp + Ko + Kt
 
    return oblKb
'''
5.1.3. Koszt inwestycji (K) wylicza się jako iloczyn wskaźnika kosztu 1 m2 (wk)15 obiek-tu(ów) podobnego(nych), zrealizowanego(nych) w danym regionie i wyrażonej w m2 powierzchni (P) projektowanego obiektu(ów)16.
K = P x wk
5.1.4. Jeżeli wskaźnik wk odnosi się tylko do Ko lub Ko + Kt koszt tych składowych nale-ży wyliczać w oparciu iloczyn wk x P a koszty pozostałe na podstawie odrębnych analiz.
5.1.5. W przypadku braku danych, w szczególności w odniesieniu do inwestycji o szcze-gólnych wymaganiach i programie, które nie mają zrealizowanych odpowiedników w danym regionie, podstawą mogą być, odpowiednio skorygowane, koszty budo-wy podobnych inwestycji w innych częściach kraju lub za granicą albo analizy własne.
5.1.6. Szczególne okoliczności jakie w konkretnym, rozpatrywanym przypadku mogą zmniejszyć lub zwiększyć koszt inwestycji w stosunku do opisanego w punkcie 5.1.3 (np. okazyjne zakupy materiałów i robocizny, korzystanie z darowizn, wbu-dowanie posiadanych materiałów itp.) nie wpływają na koszt inwestycji, który na-leży przyjmować jako podstawę wyliczenia honorarium.
'''
def kosztInw():
 
    oblKi = Pow * WskK
 
    return oblKb

#kategorie obiektów
def wybKat():
 
    oblKi = Pow * WskK
 
    return oblKb

from Tkinter import *
from tkinter import ttk
import Tkinter as tk
import csv

def read_col(CSV_FILE,CSV_COL):
    '''Read csv file and return a list like: [[username, password, count]]'''
    try:
        with open(CSV_FILE, 'rb') as f:
            records = []
            reader = csv.reader(f)
            for row in reader:
                records.append(row[CSV_COL].decode("utf-8"))
            return records
    except IOError:
        popup("Error", "File not found!")

def run_tkinter(inputs, method, comment):

    def get_radio():
        """
        function to read the radiobutton selection
        and put the result in a label
        """
        print g1.cget('state')
        print g2.cget('state')
        print g3.cget('state')
        print g4.cget('state')
        print g5.cget('state')
        print g6.cget('state')
        print 
        '''
        # get line index tuple
        sel = listbox1.curselection()
        # get the text
        seltext = listbox1.get(int(sel[0]))
        label3.config(text=seltext)'''

    def get_list(event):
        """
        function to read the listbox selection
        and put the result in a label
        """
        # get line index tuple
        sel = listbox1.curselection()
        # get the text
        seltext = listbox1.get(int(sel[0]))
        label1.config(text=seltext)

        #seltext2 = listbox1.get(int(sel[1]))
        '''print sel
        print seltext
        print sel[0]'''
        choicess = read_col(CSV_FILE = "spis_bud.csv", CSV_COL = 1)
        with open("spis_bud.csv") as f:
            reader = csv.reader(f)
            next(reader) # skip header
            data = []
            for row in reader:
                data.append(row)

        choicesss = read_col(CSV_FILE = choicess[sel[0]], CSV_COL = 0)
        choicesss = [chem.rstrip() for chem in choicesss]
        #next(choicesss) # skip header
        # Usuwanie poprzednich wartości
        listbox2.delete(0,END)
        #print choicess
        for item in choicesss:
            listbox2.insert(END, item)
        return sel


    def get_list2(event):
        # get line index tuple
        sel2 = listbox2.curselection()
        sel = listbox1.curselection()
        # get the text
        seltext2 = listbox2.get(int(sel2[0]))
        label2.config(text=seltext2)

        #seltext2 = listbox1.get(int(sel[1]))
        print sel2
        print seltext2
        print sel2[0]
        print listbox2.get(0)
        sel=int(listbox2.get(0)[1]+listbox2.get(0)[2])-1
        #sel= int(listbox2.get(0)[:2])-1
        print sel
        choicess = read_col(CSV_FILE = "spis_bud.csv", CSV_COL = 1)
        print choicess
        print choicess[sel]
        choicesss2 = read_col(CSV_FILE = choicess[sel], CSV_COL = 1)
        print choicesss2[sel2[0]]
        
        #choicesss2 = [chem.rstrip() for chem in choicesss2]
        # Usuwanie poprzednich wartości
        '''
        listbox2.delete(0,END)
        print choicess2
        for item in choicesss2:
            listbox2.insert(END, item)
        '''

        g1.config(state=DISABLED)
        g2.config(state=DISABLED)
        g3.config(state=DISABLED)
        g4.config(state=DISABLED)
        g5.config(state=DISABLED)
        g6.config(state=DISABLED)

        stg1="disabled"
        stg2="disabled"
        stg3="disabled"
        stg4="disabled"
        stg5="disabled"
        stg6="disabled"


        for item in str(choicesss2[sel2[0]])[::-1]:
            print item
            if item =="1": 
                stg1="active"
                g1.select()

               
            if item =="2": 
                stg2="active"
                g2.select()
            if item =="3": 
                stg3="active"
                g3.select()
            if item =="4": 
                stg4="active"
                g4.select()

            if item =="5": 
                stg5="active"
                g5.select()
            if item =="6": 
                stg6="active"
                g6.select()

         
    
        g1.config(state=stg1)
        g2.config(state=stg2)
        g3.config(state=stg3)
        g4.config(state=stg4)
        g5.config(state=stg5)
        g6.config(state=stg6)

        print gift.get()
        kat.delete(0, END)
        kat.insert(0, gift.get())

        #setkat get_radio()


         


       
   

    # Czytanie z pliku CSV
    choices = read_col(CSV_FILE = "spis_bud.csv", CSV_COL = 0)

    # read the data file into a list
    fin = open("spis.txt", "r")
    chem_list = fin.readlines()
    fin.close()


    # strip the trailing newline char
    chem_list = [chem.rstrip() for chem in choices]
    print chem_list
    # tworzenie okna
    root = tk.Tk()
    # create the listbox (note that size is in characters)
    listbox1 = Listbox(root, width=65, height=6)
    listbox1.grid(row=5, column=0, sticky=W)

    # create the listbox (note that size is in characters)
    listbox2 = Listbox(root, width=67, height=6)
    listbox2.grid(row=5, column=2, sticky=W)

    # create a vertical scrollbar to the right of the listbox
    yscroll = tk.Scrollbar(command=listbox1.yview, orient=VERTICAL)
    yscroll.grid(row=5, column=1, sticky=W+N+S)
    listbox1.configure(yscrollcommand=yscroll.set)

    # create a vertical scrollbar to the right of the listbox
    yscroll2 = Scrollbar(command=listbox2.yview, orient=VERTICAL)
    yscroll2.grid(row=5, column=3, sticky=W+N+S)
    listbox2.configure(yscrollcommand=yscroll2.set)

    # label to display selection
    label1 = Label(root, text='Click on an item in the list')
    label1.grid(row=12, column=0)
    label2 = Label(root, text='Click on an item in the list')
    label2.grid(row=12, column=2)
    # load the listbox with data
    for item in chem_list:
        listbox1.insert(END, item)

    # umieszczenie w oknie komentarza
    tk.Label(root, text=comment).grid(row=0, column=0, columnspan=2)
 
    # lista do zapamietania pol Entry 
    # aby potem mozna bylo pobrac z nich dane
    entries = []
 
    # dodanie w oknie pól do wprowadzania danych
    for i, text in enumerate(inputs, 1):
        tk.Label(root, text=text).grid(row=i, column=0, sticky='W')
        e = tk.Entry(root)
        e.grid(row=i, column=0, sticky='E')
        entries.append(e)
        print e
        print entries


    

    # dodanie okna z listą
  
    cnames = tk.StringVar(value=chem_list)
    #lbox = tk.Listbox(root, listvariable=chem_list, height=5)
    #wywołuje funkcje callback
    #lbox.bind('<<ListboxSelect>>', lambda:callback(root, method, entries, r))
    #lbox.grid(column=0, row=18, rowspan=8, sticky=("NSEW"))
    
    # dodanie przycisku rozpoczynajacego obliczenia - wywołuje funkcje callback
    b = tk.Button(root, text='Calc', command=lambda:callback(root, method, entries, r))
    b.grid(row=1, column=1)
    
    # Create and grid the outer content frame
    c = ttk.Frame(root, padding=(5, 5, 12, 0))
    c.grid(column=2, row=3, sticky=(N,W,S))
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0,weight=1)

    c.grid_columnconfigure(0, weight=1)
    c.grid_rowconfigure(5, weight=1)


    # dodanie zmiennej
    gift = IntVar()
    gift.set(0)

    # dodanie kategorii
    g1 = Radiobutton(c, text='1', variable=gift, value=1)
    g2 = Radiobutton(c, text='2', variable=gift, value=2)
    g3 = Radiobutton(c, text='3', variable=gift, value=3)
    g4 = Radiobutton(c, text='4', variable=gift, value=4)
    g5 = Radiobutton(c, text='5', variable=gift, value=5)
    g6 = Radiobutton(c, text='6', variable=gift, value=6)

    g1.grid(column=1, row=2, sticky=W, padx=5)
    g2.grid(column=2, row=2, sticky=W, padx=5)
    g3.grid(column=3, row=2, sticky=W, padx=5)
    g4.grid(column=4, row=2, sticky=W, padx=5)
    g5.grid(column=5, row=2, sticky=W, padx=5)
    g6.grid(column=6, row=2, sticky=W, padx=5)

    g1.config(state=DISABLED)
    g2.config(state=DISABLED)
    g3.config(state=DISABLED)
    g4.config(state=DISABLED)
    g5.config(state=DISABLED)
    g6.config(state=DISABLED) 
    
    # Pole wyniku kategorii
    kat = tk.Entry(c)
    kat.grid(row=2, column=7, sticky='E')

    
    # dodanie miejsca na wypisanie wyniku
    r = tk.Label(root)
    r.grid(columnspan=2)
    # left mouse click on a list item to display selection
    listbox1.bind('<ButtonRelease-1>', get_list)
     # left mouse click on a list item to display selection
    listbox2.bind('<ButtonRelease-1>', get_list2)
    # uruchomienie programu
    root.mainloop()
 
# funkcja wywolywana po wcisnieciu przycisku "Calc"
 
def callback(root, method, entries, r):
 
    # lista na dane pobrane z okna
    values = []
 
    # pobieranie danych z pol i zamiana tekstu na liczby
    for e in entries:
        values.append( int(e.get()) )
 
    # wywolanie funkcji liczacej i wstawienie wyniku w oknie
    r['text'] = method(*values)
 
    #root.destroy()
 
# --------------------------------------------
 
run_tkinter(__inputs__, wynarch, __comment__)