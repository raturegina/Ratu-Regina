def fungsi_python():
    print("program menghitung konversi suhu")

print(str("pilih 1 untuk konversi suhu celcius ke kelvin "))
print(str("pilih 2 untuk konversi suhu celcius ke reamur "))
print(str("pilih 3 untuk konversi suhu celcius ke fahrenheit "))
operator= input("pilih : ")
if(operator=="1"):
    n= float(input("masukkan nilai : "))
    celcius= n + 273,15
    print(" hasilnya =" ,celcius,"derajat kelvin")
elif(operator == "2"):
    n= float(input("masukkan nilai : "))
    celcius= 4/5 * n
    print(" hasilnya =" ,celcius , "derajat reamur")
elif(operator=="3"):
    n= float(input("masukkan nilai : "))
    celcius= 9/5 * n + 32
    print( " hasilnya =" ,celcius,"derajat farenheit")
else:
    print("tidak ada dalam menu")

