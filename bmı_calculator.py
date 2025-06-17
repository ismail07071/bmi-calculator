def bmı_hesap(b,k):
    return k/b**2

print("BMI(Vücut Kitle Endeksi) uygulamasına hoşgeldiniz.Lütfen boy ve kilo değerinizi sırasıyla giriniz.\n")

while True:
    try:
        boy = int(input("Boyunuz: "))
        kilo = int(input("Kilonuz: "))
        boy_metre = boy / 100
        bmi_deger = bmı_hesap(boy_metre,kilo)
    except ValueError:
        print("Lütfen sayısal bir değer giriniz.")
        continue
    except ZeroDivisionError:
        print("Lütfen boyunuzu sıfırdan farklı bir değer girin.")
        continue
    break

print(f"Vücut kitle endeksiniz: {bmi_deger:.2f}")
if bmi_deger >= 40:
    print("Durumunuz: 3. derece (morbid) obez")
elif bmi_deger >= 35:
    print("Durumunuz: 2. derece obez")
elif bmi_deger >= 30:
    print("Durumunuz: 1. derece obez")
elif bmi_deger >= 25:
    print("Durumunuz: Fazla kilolu (Overweight)")
elif bmi_deger >= 18.5:
    print("Durumunuz: Normal kilolu")
else:
    print("Durumunuz: Zayıf")



