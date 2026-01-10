# 🧠 Analisis Sintaks Bahasa Jawa Berbasis Context Free Grammar (CFG)

Proyek ini merupakan implementasi konsep **Teori Bahasa dan Otomata** yang berfokus pada **analisis sintaks kalimat Bahasa Jawa** menggunakan pendekatan **Context Free Grammar (CFG)**.
Program dirancang untuk memvalidasi **kalimat tunggal Bahasa Jawa** berdasarkan aturan grammar formal serta menampilkan **parse tree** sebagai representasi struktur sintaks kalimat.

---

## 👨‍💻 Penulis

* **Muhammad Robi Ardita** (202410370110002)
* **Tegar Tutu Empar Pranata** (202410370110008)
* **Farid Al Farizi** (202410370110017)
* **Naufal Arkaan** (202410370110020)

---

## 🎯 Tujuan

Tujuan pengembangan program ini adalah:

1. Menerapkan konsep **Context Free Grammar (CFG)** pada analisis sintaks Bahasa Jawa.
2. Menganalisis struktur kalimat secara **runut dari simbol awal (*start symbol*) hingga simbol terminal**.
3. Menentukan **validitas sintaks kalimat** berdasarkan aturan grammar yang dirumuskan.
4. Menampilkan **parse tree** sebagai representasi struktur hierarkis kalimat.

---

## 📚 Landasan Teori

Program ini mengacu pada konsep utama dalam **Teori Bahasa dan Otomata**, khususnya:

* **Context Free Grammar (CFG)**
* Analisis sintaks (*syntax analysis*)
* Representasi struktur kalimat menggunakan **parse tree**

Analisis dilakukan berdasarkan **fungsi sintaksis bahasa Jawa**, seperti **Subjek, Predikat, Objek, Pelengkap, dan Keterangan**, tanpa mempertimbangkan aspek makna (semantik).

---

## 📐 Aturan Grammar (CFG)

Aturan **Context Free Grammar (CFG)** yang digunakan dalam program ini adalah sebagai berikut:

```
S   → NP VP
S   → NP Adv VP
S   → VP

NP  → Noun
NP  → Pronoun
NP  → ProperNoun

VP  → Verb
VP  → Verb Verb
VP  → Verb NP
VP  → Verb NP NP
VP  → VP K

K   → Adv
K   → Prep Noun
```

### Keterangan Non-Terminal

* **S**   : Kalimat (*Start Symbol*)
* **NP**  : Frasa Nomina (Subjek / Objek / Pelengkap)
* **VP**  : Frasa Verba (Predikat)
* **K**   : Keterangan
* **Adv** : Adverbia
* **Prep**: Preposisi

Grammar ini dirancang untuk merepresentasikan struktur dasar kalimat Bahasa Jawa berdasarkan **fungsi sintaksis**, bukan pola linier SPOK semata.

---

## 🗂️ Leksikon (Lexicon)

Leksikon didefinisikan **secara eksplisit di dalam program** dan mencakup kategori kata berikut:

* **Noun**      : *buku, kalung, koran, asrama, perpustakaan*
* **Pronoun**   : *aku, kowe, dheweke*
* **Verb**      : *maca, sinau, nyilih, maringi, arep, manggon*
* **Adverb**    : *lagi, wis*
* **Preposition** : *neng, ing, menyang*

Nama orang (**Proper Noun**) dikenali secara otomatis dari input.

---

## ⚙️ Cara Menjalankan Program

### 1️⃣ Jalankan program

```bash
python parser_jawa.py
```

### 2️⃣ Masukkan satu kalimat Bahasa Jawa

Contoh input:

```
Anake lagi maca koran
```

---

## ✅ Contoh Kalimat Valid

Berikut contoh kalimat yang **sesuai dengan aturan CFG**:

```
Rani nyilih buku
Ibu maringi aku kalung
Anake lagi maca koran
Adhine sinau neng perpustakaan
Dheweke arep manggon neng asrama
```

---

## ❌ Contoh Kalimat Tidak Valid

Berikut contoh kalimat yang **melanggar aturan CFG**:

```
adus aku
aku buku
awan aku maca
```

---

## 🌳 Contoh Parse Tree

Contoh hasil *parse tree* dari kalimat:

```
Anake lagi maca koran
```

```
S
├── NP
│   └── N (anake)
├── AdvP
│   └── Adv (lagi)
└── VP
    ├── V (maca)
    └── NP
        └── N (koran)
```

*Parse tree* menunjukkan bahwa kalimat dapat diturunkan dari simbol awal **S** hingga simbol terminal sesuai aturan CFG.

---

## 🔍 Penentuan Validitas Kalimat

Sebuah kalimat dinyatakan:

* **VALID**, jika dapat diturunkan dari simbol awal **S** menggunakan aturan CFG dan menghasilkan *parse tree* yang sesuai.
* **TIDAK VALID**, jika melanggar aturan grammar, seperti:

  * Urutan kata tidak sesuai
  * Struktur frasa tidak lengkap
  * Predikat tidak ditemukan

---

## 📝 Catatan Penting

* Program ini dirancang untuk **satu kalimat tunggal per input**.
* Analisis dilakukan **murni pada aspek sintaksis**, bukan semantik.
* Program **tidak mendukung kalimat majemuk**.

---

## 👨‍🎓 Konteks Akademik

Proyek ini dibuat sebagai pemenuhan tugas mata kuliah:

**Teori Bahasa dan Otomata**

dengan fokus pada:

* Perumusan aturan **CFG**
* Analisis sintaks runut
* Representasi *parse tree*
* Penentuan validitas kalimat secara formal

---