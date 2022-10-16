def perfectNum(num1,num2):
  for sayi in range(num1,num2):
    total=0
    for i in range(1,sayi):
        if sayi%i==0:
            total+=i
        
    if total==sayi:
        print(sayi)


number1=int(input("Bir sayı girin: "))
number2=int(input("Bir sayı girin: "))

perfectNum(number1,number2)
