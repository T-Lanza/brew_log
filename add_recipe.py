import tkinter as tk
from tkinter import ttk
from get_date import *
from recipe import Recipe
import json
import os


# Import Saved Recipes
PATH = "DATA/recipes.json"

if os.path.exists(PATH) and os.path.getsize(PATH) > 0:
    with open(PATH, 'r') as file:
        recipes = [Recipe(**recipe) for recipe in json.load(file)]
else:
    recipes = []

def back_home(display, back_button, root):
    # Clear 'Back' Button
    back_button.destroy()

    # Clear the Display Frame
    for widget in display.winfo_children():
        widget.destroy()

    # Add Recipe Button
    add_recipe_button = tk.Button(root)
    add_recipe_button.config(text="Add Recipe +", font=("Helvetica", 12))
    add_recipe_button.config(command=lambda: add_recipe(display, add_recipe_button, root))
    add_recipe_button.place(x=25, y=5)

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


def add_recipe(display, button, root):

    def add_new(entry_date_input,
                entry_name_input,
                style_dropdown,
                entry_yeast_input,
                og_input_entry,
                notes_entry_input,
                recipes):
        date = entry_date_input.get()
        name = entry_name_input.get()
        style = style_dropdown.get()
        yeast = entry_yeast_input.get()
        og = og_input_entry.get()
        notes = notes_entry_input.get("1.0", tk.END)
        today = get_date_num()
        new_note = {
            "date": today,
            "note": notes
        }
        new_recipe = Recipe(name, style, og, yeast, date)
        
        new_recipe.notes.append(new_note)
        recipes.append(new_recipe)

        with open(PATH, 'w') as file:
            json.dump([recipe.__dict__ for recipe in recipes], file, indent=4)

        
    # Delete Add Button
    button.destroy()

    # Clear the Display Frame
    for widget in display.winfo_children():
        widget.destroy()

    # Add the 'Back' Button
    back_button = tk.Button(root)
    back_button.config(text="   << Back   ", font=("Helvetica", 12))
    back_button.config(command=lambda: back_home(display, back_button, root))
    back_button.place(x=25, y=5)

    # Create Addition Screen
    new_recipe_title = tk.Label(display)
    new_recipe_title.config(bg="white", text="New Recipe Entry")
    new_recipe_title.config(font=("Helvetica", 24))
    new_recipe_title.place(x=10, y=10)

    entry_frame = tk.Frame(display)
    entry_frame.config(bg="#E6EDFF", width=300, height=365, bd=1, relief="sunken")
    entry_frame.pack_propagate(False)
    entry_frame.place(x=10, y=45)

    entry_date_label = tk.Label(entry_frame, text="Start Date:      ")
    entry_date_label.config(width=12, font=("Helvetica", 16), bg="#E6EDFF")
    entry_date_label.place(x=0, y=2)

    entry_date_input = tk.Entry(entry_frame)
    default_date = get_date_num()
    entry_date_input.insert(0, default_date)
    entry_date_input.config(width=12, font=("Helvetica", 14), bg="white", bd=2, relief="sunken")
    entry_date_input.place(x=165, y=2)

    entry_name_label = tk.Label(entry_frame, text=" Name:")
    entry_name_label.config(width=12, font=("Helvetica", 16), bg="#E6EDFF")
    entry_name_label.place(x=0, y=32)

    entry_name_input = tk.Entry(entry_frame)
    entry_name_input.config(width=12, font=("Helvetica", 14), bg="white", bd=2, relief="sunken")
    entry_name_input.place(x=165, y=32)

    entry_style_label = tk.Label(entry_frame, text="   Style:")
    entry_style_label.config(width=12, font=("Helvetica", 16), bg="#E6EDFF")
    entry_style_label.place(x=0, y=62)

    style_options = [style for category in Recipe.brew_styles.values() for style in category]
    style_dropdown = ttk.Combobox(entry_frame, values=style_options)
    style_dropdown.config(width=11, font=("Helvetica", 13))
    style_dropdown.place(x=165, y=64)

    entry_yeast_label = tk.Label(entry_frame, text="  Yeast:")
    entry_yeast_label.config(width=12, font=("Helvetica", 16), bg="#E6EDFF")
    entry_yeast_label.place(x=0, y=92)

    entry_yeast_input = tk.Entry(entry_frame)
    entry_yeast_input.config(width=12, font=("Helvetica", 14), bg="white", bd=2, relief="sunken")
    entry_yeast_input.place(x=165, y=92)

    entry_og_label = tk.Label(entry_frame, text="    OG:")
    entry_og_label.config(width=12, font=("Helvetica", 16), bg="#E6EDFF")
    entry_og_label.place(x=0, y=122)

    entry_og_input = tk.Entry(entry_frame)
    entry_og_input.config(width=12, font=("Helvetica", 14), bg="white", bd=2, relief="sunken")
    entry_og_input.place(x=165, y=122)

    entry_notes_label = tk.Label(entry_frame, text="Notes:")
    entry_notes_label.config(font=("Helvetica", 18), bg="#E6EDFF")
    entry_notes_label.place(x=5, y=162)

    entry_notes_input = tk.Text(entry_frame)
    entry_notes_input.config(bd=2, relief="sunken", bg="white", width=34, height=9, wrap="word")
    entry_notes_input.place(x=7, y=192)

    test_button = tk.Button(display)
    test_button.place(x=615, y=380)
    test_button.config(text="Submit!", command=lambda: add_new(entry_date_input,
                                                  entry_name_input,
                                                  style_dropdown,
                                                  entry_yeast_input,
                                                  entry_og_input,
                                                  entry_notes_input,
                                                  recipes))
    
    for recipe in recipes:
        if recipe["name"] == "Test 2":
            for note in recipe["notes"]:
                print(recipe["date"])
                print(recipe["notes"])

    # Test

    #options = [style for category in Recipe.brew_styles.values() for style in category]
    #dropdown = ttk.Combobox(entry_frame, values=options)
    #dropdown.place(x=15, y=15)

    #bg="#E6EDFF"