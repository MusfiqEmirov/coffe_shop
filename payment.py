# musterilerin odenisi ucun object
class Odenis:
    def __init__(self,sifaris):
        self.sifaris = sifaris
        self.total = sifaris.get_total()
    
    # odenis nove gore musteriden pul almaq
    def process_payment(self, payment_type, amount=None):

        if payment_type == "kart":
            print(f"{self.total} manat Hesabinizdan cixildi")

        elif payment_type == "nagd":

            # eger odenis hesabdan az olarsa
            if amount < self.total:
                print("Odenis ucun yeterli vesait deyil!!")

            elif amount == self.total:
                print(f"{self.total} AZN odenildi")

            else:
                
                # eger pulu hesabdan artiq vererse
                print(f"pulunuzun geri qaligi-->>{amount-self.total}") 

        else:
            print("bele bir odenis methodu yoxdur")
