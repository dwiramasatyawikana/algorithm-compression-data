def lzw_compress(uncompressed: str) -> list:
    """Mengompresi string menjadi list kode (integer) menggunakan LZW."""
    # 1. Bangun kamus awal yang berisi 256 karakter ASCII dasar
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    
    w = ""
    result = []
    
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            # Jika pola wc sudah ada di kamus, perpanjang string w
            w = wc
        else:
            # Jika tidak ada, keluarkan kode untuk w
            result.append(dictionary[w])
            # Tambahkan pola baru wc ke dalam kamus
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    
    # Keluarkan kode untuk karakter terakhir yang tersisa
    if w:
        result.append(dictionary[w])
        
    return result


def lzw_decompress(compressed: list) -> str:
    """Mendekompresi list kode (integer) kembali menjadi string menggunakan LZW."""
    # 1. Bangun kamus awal yang sama dengan saat kompresi
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}
    
    # Tangani elemen pertama
    w = chr(compressed[0])
    result = [w]
    
    for k in compressed[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            # Kasus khusus: jika kode baru merujuk pada dirinya sendiri (cScSc)
            entry = w + w[0]
        else:
            raise ValueError(f'Kode kompresi tidak valid: {k}')
            
        result.append(entry)
        
        # Tambahkan pola baru ke dalam kamus
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
        
    return "".join(result)

# ==========================================
# Contoh Penggunaan / Testing
# ==========================================
if __name__ == "__main__":
    data_asli = "TOBEORNOTTOBEORTOBEORNOT"
    print(f"Data Asli      : {data_asli}")
    
    data_kompresi = lzw_compress(data_asli)
    print(f"Hasil Kompresi : {data_kompresi}")
    
    data_dekompresi = lzw_decompress(data_kompresi)
    print(f"Hasil Dekompresi: {data_dekompresi}")
    
    assert data_asli == data_dekompresi, "Gagal! Data asli dan dekompresi tidak sama."
    print("Status: Kompresi dan Dekompresi Berhasil Lossless!")