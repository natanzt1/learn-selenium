from function_learning import *

uang_bank = 2000
uang_cash = 5000
# hasil_penjumlahan = penjumlahan(uang_bank, uang_cash)
# pajak = hitung_pajak(hasil_penjumlahan)
# print(pajak)

pajak_dari_total_asset = hitung_pajak_dari_total_asset(uang_bank, uang_cash)
print(pajak_dari_total_asset)