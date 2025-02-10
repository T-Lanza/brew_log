import tkinter as tk
from get_date import get_date

class Recipe:
    measures = ["oz", "lb", "g", "gal", "pkt"]
    brew_styles = {
        "wines": ["Grape Wine", "Fruit Wine"],
        "meads": ["Dry Mead", "Sack Mead", "Metheglin", "Melomel", "Cyser"],
        "liquors": ["Whiskey", "Rum", "Brandy", "Mezcal", "Grappa"],
        "beers": ["Beer", "Cider", "Perry", "Hydromel"]
    }
    ingredients = []
    notes = []

    def __init__(self, name, style, og, yeast, start_date, rate=None, fg=None, **kwargs):
        self.name = name
        self.style = style
        self.og = og
        self.fg = fg
        self.yeast = yeast
        self.abv = self.abv_calc()
        self.rate = rate
        self.start_date = start_date
    
    def abv_calc(self):
        if self.fg != None:
            return (self.og - self.fg) * 131.25
        else:
            return 0
        
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