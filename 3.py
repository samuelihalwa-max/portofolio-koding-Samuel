harga_sepatu = int(input("Masukkan Harga Sepatu: "))
jumlah_beli = int(input("Masukkan Jumlah Beli: "))

total = harga_sepatu * jumlah_beli

if total > 500000:
    total_akhir = total - 50000
    print("Mendapat potongan harga Rp50.000!")
else:
    total_akhir = total

print(f"Total akhir yang harus dibayar: Rp{total_akhir}")