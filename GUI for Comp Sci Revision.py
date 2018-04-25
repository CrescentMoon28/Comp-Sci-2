
import tkinter as tk

def add_cards(): # window for adding cards
    print("Working")
    start.quit()
    addwin = tk.Tk()

def import_cards():
    print("Banana")

def select_cards(): # window for selecting card pack
    print("Works")

    packwin = tk.Tk()

start = tk.Tk()

start.title("Computer Science Revision Flashcards")

addcard = tk.Button(start, text = "Add revision cards", command = add_cards)
addpack = tk.Button(start, text = "Add card pack", command = import_cards)
revise = tk.Button(start, text = "Start revising!", command = select_cards)

addcard.pack(side = tk.TOP)
addpack.pack(side = tk.TOP)
revise.pack(side = tk.TOP)

