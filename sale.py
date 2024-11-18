
class Sifarish:
    # elave olunanlarin listi
    def __init__(self):
        self.items = [ ]
    
    # listi dict elemetlerine cevirirk for ile key ve valueni almagcun
    def add_item(self,product,price):
        self.items.append({
            "product":product,
            "price":price
        })
        # print(self.products)
    
    # umumi meblegi qaytaran method
    def get_total(self):
        total = sum([a["price"] for a in self.items])
        return total 

    # musterinin verdiyi sifarisler
    def show_sifarish(self):

        print("SIFARISLER".center(100,"-"))

        for sifaris in self.items:

            print(f'{sifaris["product"]}:{sifaris["price"]} AZN')

        print(f"UMUMI MEBLEG: {self.get_total()} AZN")




 