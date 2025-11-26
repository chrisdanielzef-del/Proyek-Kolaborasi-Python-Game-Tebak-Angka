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

def hitung_skor(level, attempts_terpakai):
   
    max_attempts = level["attempts"]
    base = 100
    bonus_level = {"Mudah": 1.0, "Sedang": 1.25, "Sulit": 1.5}[level["nama"]]
    efisiensi = max(0, (max_attempts - attempts_terpakai + 1))
    return int(base * bonus_level * efisiensi)

