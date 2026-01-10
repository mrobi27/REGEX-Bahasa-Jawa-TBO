import re

# =====================================================
# 1. LEKSIKON
# =====================================================

NOUN = {
    "buku", "kalung", "koran", "kursi",
    "kamar", "hotel", "asrama",
    "perpustakaan", "surabaya",
    "anake", "bapak", "adhine", "ibu"
}

PRONOUN = {
    "aku", "kula", "kowe", "sampeyan",
    "panjenengan", "dheweke"
}

PROPER_NOUN = set()

VERB = {
    "sinau", "maca", "turu", "maringi",
    "nyilih", "mangan", "ngombe", "tindak",
    "arep", "manggon"
}

ADVERB = {"lagi", "wis", "durung", "isih"}

PREPOSITION = {"neng", "ing", "menyang", "saka", "karo", "dening"}

# =====================================================
# 2. TERMINAL CHECK
# =====================================================

def is_terminal(word):
    return (
        word in NOUN or
        word in PRONOUN or
        word in PROPER_NOUN or
        word in VERB or
        word in ADVERB or
        word in PREPOSITION
    )

# =====================================================
# 3. FRASE
# =====================================================

def parse_np(words, i, tree, prefix=""):
    if i < len(words) and words[i] in PROPER_NOUN:
        tree.append(f"{prefix}└── PropN ({words[i]})")
        return i + 1

    if i < len(words) and words[i] in PRONOUN:
        tree.append(f"{prefix}└── Pron ({words[i]})")
        return i + 1

    if i < len(words) and words[i] in NOUN:
        tree.append(f"{prefix}└── N ({words[i]})")
        return i + 1

    return i


def parse_keterangan(words, i, tree, prefix=""):
    if i < len(words) and words[i] in ADVERB:
        tree.append(f"{prefix}└── Adv ({words[i]})")
        return i + 1

    if i < len(words) and words[i] in PREPOSITION:
        tree.append(f"{prefix}├── Prep ({words[i]})")
        i += 1
        if i < len(words):
            tree.append(f"{prefix}└── N ({words[i]})")
            return i + 1

    return i

# =====================================================
# 4. KALIMAT (CFG FINAL)
# =====================================================

def parse_sentence(words):
    n = len(words)
    tree = ["S"]

    # Imperatif
    if words[0] in VERB and n == 1:
        tree.append("└── VP")
        tree.append(f"    └── V ({words[0]})")
        return True, "\n".join(tree)

    i = 0
    tree.append("├── NP")
    ni = parse_np(words, i, tree, "│   ")
    if ni == i:
        return False, "❌ NP tidak valid"

    if ni < n and words[ni] in ADVERB:
        tree.append("├── AdvP")
        tree.append(f"│   └── Adv ({words[ni]})")
        ni += 1

    tree.append("└── VP")

    # === VERBA PERTAMA ===
    if ni < n and words[ni] in VERB:
        tree.append(f"    ├── V ({words[ni]})")
        ni += 1

        # === VERBA KEDUA (PREDIKAT KOMPLEKS) ===
        if ni < n and words[ni] in VERB:
            tree.append(f"    ├── V ({words[ni]})")
            ni += 1

        # Objek pertama
        oi1 = parse_np(words, ni, tree, "    │   ")
        if oi1 != ni:
            ni = oi1

            # Objek kedua / Pelengkap
            oi2 = parse_np(words, ni, tree, "    │   ")
            if oi2 != ni:
                ni = oi2

        # Keterangan
        ni = parse_keterangan(words, ni, tree, "    ")

    if ni == n:
        return True, "\n".join(tree)

    return False, "❌ Struktur tidak sesuai CFG"

# =====================================================
# 5. APLIKASI
# =====================================================

while True:
    kalimat = input("\nMasukkan kalimat Bahasa Jawa: ").strip()
    words_raw = kalimat.split()
    words = [w.lower() for w in words_raw]

    for w in words_raw:
        if w[0].isupper():
            PROPER_NOUN.add(w.lower())

    unknown = [w for w in words if not is_terminal(w)]
    if unknown:
        print("\n❌ Kata tidak dikenal:")
        for w in unknown:
            print(" -", w)
        if input("\nLanjut? (y/n): ").lower() != "y":
            break
        continue

    valid, result = parse_sentence(words)

    print("\n=== HASIL ANALISIS SINTAKS ===")
    if valid:
        print("VALID ✅\n")
        print(result)
    else:
        print("TIDAK VALID ❌")
        print(result)

    if input("\nLanjut? (y/n): ").lower() != "y":
        break
