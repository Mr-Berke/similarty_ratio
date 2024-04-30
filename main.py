import math
import sqlite3
from collections import Counter

def benzerlik(metin1, metin2):
    def kelime_say(metin):
        return Counter(metin.split())

    def vektor(vektor):
        return math.sqrt(sum(value ** 2 for value in vektor.values()))

    kelime_sayısı1 = kelime_say(metin1)
    kelime_sayısı2 = kelime_say(metin2)

    birlikte_geçen_kelimeler = set(kelime_sayısı1.keys()) & set(kelime_sayısı2.keys())

    toplam = sum(kelime_sayısı1[kelime] * kelime_sayısı2[kelime] for kelime in birlikte_geçen_kelimeler)

    vektor1 = vektor(kelime_sayısı1)
    vektor2 = vektor(kelime_sayısı2)

    return toplam / (vektor1 * vektor2)

def main():
    text1 = input("İlk metni giriniz: ")
    text2 = input("İkinci metni giriniz: ")

    benzerlik1 = benzerlik(text1, text2)
    print("Metinler arasındaki  benzerlik katsayısı:", benzerlik1)

    bağlantı = sqlite3.connect('texts.db')
    c = bağlantı.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS texts (id INTEGER PRIMARY KEY, text TEXT)")
    c.execute("INSERT INTO texts (text) VALUES (?)", (text1,))
    c.execute("INSERT INTO texts (text) VALUES (?)", (text2,))
    bağlantı.commit()

    with open("benzerlik_durumu.txt", "w") as d:
        d.write("Metinler arasındaki benzerlik katsayısı: {}\n".format(benzerlik1))

    bağlantı.close()

if __name__ == "__main__":
    main()
