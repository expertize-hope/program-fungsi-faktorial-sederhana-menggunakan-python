import math

def hitung_dan_tampilkan_proses(angka):
        
        if angka < 0:
            raise ValueError("Faktorial tidak terdefinisi untuk bilangan negatif.")
        
        print(f"\nMenghitung {angka}!...")
        if angka == 0:
            print("Proses: 0! = 1 (sesuai definisi)")
            return 1
            
        else:
            hasil_proses = 1
            proses_str_list = [] 

            for i in range(angka, 0, -1):
                hasil_proses *= i
                proses_str_list.append(str(i))
            
            proses_str = " x ".join(proses_str_list)
            
            print(f"Proses: {proses_str}")
            
            return hasil_proses

input_pengguna = input("Masukkan sebuah bilangan bulat non-negatif dan selain huruf: ")

try:
        n = int(input_pengguna)
        hasil_akhir = hitung_dan_tampilkan_proses(n)

        print(f"Hasil : {hasil_akhir}")
        
        hasil_math = math.factorial(n)
        print("\nPengecekan dengan math.factorial...")
        print(f"Hasil dari math.factorial({n}) = {hasil_math}")
        
        if hasil_akhir == hasil_math:
            print("Hasil perhitungan proses dan math.factorial() SESUAI. ✅")

except ValueError as e:
        print(f"\nError: Input '{input_pengguna}' tidak valid.")
        print(f"Detail: {e}")
        print("Harap masukkan bilangan bulat non-negatif dan selain huruf (contoh: 0, 1, 5).")
