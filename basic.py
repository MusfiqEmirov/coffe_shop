from menu import Menu
from sale import Sifarish
from payment import Odenis
from check_out import Kassa,Table




class Cafe:

    # diger fayllardan classlari alir
    def __init__(self):
        self.menu = Menu()
        self.kassa = Kassa()
        self.table = Table(self.kassa)


    def take_order(self):
        sifaris = Sifarish()
        self.menu.show_menu()

        while True:

            #musteriden alinan sifarisler
            item_name = input("Mehsulun adini seicin.eger sifarisiniz bitdise SON YAZIN>>>>")

            if item_name.lower() == "son":
                break

            for category, items in self.menu.items.items():
    
                if item_name in items:
                    sifaris.add_item(item_name, items[item_name])
                    print(f"{item_name} sifariniz elave olundu:Qiymet:+{items[item_name]}")
                    break
            else:
                print("axtardiginiz mehsul menuda yoxdu".center(100,"!"))
        
        # son yazdiqdan sonra musteri sifarislerini gosterir
        sifaris.show_sifarish()
        return sifaris

    def process_payment(self, sifaris):

        payment_type = input("odenisin novu:KART ve ya NAGD olaraq birini secin>>")
        amount = 0

        if payment_type.lower() == "nagd":
            amount = float(input("ODENIS EDIN:"))
            
        odenis = Odenis(sifaris)
        odenis.process_payment(payment_type, amount)
        # bu hissede cox error oldu gpt komey eledi((

        item_name = sifaris.items[0]['product']
        self.kassa.add_sales(payment_type, sifaris.get_total(), item_name=item_name)

    # bagla yazdiqda hesabat apari ve gerimqaytarir
    def close_day(self):
        self.kassa.show_daily_sales()

    # tehvil yazdiqda iwleyen method
    def protable(self):
        self.table.display_table()



