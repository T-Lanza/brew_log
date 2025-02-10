import tkinter as tk
from recipe import Recipe
from tkinter import ttk
from add_recipe import add_recipe
from get_date import get_date
import json
import os


# Import Saved Recipes
PATH = "DATA/recipes.json"

if os.path.exists(PATH) and os.path.getsize(PATH) > 0:
    with open(PATH, 'r') as file:
        recipes = [Recipe(**recipe) for recipe in json.load(file)]
else:
    recipes = []


# Build basic GUI
root = tk.Tk()
root.geometry("750x500")
root.resizable(False, False)
root.title(f"Oliver Noodle Recipe Book | {get_date()}")

# Add Recipe Button
add_recipe_button = tk.Button(root)
add_recipe_button.config(text="Add Recipe +", font=("Helvetica", 12))
add_recipe_button.config(command=lambda: add_recipe(display, add_recipe_button, root))
add_recipe_button.place(x=25, y=5)

# Create Display Frame
display = tk.Frame(root, width=700, height=420, bg="white")
display.pack_propagate(False)
display.place(x=25, y=55)

# Clear the Display Frame
for widget in display.winfo_children():
    widget.destroy()

# Addition of Recipes
counter = 1
for recipe in recipes:
    recipe_frame = tk.Frame(display)
    recipe_frame.config(width=700, height="40", bd=2, relief="solid")
    recipe_frame.pack_propagate(False)

    recipe_name = tk.Label(recipe_frame)
    recipe_name.config(text=recipe.name, width=40, pady=11, font=("Helvetica", 12))
    if counter % 2 != 0:
        recipe_name.config(bg="white")
    else:
        recipe_name.config(bg="#E6EDFF")

    go_to_button = tk.Button(recipe_frame)
    go_to_button.config(text=" >> ", height=40, bg="gray")

    recipe_abv = tk.Label(recipe_frame)
    recipe_abv.config(text=f"{recipe.abv}% ABV", width=10, pady=11, font=("Helvetica", 12))
    if counter % 2 != 0:
        recipe_abv.config(bg="#E6EDFF")
    else:
        recipe_abv.config(bg="white")

    recipe_style = tk.Label(recipe_frame)
    recipe_style.config(text=recipe.style, width=12, pady=11, font=("Helvetica", 12))
    if counter % 2 != 0:
        recipe_style.config(bg="white")
    else:
        recipe_style.config(bg="#E6EDFF")

    recipe_rate = tk.Label(recipe_frame)
    recipe_rate.config(text=f" {recipe.rate}/5 ", width=8, pady=11, font=("Helvetica", 12))
    if counter % 2 != 0:
        recipe_rate.config(bg="#E6EDFF")
    else:
        recipe_rate.config(bg="white")

    recipe_frame.pack(side="top")
    recipe_name.pack(side="left", anchor="w")
    go_to_button.pack(side="right")
    recipe_abv.pack(side="left", anchor="w")
    recipe_style.pack(side="left", anchor="w")
    recipe_rate.pack(side="left", anchor="w")

    counter += 1

# Main Loop

root.mainloop()