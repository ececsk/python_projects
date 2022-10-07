#Aklından bir sayı tut oyunu
from random import randint
def guess(number):
  user_number=int(input("Sayı tahmin oyunu için 1 ile 100 arasında bir tahminde bulun "))
  counter=0
  while number!=user_number:
    counter+=1
    if number<user_number:
      print("Üzgünüm, daha küçük bir tahminde bulunmalısın. ")
    else:
      print("Üzgünüm, daya büyük bir tahminde bulunmalısın. ")
    
    user_number=int(input("Lütfen, yeniden bir tahminde bulunun! "))
  else:
    print("Tebrikler,doğru tahmin!") 
  print(f"Tebrikler {counter}. denemede bildiniz.\n")

guess(randint(1,100))