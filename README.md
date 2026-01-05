# 🧠 Analisis Sintaks Bahasa Jawa Berbasis Context Free Grammar (CFG)

Proyek ini merupakan implementasi konsep **Teori Bahasa dan Otomata** yang berfokus pada **analisis sintaks kalimat Bahasa Jawa** menggunakan pendekatan **Context Free Grammar (CFG)**.
Program dirancang untuk memvalidasi **kalimat tunggal** berdasarkan aturan grammar yang dirumuskan secara formal serta menampilkan **parse tree** sebagai representasi struktur sintaks kalimat.

---

## 👨‍💻 Penulis

* **Muhammad Robi Ardita** (202410370110002)
* **Tegar Tutu Empar Pranata** (202410370110008)
* **Farid Al Farizi** (202410370110017)
* **Naufal Arkaan** (202410370110020)

---

## 🎯 Tujuan

Tujuan dari pengembangan program ini adalah:

1. Menerapkan konsep **Context Free Grammar (CFG)** pada analisis Bahasa Jawa.
2. Menganalisis struktur kalimat secara **runut dari simbol awal (start symbol) hingga simbol terminal**.
3. Menentukan **validitas sintaks kalimat** berdasarkan aturan grammar yang telah dirumuskan.
4. Menampilkan **parse tree** sebagai representasi struktur hierarkis kalimat.

---

## 📚 Landasan Teori

Program ini mengacu pada konsep utama dalam **Teori Bahasa dan Otomata**, khususnya:

* **Context Free Grammar (CFG)**
* Analisis sintaks (*syntax analysis*)
* Representasi struktur kalimat menggunakan **parse tree**

Dataset kosakata Bahasa Jawa digunakan **sebagai lexicon (simbol terminal)**, sedangkan **penentuan struktur kalimat sepenuhnya ditentukan oleh aturan CFG**, bukan oleh makna kata (semantik).

---

## 📐 Aturan Grammar (CFG)

Aturan Context Free Grammar (CFG) yang digunakan dalam program ini adalah sebagai berikut:

```
S   → NP VP
S   → NP
S   → VP

NP  → Pronoun
NP  → Noun
NP  → Det Noun

VP  → Verb
VP  → Verb NP
VP  → Verb Adv
VP  → Verb NP Adv
```

### Keterangan Non-Terminal

* **S**   : Kalimat (Start Symbol)
* **NP**  : Noun Phrase (Subjek / Objek)
* **VP**  : Verb Phrase (Predikat)
* **Det** : Determiner
* **Adv** : Adverb (Keterangan)

Grammar ini dirancang untuk mencerminkan struktur dasar kalimat Bahasa Jawa dengan pola **S–P–O–(K)**.

---

## 🗂️ Dataset

Dataset disimpan dalam file:

```
bahasa_jawa.xlsx
```

### Kolom yang Digunakan

* `Ngoko`
* `Krama Madya`
* `Krama Inggil`
* `Bahasa Indonesia`
* `Fungsi (SPOK)`

### Peran Dataset

* Dataset digunakan **hanya untuk membangun lexicon**, yaitu:

  * `PRONOUN`
  * `VERB`
  * `NOUN`
  * `ADVERB`
* Dataset **tidak digunakan untuk menentukan struktur grammar**, sehingga analisis tetap murni berbasis CFG.

---

## ⚙️ Cara Menjalankan Program

### 1️⃣ Instal dependensi

```bash
pip install pandas openpyxl
```

### 2️⃣ Jalankan program

```bash
python translate.py
```

### 3️⃣ Masukkan satu kalimat Bahasa Jawa

Contoh input:

```
aku adus banyu awan
```

---

## ✅ Contoh Kalimat Valid

Berikut contoh kalimat yang **sesuai dengan CFG**:

```
aku adus
aku adus banyu
aku adus awan
aku adus banyu awan
iki banyu
```

---

## ❌ Contoh Kalimat Tidak Valid

Berikut contoh kalimat yang **melanggar aturan CFG**:

```
aku banyu
adus aku
awan aku adus
```

---

## 🌳 Contoh Parse Tree

Contoh hasil parse tree dari kalimat:

```
aku adus banyu awan
```

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

Parse tree menunjukkan bahwa kalimat dapat diturunkan dari simbol awal `S` hingga simbol terminal sesuai aturan CFG.

---

## 🔍 Penentuan Validitas Kalimat

Sebuah kalimat dinyatakan:

* **VALID**, jika dapat diturunkan dari simbol awal `S` menggunakan aturan CFG dan menghasilkan parse tree yang sesuai.
* **TIDAK VALID**, jika melanggar aturan grammar, seperti:

  * Tidak memiliki predikat (Verb)
  * Urutan kata tidak sesuai
  * Struktur frasa tidak lengkap

---

## 📝 Catatan Penting

* Program ini dirancang untuk **satu kalimat tunggal per input**, sesuai konsep dasar CFG.
* Untuk menganalisis lebih dari satu kalimat, proses parsing dilakukan **secara terpisah**.
* Program ini **tidak membahas kalimat majemuk maupun analisis semantik**.

---

## 👨‍🎓 Konteks Akademik

Proyek ini dibuat sebagai pemenuhan tugas mata kuliah:

**Teori Bahasa dan Otomata**

dengan fokus pada:

* Perumusan aturan CFG
* Analisis sintaks runut
* Representasi parse tree
* Penentuan validitas kalimat


