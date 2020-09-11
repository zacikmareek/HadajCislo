import random

cislo = random.randint(1,20)
pokus = 1

meno = input("Ahoj, ako sa volas?")

print("Ahoj", meno + ".", )

otazka = input("Chcel/a by si si zahrat hru? [a/n] ")

if otazka == "n":
    print("aha, nemas ma rad, okej...")

if otazka == "a":
    print("Myslim na jedno cislo od 1 po 20, hadaj na ake cislo myslim!")

hadaj = int(input("Hadaj na ake cislo myslim:"))

if hadaj > cislo:
    print("Myslim na mensie cislo, skus znova.")
if hadaj < cislo:
    print("Myslim na vacsie cislo, skus znova.")

while hadaj != cislo:
    pokus += 1
    hadaj = int(input("Tvoj typ: "))
    if hadaj < cislo:
        print("Myslim na vacsie cislo, skus znova: ")
    if hadaj > cislo:
        print("Myslim na mensie cislo, skus znova: ")
if hadaj == cislo:
    print("Tipol si si spravne, vyhral si! Myslel som na cislo", cislo , "a potreboval si" , pokus, "pokusy/ov")
            
input()

