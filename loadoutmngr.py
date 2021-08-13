#!/usr/bin/python3

import sqlite3 as sql
from tkinter import *
import sys

class ManageApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.frames["FrontPage"] = FrontPage(parent=container, controller=self)
        self.frames["FrontPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["HelpPage"] = HelpPage(parent=container, controller=self)
        self.frames["HelpPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["ViewArsenals"] = ViewArsenals(parent=container, controller=self)
        self.frames["ViewArsenals"].grid(row=0, column=0, sticky="nsew")
        self.frames["ViewArmory"] = ViewArmory(parent=container, controller=self)
        self.frames["ViewArmory"].grid(row=0, column=0, sticky="nsew")
        self.frames["AddArsenal"] = AddArsenal(parent=container, controller=self)
        self.frames["AddArsenal"].grid(row=0, column=0, sticky="nsew")
        self.frames["AddArmory"] = AddArmory(parent=container, controller=self)
        self.frames["AddArmory"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("FrontPage")
        
        

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        menu = frame.menubar(self)
        self.configure(menu=menu)


class FrontPage(Frame):

    def menubar(self, controller):
        menu = Menu(controller)
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Help", command=lambda:controller.show_frame("HelpPage"))
        fileMenu.add_command(label="Quit", command=self.terminate)
        menu.add_cascade(label="File", menu=fileMenu)

        viewMenu = Menu(menu)
        viewMenu.add_command(label="Arsenals", command=lambda:controller.show_frame("ViewArsenals"))
        viewMenu.add_command(label="Armory", command=lambda:controller.show_frame("ViewArmory"))
        menu.add_cascade(label="View", menu=viewMenu)

        addMenu = Menu(menu)
        addMenu.add_command(label="Arsenal", command=lambda:controller.show_frame("AddArsenal"))
        addMenu.add_command(label="Armory", command=lambda:controller.show_frame("AddArmory"))
        menu.add_cascade(label="Add", menu=addMenu)
        return menu

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        #self.title("Loadout Manager")

    def terminate(self):
        print("Terminating Program...")
        exit()

class HelpPage(Frame):
    def menubar(self, controller):
        menu = Menu(controller)
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Help", command=lambda:controller.show_frame("HelpPage"))
        fileMenu.add_command(label="Quit", command=self.terminate)
        menu.add_cascade(label="File", menu=fileMenu)

        viewMenu = Menu(menu)
        viewMenu.add_command(label="Arsenals", command=lambda:controller.show_frame("ViewArsenals"))
        viewMenu.add_command(label="Armory", command=lambda:controller.show_frame("ViewArmory"))
        menu.add_cascade(label="View", menu=viewMenu)

        addMenu = Menu(menu)
        addMenu.add_command(label="Arsenal", command=lambda:controller.show_frame("AddArsenal"))
        addMenu.add_command(label="Armory", command=lambda:controller.show_frame("AddArmory"))
        menu.add_cascade(label="Add", menu=addMenu)
        return menu

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        label = Label(self, text="Help Page")
        label.pack(side="top", fill="x", pady=10)

        homeButton = Button(self, text="Return Home", command=lambda:controller.show_frame("FrontPage"))
        homeButton.pack()
 
    def terminate(self):
        print("Terminating Program...")
        exit()

class ViewArsenals(Frame):
    def menubar(self, controller):
        menu = Menu(controller)
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Help", command=lambda:controller.show_frame("HelpPage"))
        fileMenu.add_command(label="Quit", command=self.terminate)
        menu.add_cascade(label="File", menu=fileMenu)

        viewMenu = Menu(menu)
        viewMenu.add_command(label="Arsenals", command=lambda:controller.show_frame("ViewArsenals"))
        viewMenu.add_command(label="Armory", command=lambda:controller.show_frame("ViewArmory"))
        menu.add_cascade(label="View", menu=viewMenu)

        addMenu = Menu(menu)
        addMenu.add_command(label="Arsenal", command=lambda:controller.show_frame("AddArsenal"))
        addMenu.add_command(label="Armory", command=lambda:controller.show_frame("AddArmory"))
        menu.add_cascade(label="Add", menu=addMenu)
        return menu

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        label = Label(self, text="All Arsenals")
        label.pack(side="top", fill="x", pady=10)

        homeButton = Button(self, text="Return Home", command=lambda:controller.show_frame("FrontPage"))
        homeButton.pack()
 
    def terminate(self):
        print("Terminating Program...")
        exit()

class ViewArmory(Frame):
    def menubar(self, controller):
        menu = Menu(controller)
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Help", command=lambda:controller.show_frame("HelpPage"))
        fileMenu.add_command(label="Quit", command=self.terminate)
        menu.add_cascade(label="File", menu=fileMenu)

        viewMenu = Menu(menu)
        viewMenu.add_command(label="Arsenals", command=lambda:controller.show_frame("ViewArsenals"))
        viewMenu.add_command(label="Armory", command=lambda:controller.show_frame("ViewArmory"))
        menu.add_cascade(label="View", menu=viewMenu)

        addMenu = Menu(menu)
        addMenu.add_command(label="Arsenal", command=lambda:controller.show_frame("AddArsenal"))
        addMenu.add_command(label="Armory", command=lambda:controller.show_frame("AddArmory"))
        menu.add_cascade(label="Add", menu=addMenu)
        return menu

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        label = Label(self, text="All Armory")
        label.pack(side="top", fill="x", pady=10)

        homeButton = Button(self, text="Return Home", command=lambda:controller.show_frame("FrontPage"))
        homeButton.pack()
 
    def terminate(self):
        print("Terminating Program...")
        exit()

class AddArsenal(Frame):
    def menubar(self, controller):
        menu = Menu(controller)
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Help", command=lambda:controller.show_frame("HelpPage"))
        fileMenu.add_command(label="Quit", command=self.terminate)
        menu.add_cascade(label="File", menu=fileMenu)

        viewMenu = Menu(menu)
        viewMenu.add_command(label="Arsenals", command=lambda:controller.show_frame("ViewArsenals"))
        viewMenu.add_command(label="Armory", command=lambda:controller.show_frame("ViewArmory"))
        menu.add_cascade(label="View", menu=viewMenu)

        addMenu = Menu(menu)
        addMenu.add_command(label="Arsenal", command=lambda:controller.show_frame("AddArsenal"))
        addMenu.add_command(label="Armory", command=lambda:controller.show_frame("AddArmory"))
        menu.add_cascade(label="Add", menu=addMenu)
        return menu

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        label = Label(self, text="Add Arsenal")
        label.pack(side="top", fill="x", pady=10)

        homeButton = Button(self, text="Return Home", command=lambda:controller.show_frame("FrontPage"))
        homeButton.pack()
 
    def terminate(self):
        print("Terminating Program...")
        exit()

class AddArmory(Frame):
    def menubar(self, controller):
        menu = Menu(controller)
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Help", command=lambda:controller.show_frame("HelpPage"))
        fileMenu.add_command(label="Quit", command=self.terminate)
        menu.add_cascade(label="File", menu=fileMenu)

        viewMenu = Menu(menu)
        viewMenu.add_command(label="Arsenals", command=lambda:controller.show_frame("ViewArsenals"))
        viewMenu.add_command(label="Armory", command=lambda:controller.show_frame("ViewArmory"))
        menu.add_cascade(label="View", menu=viewMenu)

        addMenu = Menu(menu)
        addMenu.add_command(label="Arsenal", command=lambda:controller.show_frame("AddArsenal"))
        addMenu.add_command(label="Armory", command=lambda:controller.show_frame("AddArmory"))
        menu.add_cascade(label="Add", menu=addMenu)
        return menu

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        label = Label(self, text="Add Armory")
        label.pack(side="top", fill="x", pady=10)

        homeButton = Button(self, text="Return Home", command=lambda:controller.show_frame("FrontPage"))
        homeButton.pack()
 
    def terminate(self):
        print("Terminating Program...")
        exit()

app = ManageApp()
app.geometry("400x300")
app.mainloop()
