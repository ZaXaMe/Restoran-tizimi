# Faylga yozish funksiyasi
def malumot_qoshish(fayl_nomi, ism, familiya, yosh, jinsi):
    with open(fayl_nomi, 'a', encoding='utf-8') as fayl:
        fayl.write(f"Ism: {ism}, Familiya: {familiya}, Yosh: {yosh}, Jins: {jinsi}\n")
    print(f"{ism} {familiya} muvaffaqiyatli qo'shildi!")

# Foydalanuvchidan malumotlarni so'rash
def foydalanuvchidan_malumot_olish():
    ism = input("Iltimos, ismingizni kiriting: ")
    familiya = input("Iltimos, familiyangizni kiriting: ")
    yosh = input("Iltimos, yoshingizni kiriting: ")
    jinsi = input("Iltimos, jinsingizni kiriting (Erkak/Ayol): ")
    
    return ism, familiya, yosh, jinsi

# Fayldan xodimlar ro'yxatini o'qish funksiyasi
def xodimlar_royxatini_korsat(fayl_nomi):
    try:
        with open(fayl_nomi, 'r', encoding='utf-8') as fayl:
            malumotlar = fayl.readlines()
            if malumotlar:
                print("\nXodimlar ro'yxati:")
                for i, xodim in enumerate(malumotlar, 1):
                    print(f"{i}. {xodim.strip()}")
            else:
                print("Xodimlar ro'yxati bo'sh.")
    except FileNotFoundError:
        print(f"{fayl_nomi} fayli topilmadi.")

# Asosiy menyu funksiyasi
def menyu():
    print("\n1. Xodim qoshish")
    print("2. Xodimlar ro'yxatini ko'rish")
    print("3. Dasturni tugatish")
    tanlov = input("\nTanlang (1/2/3): ")
    return tanlov

# Asosiy dastur
if __name__ == "__main__":
    fayl_nomi = "Xodimlar_malumotlari.txt"
    
    while True:
        tanlov = menyu()
        
        if tanlov == '1':
            ism, familiya, yosh, jinsi = foydalanuvchidan_malumot_olish()
            malumot_qoshish(fayl_nomi, ism, familiya, yosh, jinsi)
        
        elif tanlov == '2':
            xodimlar_royxatini_korsat(fayl_nomi)
        
        elif tanlov == '3':
            print("Dastur tugadi.")
            break
        
        else:
            print("Noto'g'ri tanlov. Iltimos, qayta tanlang.")
