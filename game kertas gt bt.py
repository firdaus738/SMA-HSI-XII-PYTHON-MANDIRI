import random

# Inisialisasi skor
skor_pemain = 0
skor_komputer = 0

opsi = ["batu", "gunting", "kertas"]

print("🎮 Game Suit Jepang!")
print("Ketik 'exit' untuk keluar dari game.\n")

while True:
    player = input("Pilih batu/gunting/kertas: ").lower()

    if player == "exit":
        print("🎯 Permainan selesai.")
        print(f"Skor Akhir: Kamu {skor_pemain} - Komputer {skor_komputer}")
        break

    if player not in opsi:
        print("❌ Pilihan tidak valid. Coba lagi!\n")
        continue

    komputer = random.choice(opsi)
    print(f"Komputer memilih: {komputer}")

    if player == komputer:
        print("😐 Seri!")
    elif (player == "batu" and komputer == "gunting") or \
         (player == "gunting" and komputer == "kertas") or \
         (player == "kertas" and komputer == "batu"):
        print("🎉 Kamu menang!")
        skor_pemain += 1
    else:
        print("😢 Kamu kalah!")
        skor_komputer += 1

    print(f"Skor: Kamu {skor_pemain} - Komputer {skor_komputer}\n")