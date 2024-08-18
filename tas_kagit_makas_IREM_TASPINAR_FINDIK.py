import random

# Renkli metinler için ANSI kodları
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Taş, Kağıt ve Makas için ASCII sanatları
art = {
    "taş": """
 _______
|       |
| TAŞ   |
|_______|
""",
    "kağıt": """
 _______
|       |
|KAĞIT  |
|_______|
""",
    "makas": """
 _______
|       |
|MAKAS  |
|_______|
"""
}

def tas_kagit_makas():
    secenekler = ["taş", "kağıt", "makas"]
    pc_secimi = random.choice(secenekler)
    kullanici_secimi = input(f"{YELLOW}Lütfen bir seçim giriniz (taş, kağıt, makas): {RESET}").strip().lower()

    while kullanici_secimi not in secenekler:
        print(f"{RED}Geçersiz bir seçim yaptınız, lütfen geçerli bir seçim giriniz.{RESET}")
        kullanici_secimi = input(f"{YELLOW}Lütfen bir seçim giriniz (taş, kağıt, makas): {RESET}").strip().lower()

    print(f"\n{GREEN}Bilgisayarın seçimi:{RESET}\n{art[pc_secimi]}")
    print(f"\n{YELLOW}Senin seçimin:{RESET}\n{art[kullanici_secimi]}")

    if (kullanici_secimi == "kağıt" and pc_secimi == "taş") or \
       (kullanici_secimi == "taş" and pc_secimi == "makas") or \
       (kullanici_secimi == "makas" and pc_secimi == "kağıt"):
        return 3, 0  # Kazanma
    elif kullanici_secimi == pc_secimi:
        return 1, 1  # Beraberlik
    else:
        return 0, 3  # Kaybetme

def continue_game_decision():
    return random.choice(['evet', 'hayır'])

def play_game():
    kullanici_puan = 0
    pc_puan = 0
    game_round = 1
    first_two_rounds_won = False

    while True:
        print(f"\n{YELLOW}--- Tur {game_round} ---{RESET}")
        if game_round == 1 or game_round == 2:
            print(f"{YELLOW}İlk iki turda kazanırsan 20 puan kazanacaksın!{RESET}")
        else:
            print(f"{YELLOW}Puan kazanmak için oynuyorsun.{RESET}")

        kullanici_tur_puan, pc_tur_puan = tas_kagit_makas()
        kullanici_puan += kullanici_tur_puan
        pc_puan += pc_tur_puan

        if game_round <= 2 and kullanici_tur_puan == 3:
            first_two_rounds_won = True

        if game_round > 2 and first_two_rounds_won:
            kullanici_puan += 20
            print(f"{GREEN}İlk iki turu kazandınız, 20 puan kazandınız!{RESET}")
            first_two_rounds_won = False

        print(f"\n{YELLOW}Mevcut Puanlar - Oyuncu: {kullanici_puan}, Bilgisayar: {pc_puan}{RESET}")

        # Kullanıcıdan oyuna devam edip etmeyeceğini sor
        continue_game_user = input(f"{YELLOW}Oyuna devam etmek ister misiniz? (evet/hayır): {RESET}").strip().lower()
        if continue_game_user == 'hayır':
            print(f"{GREEN}Oyunu bitiriyorsun. Sonuç: Oyuncu Puan: {kullanici_puan}, Bilgisayar Puan: {pc_puan}{RESET}")
            break

        # Bilgisayara devam edip etmeyeceğini sor
        continue_game_pc = continue_game_decision()
        if continue_game_pc == 'hayır':
            print(f"{GREEN}Bilgisayar oyunu bitiriyor. Sonuç: Oyuncu Puan: {kullanici_puan}, Bilgisayar Puan: {pc_puan}{RESET}")
            break

        game_round += 1

play_game()