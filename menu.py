import json

# MENU.JSON FAYLINNAN  YENILENMIW MELUMATI ALIB DICT EDIRIK
with open("menu.json") as file:
    menu_db = json.load(file)

# umumi menyunu saxlayan object
class Menu:

    def __init__(self):
        self.items = menu_db
        

    def show_menu(self):

        print(" 🍕 MENU ☕️ ".center(100, "-"))
        
        # CATEGORYLAR UZRE SADALAYIRIQ
        for category,items in self.items.items():
            print(f"{category.capitalize()}")
            
            # MEHSULLAR VE QIYMETLERE GORE SADALAYIRIQ
            for item,price in items.items():
                print(f"{item} --- {price} azn")
  