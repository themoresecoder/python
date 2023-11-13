import random , time
sifre = ""
sifreler_icin = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi = int(input("Şifren kaç haneli olsun "))
print("Hmmm ... bir düşüneyim")
time.sleep(3)
for i in range(sayi):
    eleman = random.randint(0,71)
    sifre += sifreler_icin[eleman]
print(sifre)