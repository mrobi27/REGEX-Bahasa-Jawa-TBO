import pandas as pd 

# =====================================================
# LOAD DATASET
# =====================================================
df = pd.read_excel("bahasa_jawa.xlsx")

PRONOUN = set()
VERB = set()
NOUN = set()
ADVERB = set()

DETERMINER = {"iki", "iku"}

# =====================================================
# SAFE SPLIT
# =====================================================
def split_safe(value):
    if pd.isna(value):
        return []
    value = str(value).lower()
    value = value.replace(",", "/")
    return [k.strip() for k in value.split("/") if k.strip()]

# =====================================================
# BUILD LEXICON
# =====================================================
for _, row in df.iterrows():
    fungsi = str(row["Fungsi (SPOK)"]).upper()

    kata_set = set()
    kata_set.update(split_safe(row["Ngoko"]))
    kata_set.update(split_safe(row["Krama Madya"]))
    kata_set.update(split_safe(row["Krama Inggil"]))
    kata_set.update(split_safe(row["Bahasa Indonesia"]))

    if "S" in fungsi:
        PRONOUN.update(kata_set)
    if "P" in fungsi:
        VERB.update(kata_set)
    if "O" in fungsi:
        NOUN.update(kata_set)
    if "K" in fungsi:
        ADVERB.update(kata_set)

ALL_TERMINALS = PRONOUN | VERB | NOUN | ADVERB | DETERMINER

# =====================================================
# CONTEXT FREE GRAMMAR PARSER
# CFG:
# S  -> NP VP
# NP -> Pronoun | Noun | Det Noun
# VP -> Verb | Verb NP | Verb Adv | Verb NP Adv
# =====================================================
def parse_sentence(words):
    tree = []
    index = 0
    n = len(words)

    tree.append("S")
    tree.append("├── NP")

    # ===== NP (SUBJEK) =====
    if index < n and words[index] in DETERMINER:
        tree.append(f"│   ├── Det ({words[index]})")
        index += 1
        if index < n and words[index] in NOUN:
            tree.append(f"│   └── Noun ({words[index]})")
            index += 1
        else:
            return False, "❌ NP tidak lengkap: Determiner harus diikuti Noun"

    elif index < n and words[index] in PRONOUN:
        tree.append(f"│   └── Pronoun ({words[index]})")
        index += 1

    elif index < n and words[index] in NOUN:
        tree.append(f"│   └── Noun ({words[index]})")
        index += 1

    else:
        return False, "❌ Kalimat tidak memiliki Subjek (NP)"
    
    # ===== KALIMAT NOMINAL (S → NP) =====
    if index == n:
        return True, "\n".join(tree)

    # ===== VP =====
    tree.append("└── VP")

    if index < n and words[index] in VERB:
        tree.append(f"    └── Verb ({words[index]})")
        index += 1
    else:
        return False, "❌ Kalimat tidak memiliki Predikat (Verb)"

    # ===== VERB + NP (OBJEK) =====
    if index < n and words[index] in NOUN:
        tree[-1] = f"    ├── Verb ({tree[-1].split('(')[1].rstrip(')')})"
        tree.append("    ├── NP")
        tree.append(f"    │   └── Noun ({words[index]})")
        index += 1

    # ===== VERB + ADV =====
    if index < n and words[index] in ADVERB:
        tree.append(f"    └── Adv ({words[index]})")
        index += 1

    # ===== FINAL VALIDATION =====
    if index == n:
        return True, "\n".join(tree)

    return False, "❌ Struktur kalimat tidak sesuai CFG"

# =====================================================
# MAIN PROGRAM
# =====================================================
while True:
    kalimat = input("\nMasukkan kalimat Bahasa Jawa: ").lower().strip()
    words = kalimat.split()

    unknown_words = [w for w in words if w not in ALL_TERMINALS]
    if unknown_words:
        print("\n❌ Kata tidak dikenal dalam dataset:")
        for w in unknown_words:
            print(f" - {w}")
        print("Kalimat tidak diproses karena mengandung simbol di luar lexicon.")

        lanjut = input("\nLanjut? (y/n): ").lower()
        if lanjut != "y":
            print("Program selesai.")
            break
        continue

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
