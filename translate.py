import pandas as pd
import re

df = pd.read_excel("bahasa_jawa.xlsx")

regex_kalimat = re.compile(r"^[a-zA-Z\s\-]+$")

while True:
    teks = input("\nMasukkan kalimat: ").strip().lower()

    if not regex_kalimat.fullmatch(teks):
        print("Input tidak valid (hanya huruf, spasi, dan '-')")
        lanjut = input("Lanjut? (y/n): ").lower()
        if lanjut != "y":
            break
        continue

    kata_list = teks.split()
    print("\nINPUT VALID\n")

    S, P, O, K = [], [], [], []

    for kata in kata_list:
        ditemukan = False

        for _, row in df.iterrows():
            ngoko = [k.strip().lower() for k in str(row["Ngoko"]).split("/")]
            krama_madya = [k.strip().lower() for k in str(row["Krama Madya"]).split("/")]
            indo = str(row["Bahasa Indonesia"]).lower()
            fungsi = str(row["Fungsi (SPOK)"])

            if (
                kata in ngoko
                or kata in krama_madya
                or kata == indo
            ):
                ditemukan = True

                if "S" in fungsi:
                    S.append(kata)
                if "P" in fungsi:
                    P.append(kata)
                if "O" in fungsi:
                    O.append(kata)
                if "K" in fungsi:
                    K.append(kata)

                print(f"  Kata    : {kata}")
                print(f"  Ngoko   : {', '.join(ngoko)}")
                print(f"  Krama   : {', '.join(krama_madya)}")
                print(f"  Arti    : {indo}")
                print(f"  Fungsi  : {fungsi}")
                print()
                break

        if not ditemukan:
            print(f"Kata '{kata}' tidak ada di dataset\n")

    print("=== HASIL ANALISIS SPOK ===")
    print("Subjek     :", " ".join(S))
    print("Predikat   :", " ".join(P))
    print("Objek      :", " ".join(O))
    print("Keterangan :", " ".join(K))

    print("\n=== HASIL VALIDASI KALIMAT ===")

    if not S:
        print("Kalimat TIDAK VALID: tidak ada Subjek (S)")
    elif not P:
        print("Kalimat TIDAK VALID: tidak ada Predikat (P)")
    else:
        posisi_S = min(kata_list.index(k) for k in S)
        posisi_P = min(kata_list.index(k) for k in P)

        if posisi_S < posisi_P:
            print("Kalimat VALID (struktur SPOK benar)")
        else:
            print("Kalimat TIDAK VALID: urutan SPOK salah")

    lanjut = input("\nLanjut? (y/n): ").lower()
    if lanjut != "y":
        print("Program selesai.")
        break
