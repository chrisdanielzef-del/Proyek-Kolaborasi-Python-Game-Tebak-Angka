import random
import sys

def pilih_level():
    print("=== Game Tebak Angka ===")
    print("Pilih level:")
    print("1. Mudah   (1–10, 5 percobaan)")
    print("2. Sedang  (1–50, 7 percobaan)")
    print("3. Sulit   (1–100, 10 percobaan)")
    while True:
        pilihan = input("Masukkan angka level (1/2/3): ").strip()
        if pilihan in {"1", "2", "3"}:
            if pilihan == "1":
                return {"nama": "Mudah", "batas": 10, "attempts": 5}
            elif pilihan == "2":
                return {"nama": "Sedang", "batas": 50, "attempts": 7}
            else:
                return {"nama": "Sulit", "batas": 100, "attempts": 10}
        print("Input tidak valid. Pilih 1, 2, atau 3.")

def minta_tebakan(batas):
    while True:
        jawaban = input(f"Tebak angka (1–{batas}): ").strip()
        if jawaban.isdigit():
            angka = int(jawaban)
            if 1 <= angka <= batas:
                return angka
            else:
                print(f"Angka harus di rentang 1–{batas}.")
        else:
            print("Harus angka. Coba lagi.")

def hitung_skor(level, attempts_terpakai):
    # Skor sederhana: makin sedikit percobaan, makin tinggi
    max_attempts = level["attempts"]
    base = 100
    bonus_level = {"Mudah": 1.0, "Sedang": 1.25, "Sulit": 1.5}[level["nama"]]
    efisiensi = max(0, (max_attempts - attempts_terpakai + 1))
    return int(base * bonus_level * efisiensi)

def main():
    while True:
        level = pilih_level()
        target = random.randint(1, level["batas"])
        attempts_left = level["attempts"]

        print(f"\nLevel {level['nama']} dipilih. Kamu punya {attempts_left} percobaan.")
        # Debug dev hint (matikan saat produksi):
        # print(f"(DEV: target = {target})")

        riwayat = []
        while attempts_left > 0:
            print(f"\nPercobaan tersisa: {attempts_left}")
            tebakan = minta_tebakan(level["batas"])
            riwayat.append(tebakan)

            if tebakan == target:
                skor = hitung_skor(level, attempts_terpakai=(level["attempts"] - attempts_left + 1))
                print(f"\nBenar! Angkanya {target}.")
                print(f"Kamu menebak benar dalam {level['attempts'] - attempts_left + 1} percobaan.")
                print(f"Skor kamu: {skor}")
                break
            elif tebakan < target:
                print("Terlalu kecil.")
            else:
                print("Terlalu besar.")

            attempts_left -= 1

        if attempts_left == 0 and (not riwayat or riwayat[-1] != target):
            print(f"\nKesempatan habis. Angka yang benar: {target}.")
            print("Tetap semangat!")

        # Tampilkan riwayat tebakan
        if riwayat:
            history_str = ", ".join(map(str, riwayat))
            print(f"Riwayat tebakan: [{history_str}]")

        # Main lagi?
        while True:
            lagi = input("\nMain lagi? (y/n): ").strip().lower()
            if lagi in {"y", "n"}:
                break
            print("Jawab dengan 'y' atau 'n'.")
        if lagi == "n":
            print("Terima kasih sudah bermain. Sampai jumpa!")
            sys.exit(0)

if __name__ == "__main__":
    main()
