# 🧠 Analisis Sintaks Bahasa Jawa Berbasis Context Free Grammar (CFG)

Proyek ini merupakan implementasi **Teori Bahasa dan Otomata** untuk menganalisis **struktur sintaks kalimat Bahasa Jawa** menggunakan pendekatan **Context Free Grammar (CFG)**.  
Program dirancang untuk memvalidasi **kalimat tunggal** berdasarkan aturan grammar dan menampilkan **parse tree** sebagai representasi struktur kalimat.

---

## 👨‍💻 Penulis

* **Muhammad Robi Ardita** (202410370110002)  
* **Tegar Tutu Empar Pranata** (202410370110008)  
* **Farid Al Farizi** (202410370110017)  
* **Naufal Arkaan** (202410370110020)

---

## 🎯 Tujuan
Tujuan dari program ini adalah:
1. Menerapkan konsep **Context Free Grammar (CFG)** pada Bahasa Jawa.
2. Menganalisis struktur kalimat secara **runut dari simbol awal hingga terminal**.
3. Menentukan **validitas kalimat** berdasarkan aturan grammar.
4. Menampilkan **parse tree** sebagai representasi struktur sintaks.

---

## 📚 Landasan Teori
Program ini mengacu pada konsep utama dalam **Teori Bahasa dan Otomata**, khususnya:
- **Context Free Grammar (CFG)**
- Analisis sintaks (syntax analysis)
- Parse tree sebagai representasi struktur kalimat

Dataset kosa kata Bahasa Jawa digunakan **sebagai lexicon (simbol terminal)**, sedangkan proses parsing dan validasi kalimat dilakukan **sepenuhnya berdasarkan aturan CFG**, bukan berdasarkan makna kata (semantik).

---

## 📐 Aturan Grammar (CFG)

Grammar yang digunakan dalam program ini adalah sebagai berikut:

```

S   → NP VP
NP  → Pronoun
NP  → Noun
NP  → Det Noun
VP  → Verb
VP  → Verb NP
VP  → Verb Adv
VP  → Verb NP Adv

```

Keterangan:
- **S**  : Kalimat
- **NP** : Noun Phrase (Subjek / Objek)
- **VP** : Verb Phrase (Predikat)
- **Det**: Determiner
- **Adv**: Adverb (Keterangan)

---

## 🗂️ Dataset
Dataset disimpan dalam file:

```

bahasa_jawa.xlsx

````

Kolom yang digunakan:
- `Ngoko`
- `Krama Madya`
- `Bahasa Indonesia`
- `Fungsi (SPOK)`

Dataset digunakan **hanya untuk membangun lexicon** (Pronoun, Verb, Noun, Adverb) dan **tidak digunakan untuk menentukan struktur grammar**.

---

## ⚙️ Cara Menjalankan Program

### 1️⃣ Pastikan dependensi terpasang
```bash
pip install pandas openpyxl
````

### 2️⃣ Jalankan program

```bash
python translate.py
```

### 3️⃣ Masukkan satu kalimat Bahasa Jawa

Contoh:

```
aku adus banyu awan
```

---

## ✅ Contoh Kalimat Valid

```
aku adus
aku adus banyu
aku adus awan
aku adus banyu awan
aku adus iki banyu
```

## ❌ Contoh Kalimat Tidak Valid

```
aku banyu
adus aku
awan aku adus
```

---

## 🌳 Contoh Parse Tree

```
S
├── NP
│   └── Pronoun (aku)
└── VP
    ├── Verb (adus)
    ├── NP
    │   └── Noun (banyu)
    └── Adv (awan)
```

---

## 🔍 Penentuan Validitas Kalimat

Kalimat dinyatakan:

* **VALID** jika dapat diturunkan dari simbol awal `S` hingga simbol terminal sesuai CFG.
* **TIDAK VALID** jika melanggar aturan grammar (misalnya tidak ada predikat atau urutan tidak sesuai).

---

## 📝 Catatan Penting

* Program ini **dirancang untuk satu kalimat tunggal per input**, sesuai dengan konsep CFG.
* Untuk menganalisis lebih dari satu kalimat, proses parsing dilakukan **secara terpisah**.
* Program ini tidak membahas kalimat majemuk atau analisis semantik.

---

## 👨‍🎓 Konteks Akademik

Proyek ini dibuat sebagai pemenuhan tugas mata kuliah:

**Teori Bahasa dan Otomata**

dengan fokus pada:

* Perumusan CFG
* Analisis sintaks runut
* Representasi parse tree
* Validasi kalimat

---

