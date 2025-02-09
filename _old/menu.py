import tkinter as tk

def main_menu(frame, recipes):
    contents_title = tk.Label(frame, text="Table of Contents")
    contents_title.config(font=("Z003 Medium Italic", 24), bg="#EBDBCD")
    contents_title.place(x=115, y=53)

    contents_text = tk.Text(frame)
    contents_text.config(width=47, height=28, bg="#EBDBCD")
    contents_text.place(x=62, y=110)