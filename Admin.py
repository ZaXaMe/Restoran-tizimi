# Fayldan xodimlar ro'yxatini o'qish funksiyasi
def xodimlar_royxatini_korsat(fayl_nomi):
    try:
        with open(fayl_nomi, 'r', encoding='utf-8') as fayl:
            malumotlar = fayl.readlines()
            return malumotlar
    except FileNotFoundError:
        print(f"{fayl_nomi} fayli topilmadi.")
        return []

# Yangi lavozim va maoshni qo'shish funksiyasi
def lavozim_va_maosh_qoshish(fayl_nomi, malumotlar):
    if not malumotlar:
        print("Xodimlar ro'yxati mavjud emas.")
        return
    
    print("\nXodimlar ro'yxati:")
    for i, xodim in enumerate(malumotlar, 1):
        print(f"{i}. {xodim.strip()}")
    
    try:
        xodim_index = int(input("\nQaysi xodimga yangi lavozim va maosh qo'shishni xohlaysiz? (raqamini kiriting): ")) - 1
        if xodim_index < 0 or xodim_index >= len(malumotlar):
            print("Noto'g'ri raqam kiritildi.")
            return
        
        # Lavozimlar ro'yxati
        lavozimlar = ["Offitsiant", "Oshpaz", "Hisobchi", "Qorovul", "Idish yuvuvchi", "Farrosh"]
        
        # Lavozimlarni tanlash
        print("\nMavjud lavozimlar:")
        for i, lavozim in enumerate(lavozimlar, 1):
            print(f"{i}. {lavozim}")
        
        lavozim_tanlov = int(input("\nLavozimni tanlang (raqamini kiriting): ")) - 1
        if lavozim_tanlov < 0 or lavozim_tanlov >= len(lavozimlar):
            print("Noto'g'ri lavozim tanlandi.")
            return
        
        # Yangi lavozimni olish
        yangi_lavozim = lavozimlar[lavozim_tanlov]
        
        # Yangi maoshni kiritish (int formatida)
        maosh = int(input("Yangi maoshni kiriting (butun raqam): "))
        
        # Yangi malumotni yangilash
        yangi_malumot = f"{malumotlar[xodim_index].strip().split(',')[0]}, Lavozim: {yangi_lavozim}, Maosh: {maosh}\n"
        malumotlar[xodim_index] = yangi_malumot
        
        # Faylni yangilash
        with open(fayl_nomi, 'w', encoding='utf-8') as fayl:
            fayl.writelines(malumotlar)
        
        print(f"Yangi lavozim: {yangi_lavozim} va maosh: {maosh} muvaffaqiyatli qo'shildi.")
    
    except ValueError:
        print("Noto'g'ri raqam kiritildi!")

# Asosiy menyu funksiyasi
def menyu():
    print("\n1. Xodimlar ro'yxatini ko'rish")
    print("2. Yangi lavozim va maosh qo'shish")
    print("3. Dasturni tugatish")
    tanlov = input("\nTanlang (1/2/3): ")
    return tanlov

# Asosiy dastur
if __name__ == "__main__":
    fayl_nomi = "Xodimlar_malumotlari.txt"
    
    while True:
        tanlov = menyu()
        
        if tanlov == '1':
            malumotlar = xodimlar_royxatini_korsat(fayl_nomi)
            if malumotlar:
                print("\nXodimlar ro'yxati:")
                for i, xodim in enumerate(malumotlar, 1):
                    print(f"{i}. {xodim.strip()}")
        
        elif tanlov == '2':
            malumotlar = xodimlar_royxatini_korsat(fayl_nomi)
            lavozim_va_maosh_qoshish(fayl_nomi, malumotlar)
        
        elif tanlov == '3':
            print("Dastur tugadi.")
            break
        
        else:
            print("Noto'g'ri tanlov. Iltimos, qayta tanlang.")
