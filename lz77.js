/**
 * Mengompresi string menggunakan algoritma LZ77
 * @param {string} data - Teks asli yang akan dikompresi
 * @param {number} searchWindow - Ukuran maksimal buffer mundur
 * @param {number} lookaheadWindow - Ukuran maksimal buffer maju
 * @returns {Array} Array of arrays (jarak, panjang, karakter_selanjutnya)
 */
function lz77Compress(data, searchWindow = 20, lookaheadWindow = 15) {
    let i = 0;
    let compressed = [];

    while (i < data.length) {
        let matchLength = 0;
        let matchDistance = 0;

        // Tentukan batas pencarian ke belakang dan ke depan
        let startWindow = Math.max(0, i - searchWindow);
        let endLookahead = Math.min(data.length, i + lookaheadWindow);

        // Cari pola terpanjang di dalam Search Buffer
        for (let j = startWindow; j < i; j++) {
            let length = 0;
            while ((i + length < endLookahead) && (data[j + length] === data[i + length])) {
                length++;
            }

            if (length > matchLength) {
                matchLength = length;
                matchDistance = i - j;
            }
        }

        // Tentukan karakter berikutnya setelah pola (jika ada)
        let nextChar = (i + matchLength < data.length) ? data[i + matchLength] : "";
        
        // Simpan token kompresi [Jarak, Panjang, Karakter]
        compressed.push([matchDistance, matchLength, nextChar]);
        
        // Geser jendela (Sliding Window) maju
        i += matchLength + 1;
    }

    return compressed;
}

/**
 * Mendekompresi hasil kompresi LZ77 kembali menjadi string
 * @param {Array} compressed - Array hasil kompresi LZ77
 * @returns {string} String asli yang telah direkonstruksi
 */
function lz77Decompress(compressed) {
    let decompressed = "";

    for (let k = 0; k < compressed.length; k++) {
        let distance = compressed[k][0];
        let length = compressed[k][1];
        let nextChar = compressed[k][2];

        if (distance === 0 && length === 0) {
            decompressed += nextChar;
        } else {
            let startPos = decompressed.length - distance;
            for (let step = 0; step < length; step++) {
                decompressed += decompressed[startPos + step];
            }
            decompressed += nextChar;
        }
    }

    return decompressed;
}

// ==========================================
// Contoh Penggunaan / Eksekusi
// ==========================================
const teksUji = "BANANABANANABANANABANANA";
console.log("Data Asli      :", teksUji, "\n");

const hasilKompresi = lz77Compress(teksUji);
console.log("Hasil Kompresi (Token LZ77):");
console.table(hasilKompresi); // Menggunakan console.table agar output lebih rapi di browser

const hasilDekompresi = lz77Decompress(hasilKompresi);
console.log("\nHasil Dekompresi:", hasilDekompresi);

if (teksUji === hasilDekompresi) {
    console.log("Status: Kompresi dan Dekompresi Berhasil Lossless!");
}