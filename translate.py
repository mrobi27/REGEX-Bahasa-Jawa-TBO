import pandas as pd

# =====================================================
# LOAD DATASET (LEXICON / TERMINAL SYMBOLS)
# =====================================================
df = pd.read_excel("bahasa_jawa.xlsx")

PRONOUN = set()
VERB = set()
NOUN = set()
ADVERB = set()

# Determiner (boleh ditambah manual, aman secara CFG)
DETERMINER = {"iki", "iku"}

# =====================================================
# BUILD LEXICON DARI DATASET
# =====================================================
for _, row in df.iterrows():
    fungsi = str(row["Fungsi (SPOK)"]).upper()

    kata_set = set()
    kata_set.update(str(row["Ngoko"]).lower().split("/"))
    kata_set.update(str(row["Krama Madya"]).lower().split("/"))
    kata_set.add(str(row["Bahasa Indonesia"]).lower())

    if "S" in fungsi:
        PRONOUN.update(kata_set)
    if "P" in fungsi:
        VERB.update(kata_set)
    if "O" in fungsi:
        NOUN.update(kata_set)
    if "K" in fungsi:
        ADVERB.update(kata_set)

# =====================================================
# CONTEXT FREE GRAMMAR (CFG)
#
# S   → NP VP
# NP  → Pronoun | Noun | Det Noun
# VP  → Verb
# VP  → Verb NP
# VP  → Verb Adv
# VP  → Verb NP Adv
# =====================================================

def parse_sentence(words):
    tree = []
    index = 0
    n = len(words)

    # ===== START SYMBOL =====
    tree.append("S")
    tree.append("├── NP")

    # ===== NP =====
    if index < n and words[index] in DETERMINER:
        tree.append(f"│   ├── Det ({words[index]})")
        index += 1
        if index < n and words[index] in NOUN:
            tree.append(f"│   └── Noun ({words[index]})")
            index += 1
        else:
            return False, "❌ NP tidak lengkap (Det tanpa Noun)"

    elif index < n and words[index] in PRONOUN:
        tree.append(f"│   └── Pronoun ({words[index]})")
        index += 1

    elif index < n and words[index] in NOUN:
        tree.append(f"│   └── Noun ({words[index]})")
        index += 1

    else:
        return False, "❌ NP (Subjek) tidak ditemukan"

    # ===== VP =====
    tree.append("└── VP")

    if index < n and words[index] in VERB:
        tree.append(f"    ├── Verb ({words[index]})")
        index += 1
    else:
        return False, "❌ Verb (Predikat) tidak ditemukan"

    # ===== OPTIONAL NP (OBJ) =====
    if index < n and words[index] in NOUN:
        tree.append("    ├── NP")
        tree.append(f"    │   └── Noun ({words[index]})")
        index += 1

    # ===== OPTIONAL ADV =====
    if index < n and words[index] in ADVERB:
        tree.append(f"    └── Adv ({words[index]})")
        index += 1

    # ===== FINAL CHECK =====
    if index != n:
        return False, "❌ Struktur tidak sesuai CFG"

    return True, "\n".join(tree)

# =====================================================
# MAIN PROGRAM
# =====================================================
while True:
    kalimat = input("\nMasukkan kalimat Bahasa Jawa: ").lower().strip()
    words = kalimat.split()

    valid, result = parse_sentence(words)

    print("\n=== HASIL ANALISIS SINTAKS ===")
    if valid:
        print("Kalimat VALID berdasarkan Context Free Grammar (CFG)\n")
        print("Parse Tree:")
        print(result)
    else:
        print("Kalimat TIDAK VALID")
        print(result)

    lanjut = input("\nLanjut? (y/n): ").lower()
    if lanjut != "y":
        print("Program selesai.")
        break
