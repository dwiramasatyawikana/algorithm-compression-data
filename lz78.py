def lz78_compress(data: str) -> list:
    """Mengompresi string menggunakan algoritma LZ78."""
    # Inisialisasi kamus dengan string kosong di indeks 0
    dictionary = {"": 0}
    dict_size = 1
    compressed = []
    
    w = ""
    for c in data:
        wc = w + c
        if wc in dictionary:
            # Jika pola wc sudah ada di kamus, perpanjang pembacaan
            w = wc
        else:
            # Jika tidak ada, keluarkan token (indeks dari w, karakter c)
            compressed.append((dictionary[w], c))
            
            # Tambahkan pola baru wc ke dalam kamus
            dictionary[wc] = dict_size
            dict_size += 1
            
            # Reset w untuk pola berikutnya
            w = ""
            
    # Tangani sisa karakter di akhir string (jika loop selesai tapi w masih ada isinya)
    if w:
        compressed.append((dictionary[w], ""))
        
    return compressed


def lz78_decompress(compressed: list) -> str:
    """Mendekompresi list token LZ78 kembali menjadi string."""
    # Inisialisasi kamus awal yang sama (0 = string kosong)
    dictionary = {0: ""}
    dict_size = 1
    decompressed = ""
    
    for index, char in compressed:
        # Rekonstruksi kata: ambil dari kamus berdasarkan indeks, lalu tambah karakter baru
        word = dictionary[index] + char
        decompressed += word
        
        # Masukkan kata baru ke kamus
        dictionary[dict_size] = word
        dict_size += 1
        
    return decompressed


# ==========================================
# Contoh Penggunaan / Testing
# ==========================================
if __name__ == "__main__":
    # Teks uji coba
    teks_uji = "ABRACADABRA" 
    print(f"Data Input: {teks_uji}\n")
    
    hasil_lz78 = lz78_compress(teks_uji)
    
    print("Token Kompresi LZ78 (Indeks Kamus, Karakter):")
    for token in hasil_lz78:
        print(token)
        
    print("\n")
    
    hasil_dekompresi = lz78_decompress(hasil_lz78)
    print(f"Hasil Dekompresi: {hasil_dekompresi}")
    
    assert teks_uji == hasil_dekompresi, "Gagal! Data asli dan dekompresi tidak sama."
    print("Status: Kompresi dan Dekompresi Berhasil Lossless!")