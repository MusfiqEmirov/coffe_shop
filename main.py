import time
from basic import Cafe
from check_out import Kassa


# butun classlarin ve faylarin islediyini function
def main():

    cafe = Cafe()
    cost = Kassa()
    

    while True:
        print(f"Businesscupa xos gelmisiniz\n".upper().center(100," "))

        print("sifaris vermek ve menyunu elde elemek.(basla) - yazin".center(100," "))  
        print("gun sonu kassani baglamagcun.(bagla) - yazin".center(100," "))  
        print("smen tehvili ucun (tehvil) - yazin".center(100," ")) 

        # emelyat secimi ucun
        select = input("secim ele>>")

 

        if select == "basla":
            
            # sifarisleri qebul edir
            sifaris = cafe.take_order()
            cafe.process_payment(sifaris)
        
        # hesabat aparir
        elif select == "bagla":

            add_cost = float(input("Rəsxodu yaz: "))
            cost.add_expenses(add_cost)

            cafe.close_day()
        
        # kassa baglanir ve tehvil verilir gun bitir proqram dayanir
        elif select == "tehvil":

            # 3 saniye sonra 
            print("sistem baglanir.....")

            time.sleep(2)
            print("Gun sonu tamamlandi".center(100,"*"))

            # cedveli qaytarir
            cafe.protable()
            break

        else:
            print("yalnis secim!!!")



if __name__ == "__main__":
    main()