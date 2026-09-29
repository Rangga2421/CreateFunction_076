#1. Fungsi konversi suhu
def konversi_suhu(suhu, satuan):
    if satuan == 'C':
        # Celsius ke Fahrenheit
        hasil = (suhu * 9/5) + 32
        return hasil
    elif satuan == 'F':
        # Fahrenheit ke Celsius
        hasil = (suhu - 32) * 5/9
        return hasil
    else:
        return "Satuan tidak valid!"

