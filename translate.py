# =====================================================
# IMPORT LIBRARY
# =====================================================
# pandas: Library untuk membaca dan memanipulasi data dari file Excel
# re: Library untuk Regular Expression (pencocokan pola teks)
import pandas as pd
import re

# =====================================================
# MEMBACA DATA DARI FILE EXCEL
# =====================================================
# Membaca file "bahasa_jawa.xlsx" yang berisi kamus kata Bahasa Jawa
# Data akan disimpan dalam DataFrame (tabel) bernama 'df'
df = pd.read_excel("bahasa_jawa.xlsx")

# =====================================================
# ATURAN KATA (KATEGORI LEKSIKAL)
# =====================================================
# Mendefinisikan 9 kategori kata yang akan digunakan dalam parser
# Set kosong akan diisi dari file Excel, set dengan nilai adalah hardcoded

#Aturan kata
PRONOUN = set()      # Kata ganti (aku, kowe, dheweke) - diisi dari Excel kolom S
VERB = set()         # Kata kerja (mangan, turu, lunga) - diisi dari Excel kolom P
NOUN = set()         # Kata benda (sega, omah, buku) - diisi dari Excel kolom O
ADVERB = set()       # Kata keterangan (saiki, wingi, sesuk) - diisi dari Excel kolom K

# Kategori kata yang didefinisikan langsung (hardcoded)
DETERMINER = {"iki", "iku"}  # Kata penentu: iki = ini, iku = itu
ADJECTIVE = {"apik", "ala", "gedhe", "cilik", "ayu", "bagus", "elek", "resik", "reged", "adhem", "panas", "anyar", "lawas"}  # Kata sifat
CONJUNCTION = {"lan", "utawa", "nanging", "yen", "amarga", "supaya", "karo", "sarta"}  # Kata hubung
PREPOSITION = {"ing", "saka", "menyang", "kanggo", "tanpa", "karo", "nganti", "sadurunge"}  # Kata depan
INTERJECTION = {"wah", "lho", "ya", "ayo", "aduh", "hore", "eh", "oh", "ah"}  # Kata seru

# =====================================================
# SAFE SPLIT (REGEX VERSION)
# =====================================================
# Fungsi untuk memecah string menjadi list kata-kata
# Menangani nilai kosong (NaN) dan karakter pemisah (koma, spasi, slash)
def split_safe(value):
    # Jika nilai kosong (NaN), kembalikan list kosong
    if pd.isna(value):
        return []
    # Ubah ke lowercase untuk konsistensi
    value = str(value).lower()
    # Ganti semua pemisah (koma, spasi, slash) menjadi slash
    value = re.sub(r"[,\s/]+", "/", value)
    # Ambil semua kata yang hanya berisi huruf a-z
    return re.findall(r"[a-z]+", value)

# =====================================================
# BUILD LEXICON (MEMBANGUN KAMUS KATA)
# =====================================================
# Membaca setiap baris dari file Excel dan mengisi kategori kata
# berdasarkan kolom "Fungsi (SPOK)" yang menentukan peran kata
for _, row in df.iterrows():
    # Ambil fungsi SPOK dan ubah ke uppercase
    fungsi = str(row["Fungsi (SPOK)"]).upper()

    # Kumpulkan semua varian kata (Ngoko, Krama Madya, Krama Inggil, Indonesia)
    kata_set = set()
    kata_set.update(split_safe(row["Ngoko"]))        # Bahasa Jawa Ngoko (kasar)
    kata_set.update(split_safe(row["Krama Madya"]))  # Bahasa Jawa Krama Madya (sedang)
    kata_set.update(split_safe(row["Krama Inggil"])) # Bahasa Jawa Krama Inggil (halus)
    kata_set.update(split_safe(row["Bahasa Indonesia"]))  # Terjemahan Indonesia

    # Masukkan kata ke kategori sesuai fungsinya
    if "S" in fungsi:        # S = Subjek → masuk PRONOUN
        PRONOUN.update(kata_set)
    if "P" in fungsi:        # P = Predikat → masuk VERB
        VERB.update(kata_set)
    if "O" in fungsi:        # O = Objek → masuk NOUN
        NOUN.update(kata_set)
    if "K" in fungsi:        # K = Keterangan → masuk ADVERB
        ADVERB.update(kata_set)

# =====================================================
# GABUNGAN SEMUA TERMINAL (KATA YANG DIKENALI)
# =====================================================
# Menggabungkan semua kategori kata menjadi satu set
# Digunakan untuk validasi apakah kata input dikenali atau tidak
ALL_TERMINALS = PRONOUN | VERB | NOUN | ADVERB | DETERMINER | ADJECTIVE | CONJUNCTION | PREPOSITION | INTERJECTION

# =====================================================
# CONTEXT FREE GRAMMAR PARSER
# =====================================================
# Fungsi untuk menganalisis struktur kalimat berdasarkan aturan CFG
# Mengembalikan (True, tree) jika valid, (False, pesan_error) jika tidak
#
# ATURAN KALIMAT:
#   S → VP              (Kalimat imperatif/perintah)
#   S → NP VP           (Kalimat lengkap: Subjek + Predikat)
#   S → NP              (Kalimat nominal: hanya Subjek)
#
# ATURAN FRASA:
#   NP → Det Noun | Pronoun | Noun
#   VP → Verb (NP)? (Adv)?
def parse_sentence(words):
    tree = []       # List untuk menyimpan struktur pohon sintaks
    index = 0       # Penunjuk posisi kata saat ini
    n = len(words)  # Jumlah total kata

    # Root node: S (Sentence/Kalimat)
    tree.append("S")

    # -------------------------------------------------
    # ATURAN 1: S → VP (Kalimat Imperatif/Perintah)
    # Kalimat yang dimulai dengan kata kerja (tanpa subjek eksplisit)
    # Contoh: "mangan!", "turu saiki!", "mangan sega!"
    # -------------------------------------------------
    if index < n and words[index] in VERB:
        # Tambahkan VP (Verb Phrase) ke pohon
        tree.append("└── VP")
        tree.append(f"    └── Verb ({words[index]})")
        index += 1  # Pindah ke kata berikutnya

        # Cek apakah ada objek (NOUN) setelah verb → VP → Verb NP
        if index < n and words[index] in NOUN:
            # Ubah format tree untuk menampilkan cabang
            tree[-1] = f"    ├── Verb ({tree[-1].split('(')[1].rstrip(')')})"
            tree.append("    ├── NP")
            tree.append(f"    │   └── Noun ({words[index]})")
            index += 1

        # Cek apakah ada keterangan (ADVERB) di akhir → VP → ... Adv
        if index < n and words[index] in ADVERB:
            tree.append(f"    └── Adv ({words[index]})")
            index += 1

        # Jika semua kata sudah diproses, kalimat VALID
        if index == n:
            return True, "\n".join(tree)
        # Jika masih ada kata tersisa, struktur tidak sesuai
        return False, "❌ Struktur tidak sesuai CFG"

    # -------------------------------------------------
    # ATURAN 2: S → NP VP (Kalimat Lengkap)
    # Kalimat yang dimulai dengan subjek (NP) diikuti predikat (VP)
    # Contoh: "aku mangan", "kowe turu", "iki buku"
    # -------------------------------------------------
    
    # Tambahkan NP (Noun Phrase) untuk Subjek
    tree.append("├── NP")

    # ATURAN FRASA NP: NP → Det Noun (Determiner + Kata Benda)
    # Contoh: "iki buku" (ini buku), "iku kucing" (itu kucing)
    if index < n and words[index] in DETERMINER:
        tree.append(f"│   ├── Det ({words[index]})")
        index += 1
        # Setelah determiner harus ada noun
        if index < n and words[index] in NOUN:
            tree.append(f"│   └── Noun ({words[index]})")
            index += 1
        else:
            return False, "❌ NP tidak lengkap"

    # ATURAN FRASA NP: NP → Pronoun (Kata Ganti)
    # Contoh: "aku", "kowe", "dheweke"
    elif index < n and words[index] in PRONOUN:
        tree.append(f"│   └── Pronoun ({words[index]})")
        index += 1

    # ATURAN FRASA NP: NP → Noun (Kata Benda sebagai Subjek)
    # Contoh: "bapak", "ibu", "kucing"
    elif index < n and words[index] in NOUN:
        tree.append(f"│   └── Noun ({words[index]})")
        index += 1

    # Jika tidak ada yang cocok, berarti tidak ada subjek
    else:
        return False, "❌ Tidak ada Subjek"

    # ATURAN 3: S → NP (Kalimat Nominal - hanya subjek tanpa predikat)
    # Jika semua kata sudah diproses setelah NP, kalimat tetap VALID
    if index == n:
        return True, "\n".join(tree)

    # -------------------------------------------------
    # Lanjutan ATURAN 2: Bagian VP (Verb Phrase) untuk Predikat
    # -------------------------------------------------
    tree.append("└── VP")

    # ATURAN FRASA VP: VP → Verb (Kata Kerja sebagai Predikat)
    if index < n and words[index] in VERB:
        tree.append(f"    └── Verb ({words[index]})")
        index += 1
    else:
        return False, "❌ Tidak ada Predikat"

    # ATURAN FRASA VP: VP → Verb NP (Kata Kerja + Objek)
    # Contoh: "mangan sega", "tuku buku"
    if index < n and words[index] in NOUN:
        # Ubah format untuk menampilkan cabang
        tree[-1] = f"    ├── Verb ({tree[-1].split('(')[1].rstrip(')')})"
        tree.append("    ├── NP")
        tree.append(f"    │   └── Noun ({words[index]})")
        index += 1

    # ATURAN FRASA VP: VP → ... Adv (Menambahkan Keterangan)
    # Contoh: "mangan sega saiki", "turu wingi"
    if index < n and words[index] in ADVERB:
        tree.append(f"    └── Adv ({words[index]})")
        index += 1

    # Jika semua kata sudah diproses, kalimat VALID
    if index == n:
        return True, "\n".join(tree)

    # Jika masih ada kata tersisa, struktur tidak sesuai CFG
    return False, "❌ Struktur tidak sesuai CFG"

# =====================================================
# MAIN PROGRAM (PROGRAM UTAMA)
# =====================================================
# Loop utama untuk menerima input kalimat dari pengguna
# dan melakukan analisis sintaks
while True:
    # Minta input kalimat dari pengguna
    # .lower() = ubah ke huruf kecil, .strip() = hapus spasi di awal/akhir
    kalimat = input("\nMasukkan kalimat Bahasa Jawa: ").lower().strip()

    # -------------------------------------------------
    # REGEX TOKENIZER
    # -------------------------------------------------
    # Memecah kalimat menjadi list kata menggunakan regex
    # Hanya mengambil karakter huruf a-z (mengabaikan tanda baca, angka)
    words = re.findall(r"[a-z]+", kalimat)

    # -------------------------------------------------
    # VALIDASI KATA
    # -------------------------------------------------
    # Cek apakah semua kata dikenali (ada di ALL_TERMINALS)
    unknown_words = [w for w in words if w not in ALL_TERMINALS]
    if unknown_words:
        # Jika ada kata tidak dikenal, tampilkan daftar kata tersebut
        print("\n❌ Kata tidak dikenal:")
        for w in unknown_words:
            print(f" - {w}")
        # Tanya apakah user ingin melanjutkan
        lanjut = input("\nLanjut? (y/n): ").lower()
        if lanjut != "y":
            break  # Keluar dari loop jika tidak ingin lanjut
        continue   # Kembali ke awal loop untuk input baru

    # -------------------------------------------------
    # ANALISIS SINTAKS
    # -------------------------------------------------
    # Panggil fungsi parser untuk menganalisis struktur kalimat
    valid, result = parse_sentence(words)

    # -------------------------------------------------
    # TAMPILKAN HASIL
    # -------------------------------------------------
    print("\n=== HASIL ANALISIS SINTAKS ===")
    if valid:
        print("VALID (CFG)\n")
        print(result)  # Tampilkan pohon sintaks
    else:
        print("TIDAK VALID")
        print(result)  # Tampilkan pesan error

    # Tanya apakah user ingin menganalisis kalimat lain
    if input("\nLanjut? (y/n): ").lower() != "y":
        break  # Keluar dari loop jika tidak ingin lanjut
