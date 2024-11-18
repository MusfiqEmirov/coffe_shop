from sale import Sifarish
from payment import Odenis
from tabulate import tabulate
from datetime import date

# global self.daily_expenses elediyimmiz
daily_expenses = 0

class Kassa:
    
    # gun sonu hesbati
    def __init__(self):
        self.total_nagd = 0
        self.total_kart = 0
        self.total_sales = 0
        self.items_sold = { }

    
    # satislari ve satilan mehsullari elave eden method
    def add_sales(self, sale_type, amount, item_name):

        global daily_expenses
        
        if sale_type == "nagd":
            self.total_nagd += amount

        elif sale_type == "kart":
            self.total_kart += amount

        self.total_sales += amount

        if item_name in self.items_sold:
            self.items_sold[item_name] += 1
        
        else:
            self.items_sold[item_name] = 1

    
    # gundelik  xercleri elave eden method
    def add_expenses(self,cost):

        # self.daily_expenses global etmeden diger methodlar icine elave elemey mumkun olmadi
        global daily_expenses
        daily_expenses += cost

        # burda bir dewiy var {self.daily_expenses} - xerci geri qaytarir burda
        print(f"sizin rasxod:{daily_expenses}")

        
    # gun sonu emelyatlari
    def show_daily_sales(self):


        print(f"Umumi xercler:{daily_expenses}")

        print("Gun sonunun hesabati".center(100,"-"))

        if not self.items_sold:
                print("kankret alver yoxdu")

        else:
            for item, count in self.items_sold.items():
                print(f"satilan mehsul: {item}, satis sayi: {count}")

        # gun sonu nagd satisi gosterir
        print(f"nagd satislar:{self.total_nagd}")

        # gun sonu kartla satisi gosterir
        print(f"kartla satislar:{self.total_kart}")

        # gun sonu umumi satisi gosterir
        print(f"Umumi satis:{self.total_sales}")
        
        # gun sonu umumi xercleri gosterir
        print(f"Umumi xercler:{daily_expenses}")

        # gun sonu umumi menfeeti gosterir
        menfeet = self.total_sales - daily_expenses

        print(f"Umumi menfeet:{menfeet}")

# tehvil kamandasi olduqdan sonra butun melumatlar protetablede gorsenecek
class Table:
    # gunun tarixi
    today = date.today()
    
    def __init__(self,kassa):
        self.kassa = kassa 
        
        # cedvelin basligi
        self.headers = ["tarix", "Nagd satis", "kartla satis","Umumi satis","umumi mesref","xalis menfeeet"]
     
    # cedvel daxili melumatlar qebul edir
    def display_table(self):
        
        nagd = self.kassa.total_nagd
        kart = self.kassa.total_kart
        sales = self.kassa.total_sales
        expenses = daily_expenses
        today = self.today
        profit = sales - expenses
       
        
    # qebul etdiyi melumatlari cedvele elave edir
        rows = [
            [today, nagd, kart, sales, expenses, profit]
        ]

        print(f"\n")
        
        # cedveli yazdirmag
        print(tabulate(rows, headers=self.headers, tablefmt="grid").center(100," "))
        print("BIZI SECDIYINIZ UCUN TESEKKURLER".center(100,"-"))
        print(f"\n")


        
       

