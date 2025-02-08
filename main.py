import tkinter as tk
from recipe import Recipe
from menu import main_menu
import json


PATH = "DATA/recipes.json"

def close_book_toggle(root, test_button, background):
    for widget in root.winfo_children():
        if widget != background:
            widget.destroy()

    # Insert Open Book
    open_book_frame = tk.Frame(root, width=1030, height=700, bg="#854218")
    open_book_frame.place(x=450, y=30)
    open_book_canvas = tk.Canvas(open_book_frame, width=1030, height=700, bg="#854218")
    open_book_canvas.pack(side="left")
    open_book_image = tk.PhotoImage(file="Images/open.png")
    open_book_canvas.create_image(0, 0, image=open_book_image, anchor="nw")

    # Store the image in root to prevent garbage collection
    root.open_book_image = tk.PhotoImage(file="Images/open.png")
    open_book_canvas.create_image(0, 0, image=root.open_book_image, anchor="nw")

    test_button.config(command=lambda: open_book_toggle(root, test_button, background))

    main_menu(open_book_frame, recipes)

def open_book_toggle(root, test_button, background):
    for widget in root.winfo_children():
        if widget != background:
            widget.destroy()

    # Insert Closed Book
    open_book_frame = tk.Frame(root, width=1030, height=700, bg="#854218")
    open_book_frame.place(x=450, y=30)
    closed_book_canvas = tk.Canvas(open_book_frame, width=469, height=700, bg="#854218")
    closed_book_canvas.place(x=561, y=0)
    close_book_image = tk.PhotoImage(file="Images/closed.png")
    closed_book_canvas.create_image(0, 0, image=close_book_image, anchor="nw")

    # Store the image in root to prevent garbage collection
    root.close_book_image = tk.PhotoImage(file="Images/closed.png")
    closed_book_canvas.create_image(0, 0, image=root.close_book_image, anchor="nw")

    test_button.config(command=lambda: close_book_toggle(root, test_button, background))

with open(PATH, 'r') as file:
    content = file.read().strip()
    if not content:
        recipes = []
    else:
        recipes = json.load(file)

# Build GUI
root = tk.Tk()
root.title("Oliver Noodle Vintner Catalogue")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")

# Make Background
background = tk.Canvas(root, width=1600, height=900)
background.pack()
desktop = tk.PhotoImage(file="Images/wood.png")
background.create_image(0,0, image=desktop, anchor="nw")


# Insert Closed Book
open_book_frame = tk.Frame(root, width=1030, height=700, bg="#854218")
open_book_frame.place(x=450, y=30)
closed_book_canvas = tk.Canvas(open_book_frame, width=469, height=700, bg="#854218")
closed_book_canvas.place(x=561, y=0)
close_book_image = tk.PhotoImage(file="Images/closed.png")
closed_book_canvas.create_image(0, 0, image=close_book_image, anchor="nw")

# Test Button
test_button = tk.Button(background)
test_button.config(text="Test", command=lambda: close_book_toggle(root, test_button, background))
test_button.place(x=100, y=100)

# Main GUI Loop
root.mainloop()