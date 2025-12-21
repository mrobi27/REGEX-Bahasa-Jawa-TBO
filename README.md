# 📘 REGEX Bahasa Jawa – TBO

Repository ini berisi program **Python** untuk **Tugas Mata Kuliah Teori Bahasa dan Otomata (TBO)**.  
Program mengimplementasikan **Regular Expression (Regex)** untuk memvalidasi input serta mengenali **struktur kalimat Bahasa Jawa berpola SPOK (Subjek, Predikat, Objek, Keterangan)**.

---

## 🎯 Tujuan
- Menerapkan konsep **Regular Expression (Regex)**  
- Mengenali struktur **SPOK** pada kalimat Bahasa Jawa  
- Mengimplementasikan konsep **Teori Bahasa dan Otomata** dalam program sederhana

---

## 🧠 Cara Kerja Program
Program bekerja dalam dua tahap utama:
1. **Validasi Kalimat dengan Regex**  
   Input hanya diperbolehkan berisi huruf, spasi, dan tanda hubung (`-`)

2. **Analisis Struktur SPOK**  
   Setiap kata dicocokkan dengan dataset Bahasa Jawa (Ngoko, Krama Madya, dan Bahasa Indonesia) untuk menentukan fungsinya

Kalimat dinyatakan **VALID** apabila memiliki Subjek dan Predikat dengan urutan yang benar.

---

## 📂 Struktur Folder
```

TBO/
├── translate.py          # Program utama
├── bahasa_jawa.xlsx      # Dataset kosakata Bahasa Jawa
└── README.md             # Dokumentasi

````

---

## 🛠 Teknologi
- Python
- Pandas
- Regular Expression (`re`)
- Visual Studio Code

---

## ▶️ Menjalankan Program di VS Code

### 1. Buka Project
- Buka **Visual Studio Code**
- Pilih **File → Open Folder**
- Arahkan ke folder `TBO`

### 2. Buka Terminal VS Code
- Tekan **Ctrl + `**
- Pastikan terminal berada di folder project:
  ```bash
  pwd
````

atau di Windows:

```bash
dir
```

### 3. Install Dependency

```bash
pip install pandas openpyxl
```

### 4. Jalankan Program

```bash
python translate.py
```

---

## 📝 Contoh Penggunaan

**Input:**

```
aku mangan sega
```

**Output:**

```
Subjek     : aku
Predikat   : mangan
Objek      : sega
Keterangan :

Kalimat VALID (struktur SPOK benar)
```

---

## ⚠️ Aturan Validasi

* Input hanya boleh huruf, spasi, dan tanda `-`
* Kalimat harus memiliki Subjek dan Predikat
* Subjek harus muncul sebelum Predikat

---

## 🎓 Informasi Akademik

* Mata Kuliah : Teori Bahasa dan Otomata
* Dosen Pengampu : Ali Sofyan Kholimi, S.Kom., M.Kom.
* Program Studi : Informatika
* Universitas : Universitas Muhammadiyah Malang

---

## 👨‍💻 Penulis

* Muhammad Robi Ardita (202410370110002)
* Farid Al Farizi (202410370110017)
* Naufal Arkaan (202410370110020)

---

📌 *Repository ini dibuat untuk keperluan tugas akademik dan pembelajaran.*

````

---

## ✅ LANGKAH TERAKHIR (WAJIB)
Setelah README rapi di VS Code:

```bash
git add README.md
git commit -m "Update README for VS Code usage"
git push origin main
````
