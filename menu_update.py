
# MENU DAXILINDEKI MEHSULLARA BURDAN ELAVE EDIR VE YA DEYIWIRIK.SONDA JSONA GEDECEK
db = {
    "desertler":{
        "balli tort":6,
        "gilemeyveli crep":8,
        "dietik desert":12
    },

    "ickiler":{
        "latte":6.5,
        "mohito":7.3,
        "milkshake":9,
        "cay":2,
        "qazli su":3
    },
    
    "sandwich":{
        "chickensandwich":7,
        "barbukysandwich":6,
        "sezarroll":10,
        "vegeteriansandwich":13
    }
}

# HER DEFE MENUDA DUZELIS ELESEK MENU.JSON FAYLINA ELAVE OLUNACAG
with open("menu.json","w") as file:
    json.dump(db, file, ensure_ascii=False, indent=2)