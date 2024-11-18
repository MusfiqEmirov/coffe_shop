class A:
    def __init__(self):
        self.b = 0

    def add(self,b):
        self.b += b
        print(f"add methodd {self.b}")

    def update(self):
        print(f"update methodd {self.b}")
c = A() 
c.add(2)
c.update()

# bu fayl class daxilinda self parametrini butun methodlara oture bilmeyle bagli test ucundur
# cunki chec_out.py>>class Kassa>>add_expenses() method icindeki self.daily_expenses global deyiwken etmeden diger methodlara oturmey mumkun olmadi