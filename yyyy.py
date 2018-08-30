#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A Python Exercise: Reading CSV File & Tkinter Implementation
Including the subjects: Grid Layout, Tk Variables and Binding
'''
from Tkinter import *
import Tkinter as tk
from ttk import *
import csv

# display names in system codepage
def decolist(f_list):
    # type: (object) -> object
    return f_list.decode(sys.getfilesystemencoding())
'''
def read_from_file(CSV_FILE):
    #Read csv file and return a list like: [[username, password, count]]
    try:
        with open(CSV_FILE, 'rb') as f:
            users = []
            reader = csv.reader(f)
            for row in reader:
                #row[2] = int(row[2]) # Make the count an integer so it can increase later
                users.append(row[0])
            return users
    except IOError:
        popup("Error", "File not found!")
'''
def read_col(CSV_FILE,CSV_COL):
    '''Read csv file and return a list like: [[username, password, count]]'''
    try:
        with open(CSV_FILE, 'rb') as f:
            records = []
            reader = csv.reader(f)
            for row in reader:
                records.append(row[CSV_COL])
            return records
    except IOError:
        popup("Error", "File not found!")


choices_bud = ['l','o','p']

class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack(anchor="w")

        # Labels

        tk.Label(self, text="Typ budynku:").grid(row = 3, column = 0)
        tk.Label(self, text="Wybierz uszczegółowienie:").grid(row = 6, column = 0)

        # Create a Tkinter variable
        tkvar1 = StringVar(root)
        tkvar2 = StringVar(root)

        # Dictionary with options
        choices = read_col(CSV_FILE = "spis_bud.csv", CSV_COL = 1)
        choices2 = read_col(CSV_FILE = "spis_bud.csv", CSV_COL = 0)
        #print choices

        choices_bud = read_col(CSV_FILE = "1_mieszkalne.csv", CSV_COL = 0)
        #print choices_bud


        # MenuButton
        popupMenu = OptionMenu(self, tkvar1, *choices)#.grid(row=5,column=1)
        popupMenu.grid(row = 5, column =1)
        #popupMenu.pack(padx=5, side=LEFT)

        # MenuButton
        popupMenu2 = OptionMenu(self, tkvar2, *choices_bud)#.grid(row=7,column=1)
        popupMenu2.grid(row = 7, column =1)
        popupMenu2.pack(fill=X)
        #menu2 = popupMenu2.children['menu']
        # Binding
        '''
        def refresh():
        # Reset var and delete all old options
            tkvar2.set('')
            popupMenu2['menu'].delete(0, 'end')

            # Insert list of new options (tk._setit hooks them up to var)
            new_choices =  read_col(CSV_FILE = read_col("spis_bud.csv",1), CSV_COL = 0)
            for choice in new_choices:
                popupMenu2['menu'].add_command(label=choice, command=tk._setit(tkvar2, choice))

'''
        # on change dropdown value
        def change_dropdown(self, *args):
            print( tkvar2.get() )
            print( tkvar1.get() )
            #refresh
            name_files = tkvar1.get()
            print name_files
            #self.master.bind("<Return>", self.login)
            #print choices_bud
            
            tkvar2.set('')
            popupMenu2['menu'].delete(0, 'end')

            # Insert list of new options (tk._setit hooks them up to var)
            new_choices =  read_col(CSV_FILE = name_files, CSV_COL = 0)
            for choice in new_choices:
                popupMenu2['menu'].add_command(label=choice, command=tk._setit(tkvar2, choice))



        #def change_drop(self, *args):
         #   print( self.tkvar2.get() )
       
        #tk.Button(self, text='Refresh', command=refresh).grid()

        # link function to change dropdown
        tkvar1.trace('w', change_dropdown)

        # link function to change dropdown
        #tkvar2.trace('w', change_drop)
        #self.master.bind("<Return>", self.login)
        self.pack(anchor="w")


# GUI settings
root = tk.Tk()
app = App(root)
root.title("Login Form")
root.minsize(800, 200)

# Initalize GUI
root.mainloop()