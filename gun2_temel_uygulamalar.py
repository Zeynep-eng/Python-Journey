# ==========================================================
# Python Öğrenme Yolculuğu - 2. Gün
# Konu: Temel Veri Tipleri, Dönüşümler ve Hesaplamalar
# ==========================================================

# --- UYGULAMA 1: İki Sayının Toplamı ---
print("--- Sayı Toplama Uygulaması ---")

number1 = int(input("birinci Sayıyı Gir:"))
number2 = int(input("ikinci Sayıyı Gir:"))

sum = number1 + number2
print("Toplam:", sum)


print("\n----------------------------------------\n")


# --- UYGULAMA 2: Dairenin Alanı ve Çevresi ---
# dairenin alanı: pi*r*r
# dairenin çevresi: 2*pi*r

pi = 3.14159

radius_of_circle = float(input("Yarı çap:"))

area_of_circle = pi * radius_of_circle * radius_of_circle
circumference_of_circle = 2 * pi * radius_of_circle

print("Alan:", area_of_circle)
print("Çevre:", circumference_of_circle)
