import requests
import os
import sys
import argparse 

def banner():
    print("""
    ######################################
    #          PY-DIR-HUNTER             #
    #        CLI Version (Pro)           #
    #       Coded by 0xWandererx0        #
    ######################################
    """)


parser = argparse.ArgumentParser(description="Python Web Directory Buster")
parser.add_argument("-u", "--url", help="Hedef URL (Örn: http://site.com)", required=True)
parser.add_argument("-w", "--wordlist", help="Wordlist Dosya Yolu", required=True)


args = parser.parse_args()


target_url = args.url
wordlist_path = args.wordlist

banner()


if not target_url.endswith("/"):
    target_url += "/"

if not os.path.exists(wordlist_path):
    print(f"\n[!] HATA: '{wordlist_path}' bulunamadı!")
    sys.exit()

with open(wordlist_path, "r") as file:
    wordlist = file.read().splitlines()

print(f"[*] HEDEF: {target_url}")
print(f"[*] KELİME LİSTESİ: {wordlist_path}")
print(f"[*] Toplam Kelime: {len(wordlist)}")
print("-" * 40)


try:
    for word in wordlist:
        full_url = target_url + word
        try:
            response = requests.get(full_url, timeout=3)
            if response.status_code == 200:
                print(f"[+] BULUNDU: {full_url}")
            elif response.status_code == 403:
                print(f"[!] YASAKLI: {full_url}")
        except:
            pass
except KeyboardInterrupt:
    print("\n[!] İşlem kullanıcı tarafından iptal edildi.")
    sys.exit()

print("-" * 40)
print("Tarama Tamamlandı.")
