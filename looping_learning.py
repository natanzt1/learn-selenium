nama = "dipa"
umur = 24

nama_pelanggan = ['Andi', 'Budi', 'Ilham', "Veggy", "Trio", "Satria"]
umur_pelanggan = [22, 26, 28, 17, 35]
pelanggan_genap = []
pelanggan_dengan_huruf_i = []
umur_pelanggan_muda = []

# for index in range(2, len(nama_pelanggan)):
#     if index % 2 != 0:
#         pelanggan_genap.append(nama_pelanggan[index])
#
# print(pelanggan_genap)

# for index in range(0, len(nama_pelanggan)):
#     if "i" in nama_pelanggan[index]:
#         pelanggan_dengan_huruf_i.append(nama_pelanggan[index])
#
# print(pelanggan_dengan_huruf_i)

for index in range(0, len(umur_pelanggan)):
    if umur_pelanggan[index] < 25:
        umur_pelanggan_muda.append(umur_pelanggan[index])

print(umur_pelanggan_muda)