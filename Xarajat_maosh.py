# Fayldan xodimlar royxatini oqish funksiyasi
def xodimlar_royxatini_korsat(fayl_nomi):
    try:
        with open(fayl_nomi, 'r', encoding='utf-8') as fayl:
            malumotlar = fayl.readlines()
            if not malumotlar:
                print("Xodimlar royxati bosh.")
            return malumotlar
    except FileNotFoundError:
        print(f"{fayl_nomi} fayli topilmadi.")
        return []

# Maoshlarni hisoblash funksiyasi
def maoshlarni_hisoblash(malumotlar):
    umumiy_maosh = 0
    xodim_maoshlari = []
    
    for malumot in malumotlar:
        try:
            # Maoshni olish (malumot qatorida "Maosh: " sozidan keyingi raqamni olish)
            maosh_qismi = malumot.split('Maosh: ')[-1].strip()  # "Maosh: "dan keyin bolgan qiymatni olamiz
            maosh = float(maosh_qismi)
            umumiy_maosh += maosh
            xodim_maoshlari.append(maosh)
        except (IndexError, ValueError):
            print(f"Maoshni olishda xatolik: {malumot.strip()}")
    
    return umumiy_maosh, xodim_maoshlari

# Asosiy dastur
if __name__ == "__main__":
    fayl_nomi = "Xodimlar_malumotlari.txt"
    
    # Fayldan xodim malumotlarini olish
    malumotlar = xodimlar_royxatini_korsat(fayl_nomi)
    
    # Maoshlarni hisoblash va natijani chiqarish
    if malumotlar:
        umumiy_maosh, xodim_maoshlari = maoshlarni_hisoblash(malumotlar)
        print(f"\nUmumiy maosh: {umumiy_maosh}")
        for i, maosh in enumerate(xodim_maoshlari, 1):
            print(f"{i}-xodimning maoshi: {maosh}")
