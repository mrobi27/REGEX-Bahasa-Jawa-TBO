import pandas as pd
import re

df = pd.read_excel("bahasa_jawa.xlsx")

PRONOUN = set()
VERB = set()
NOUN = set()
ADVERB = set()

DETERMINER = {"iki", "iku"}

# =====================================================
# SAFE SPLIT (REGEX VERSION)
# =====================================================
def split_safe(value):
    if pd.isna(value):
        return []
    value = str(value).lower()
    value = re.sub(r"[,\s/]+", "/", value)
    return re.findall(r"[a-z]+", value)

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
# =====================================================
def parse_sentence(words):
    tree = []
    index = 0
    n = len(words)

    tree.append("S")

    # Aturan 3: S → VP (Kalimat Imperatif/Perintah)
    if index < n and words[index] in VERB:
        tree.append("└── VP")
        tree.append(f"    └── Verb ({words[index]})")
        index += 1

        if index < n and words[index] in NOUN:
            tree[-1] = f"    ├── Verb ({tree[-1].split('(')[1].rstrip(')')})"
            tree.append("    ├── NP")
            tree.append(f"    │   └── Noun ({words[index]})")
            index += 1

        if index < n and words[index] in ADVERB:
            tree.append(f"    └── Adv ({words[index]})")
            index += 1

        if index == n:
            return True, "\n".join(tree)
        return False, "❌ Struktur tidak sesuai CFG"

    tree.append("├── NP")

    if index < n and words[index] in DETERMINER:
        tree.append(f"│   ├── Det ({words[index]})")
        index += 1
        if index < n and words[index] in NOUN:
            tree.append(f"│   └── Noun ({words[index]})")
            index += 1
        else:
            return False, "❌ NP tidak lengkap"

    elif index < n and words[index] in PRONOUN:
        tree.append(f"│   └── Pronoun ({words[index]})")
        index += 1

    elif index < n and words[index] in NOUN:
        tree.append(f"│   └── Noun ({words[index]})")
        index += 1

    else:
        return False, "❌ Tidak ada Subjek"

    if index == n:
        return True, "\n".join(tree)

    tree.append("└── VP")

    if index < n and words[index] in VERB:
        tree.append(f"    └── Verb ({words[index]})")
        index += 1
    else:
        return False, "❌ Tidak ada Predikat"

    if index < n and words[index] in NOUN:
        tree[-1] = f"    ├── Verb ({tree[-1].split('(')[1].rstrip(')')})"
        tree.append("    ├── NP")
        tree.append(f"    │   └── Noun ({words[index]})")
        index += 1

    if index < n and words[index] in ADVERB:
        tree.append(f"    └── Adv ({words[index]})")
        index += 1

    if index == n:
        return True, "\n".join(tree)

    return False, "❌ Struktur tidak sesuai CFG"

# =====================================================
# MAIN PROGRAM
# =====================================================
while True:
    kalimat = input("\nMasukkan kalimat Bahasa Jawa: ").lower().strip()

    # REGEX TOKENIZER
    words = re.findall(r"[a-z]+", kalimat)

    unknown_words = [w for w in words if w not in ALL_TERMINALS]
    if unknown_words:
        print("\n❌ Kata tidak dikenal:")
        for w in unknown_words:
            print(f" - {w}")
        lanjut = input("\nLanjut? (y/n): ").lower()
        if lanjut != "y":
            break
        continue

    valid, result = parse_sentence(words)

    print("\n=== HASIL ANALISIS SINTAKS ===")
    if valid:
        print("VALID (CFG)\n")
        print(result)
    else:
        print("TIDAK VALID")
        print(result)

    if input("\nLanjut? (y/n): ").lower() != "y":
        break
