#Biz bir sayı belirleyerek bilgisayarın bu sayıyı tahmin etmesini sağlayalım.
import random

def computer_guess(x):
  start=1
  end=100
  result=""
  while result!="d":
    guess=random.randint(start,end)

    result=input(f"{guess} değeri aklından tuttuğun değerden büyükse (b), küçükse (k), doğruysa (d) giriniz.").lower()  #lower ile girilen karakterleri büyükse küçük harfe dönüştürür
    if result=="b":
      end=guess-1
    elif result=="k":
      start=guess+1
  print("Tebrikler, doğru tahmin") #buraya else yazmasakta döngüden çıktığı için aynı şekilde çalışacaktır.
    

computer_guess(29)