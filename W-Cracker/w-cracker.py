import hashlib
import sys
import os
import time
import argparse


class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


def banner():
    print(f"""{Colors.BLUE}
__          __   _____ _____            _____ _  ________ _____  
\ \        / /  / ____|  __ \     /\   / ____| |/ /  ____|  __ \ 
 \ \  /\  / /__| |    | |__) |   /  \ | |    | ' /| |__  | |__) |
  \ \/  \/ /___| |    |  _  /   / /\ \| |    |  < |  __| |  _  / 
   \  /\  /    | |____| | \ \  / ____ \ |____| . \| |____| | \ \ 
    \/  \/      \_____|_|  \_\/_/    \_\_____|_|\_\______|_|  \_\ 
                                                                 
    Python Hash Cracker Tool | v1.0
    Coded by 0xWandererx0
    {Colors.RESET}""")
   

parser = argparse.ArgumentParser(description="W-Cracker: Hash Kırma Aracı")
parser.add_argument("-s", "--hash", help="Kırılacak Hash Değeri", required=True)
parser.add_argument("-w", "--wordlist", help="Wordlist Dosya Yolu", required=True)
parser.add_argument("-t", "--type", help="Hash Türü(md5, sha1, sha256, sha512)" , required=True)

args = parser.parse_args()

TARGET_HASH = args.hash 
WORDLIST_PATH = args.wordlist
HASH_TYPE = args.type.lower()

desteklenenler = ["md5", "sha1", "sha256", "sha512"]


desteklenenler = ["md5", "sha1", "sha256", "sha512"]


while HASH_TYPE not in desteklenenler:
    print(f"\n{Colors.RED}[!] HATA: '{HASH_TYPE}' geçerli bir tür değil!{Colors.RESET}")
    print(f"{Colors.YELLOW}[*] Desteklenenler: md5, sha1, sha256, sha512{Colors.RESET}")
    
   
    try:
        HASH_TYPE = input(f"{Colors.BLUE}[?] Lütfen hash türünü tekrar yazın (örn: md5): {Colors.RESET}").strip().lower()
    except KeyboardInterrupt:
        print("\n[!] Çıkış yapılıyor...")
        sys.exit()




def encrypt_word(word, algorithm):
    word = word.encode('utf-8')

    if algorithm == "md5":
        return hashlib.md5(word).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(word).hexdigest
    elif algorithm == "sha256":
        return hashlib.sha256(word).hexdigest
    elif algorithm == "sha512":
        return hashlib.sha512(word).hexdigest
    else:
        print(f"{Colors.RED}[!] HATA: Desteklenmeyen algoritma!{Colors.RESET}")
        sys.exit() 

def main():
    banner()

    if not os.path.exists(WORDLIST_PATH):
        print(f"{Colors.RED}[!] Wordlist dosyası bulunamadı!{Colors.RESET}")
        sys.exit()

    print(f"[*] Hedef Hash : {TARGET_HASH}")
    print(f"[*] Algoritma : {HASH_TYPE.upper()}")
    print(f"[*] Wordlist : {WORDLIST_PATH}")
    print("-" * 50)
    print(f"{Colors.YELLOW}[*] Saldırı Başlıyor...{Colors.RESET}\n")

    start_time = time.time()
    counter = 0

    try:
        with open(WORDLIST_PATH, "r", encoding='utf-8', errors="ignore") as file:
            for line in file:
                word = line.strip()
                counter += 1

                hashed_word = encrypt_word(word, HASH_TYPE)


                if counter % 5000 == 0:
                    sys.stdout.write(f"\r[*] Denenen: {counter} kelime...")
                    sys.stdout.flush()

                if hashed_word == TARGET_HASH:
                    end_time = time.time()
                    diff = end_time - start_time

                    print(f"\n\n{Colors.GREEN}" + "="*40)
                    print(f"  ŞİFRE KIRILDI! ")
                    print("="*40 + f"{Colors.RESET}")
                    print(f"{Colors.GREEN}[+] Şifre: {word}{Colors.RESET}")
                    print(f"[*] Geçen Süre: {diff:.2f} saniye")
                    print(f"[*] Toplam Deneme: {counter}")      
                    sys.exit()
            print(f"\n\n{Colors.RED}[-] Üzgünüm, şifre wordlist içinde bulunamadı{Colors.RESET}")
    except KeyboardInterrupt:
        print("\n[!] İşlem iptal edildi.")

if __name__ == "__main__":
    main()