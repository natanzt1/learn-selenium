def penjumlahan(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

def hitung_pajak(angka1):
    total_pajak = angka1*0.1
    return total_pajak

def hitung_pajak_dari_total_asset(angka1, angka2):
    hasil_penjumlahannya = penjumlahan(angka1, angka2)
    hasil_hitung_pajak = hitung_pajak(hasil_penjumlahannya);
    return hasil_hitung_pajak