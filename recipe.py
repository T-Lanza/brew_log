import tkinter as tk
from get_date import get_date

class Recipe:
    def __init__(self, name, style, option, og, yeast):
        self.name = name
        measures = ["oz", "lb", "g", "gal", "pkt"]
        self.brew_styles = {
            "wines": ["Grape Wine", "Fruit Wine"],
            "meads": ["Dry Mead", "Sack Mead", "Metheglin", "Melomel", "Cyser"],
            "liquors": ["Whiskey", "Rum", "Brandy", "Mezcal", "Grappa"],
            "beers": ["Beer", "Cider", "Perry", "Hydromel"]
        }
        self.style = self.brew_styles[style][option]
        self.og = og
        self.fg = None
        self.yeast = yeast
        self.ingredients = []
        self.notes = []
    
    def abv_calc(self):
        if self.fg != None:
            return (self.og - self.fg) * 131.25
        else:
            return ""
        
    def add_ingredients(self, quantity, unit, item):
        ingredient = f"{quantity}{unit} {item}"
        self.ingredients.append(ingredient)

    def add_notes(self, note_entry):
        date = get_date()
        note = note_entry.get("1.0", tk.END)
        addition = {
            "date": date,
            "note": note
        }
        self.notes.append(addition)