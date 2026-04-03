import os
import sys
import time
import requests

# --- Global Configurations ---
G = '\033[92m'  # Neon Green
C = '\033[96m'  # Cyan
R = '\033[91m'  # Red
W = '\033[0m'   # White
Y = '\033[93m'  # Yellow
B = '\033[94m'  # Blue

# Your Google Apps Script Web App URL
API_URL = "https://script.google.com/macros/s/AKfycbxEOjSnergzkiCCwEUmJr1ZvEsl06bEfZu5UjvsxK0vIgkbm9Lax8D4SJs2rQO4mHoV/exec"

# --- Emoji Dictionary ---
cipher_map = {
    'a': '🍏', 'b': '🫐', 'c': '🥥', 'd': '🍩', 'e': '🥚', 'f': '🍟', 'g': '🍇', 'h': '🍯', 'i': '🍦', 'j': '🧃', 'k': '🥝', 'l': '🍭', 'm': '🥨', 'n': '🍜', 'o': '🍊', 'p': '🥞', 'q': '🧀', 'r': '🍙', 's': '🍓', 't': '🌮', 'u': '🥪', 'v': '🍕', 'w': '🍉', 'x': '🍬', 'y': '🍿', 'z': '🥗',
    'A': '🦁', 'B': '🐻', 'C': '🐈', 'D': '🐕', 'E': '🐘', 'F': '🦊', 'G': '🦒', 'H': '🐹', 'I': '🦎', 'J': '🐆', 'K': '🐨', 'L': '🐪', 'M': '🐒', 'N': '🦌', 'O': '🦦', 'P': '🐼', 'Q': '🦜', 'R': '🐇', 'S': '🐍', 'T': '🐅', 'U': '🦄', 'V': '🦇', 'W': '🐺', 'X': '🦓', 'Y': '🦖', 'Z': '🦂',
    '0': '🌑', '1': '🕐', '2': '🕑', '3': '🕒', '4': '🕓', '5': '🕔', '6': '🕕', '7': '🕖', '8': '🕗', '9': '🕘',
    ' ': '☁️', '.': '💎', ',': '💠', '!': '🔥', '?': '🌀', '@': '🛡️', '#': '🧱', '$': '💰', '%': '📈', '+': '➕', '-': '➖'
}

reverse_map = {v: k for k, v in cipher_map.items()}
sorted_emojis = sorted(cipher_map.values(), key=len, reverse=True)

def hacker_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    os.system('clear')
    print(f"""{C}
    ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
    ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
    ██║  ███╗███████║██║   ██║███████╗   ██║   
    ██║   ██║██╔══██║██║   ██║╚════██║   ██║   
    ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   
              {G}P R O T O C O L : E N I G M A{W}
    -------------------------------------------
    {R}[+]{W} DEVELOPER : {Y}MD SADID HASAN SAJID [H@CKER__x]{W}
    {R}[+]{W} DATABASE  : {G}CLOUD SECURED{W}
    -------------------------------------------
    """)

# --- Manual Registration Info ---
def registration_info():
    banner()
    print(f"{Y}[*] MANUAL REGISTRATION PROCESS{W}")
    print("-" * 40)
    hacker_print(f"{G}To use this tool, you need a pre-registered account.{W}")
    print(f"\n{C}FOLLOW THESE STEPS:{W}")
    print(f"1. Send an email to: {Y}minustest64@gmail.com{W}")
    print(f"2. Subject: {G}Request for Ghost-Cipher Access{W}")
    print(f"3. Message format: {R}/reg [your_preferred_username]{W}")
    print("-" * 40)
    hacker_print(f"{W}Once your request is processed, the developer will email you")
    hacker_print(f"your official {G}Username{W} and {G}Password{W} shortly.")
    print(f"\n{B}Note: If your username is taken, we will provide the closest alternative.{W}")
    input(f"\n{G}Press Enter to go back...{W}")

# --- Login System ---
def login():
    banner()
    print(f"{Y}[*] SECURE ACCESS LOGIN{W}")
    user = input(f"{C}Username: {W}")
    password = input(f"{C}Password: {W}")
    print(f"{G}[*] Verifying Identity with Cloud...{W}")
    
    try:
        # Action is fixed to login, signup removed from code
        res = requests.get(f"{API_URL}?action=login&user={user}&pass={password}")
        if "Granted" in res.text:
            print(f"{G}[✔] ACCESS GRANTED!{W}")
            time.sleep(1)
            return True
        else:
            print(f"{R}[!] ACCESS DENIED! Invalid Credentials.{W}")
            time.sleep(2)
            return False
    except:
        print(f"{R}[!] Cloud Connection Failed.{W}")
        time.sleep(2)
        return False

# --- Core Logic Functions ---
def encrypt(text):
    return "".join(cipher_map.get(char, char) for char in text)

def decrypt(emoji_text):
    result = ""
    i = 0
    while i < len(emoji_text):
        found = False
        for emoji in sorted_emojis:
            if emoji_text.startswith(emoji, i):
                result += reverse_map[emoji]
                i += len(emoji)
                found = True
                break
        if not found:
            result += emoji_text[i]
            i += 1
    return result

def main_tool():
    while True:
        banner()
        print(f"{C}[1]{W} LOCK MESSAGE")
        print(f"{C}[2]{W} UNLOCK MESSAGE")
        print(f"{C}[3]{W} DISCONNECT SYSTEM")
        
        print(f"\n{G}┌──(ghost㉿enigma)-[~]{W}")
        choice = input(f"{G}└─${W} ")

        if choice == '1':
            msg = input(f"\n{R}[?]{W} Input Text: {C}")
            hacker_print(f"{G}[✔] RESULT: {W}{encrypt(msg)}")
            input(f"\n{B}Press Enter to return...{W}")
        elif choice == '2':
            code = input(f"\n{R}[?]{W} Input Emoji Code: {C}")
            hacker_print(f"{G}[✔] DECODED: {W}{decrypt(code)}")
            input(f"\n{B}Press Enter to return...{W}")
        elif choice == '3':
            hacker_print(f"{R}[!] DISCONNECTING FROM CLOUD...{W}")
            time.sleep(1)
            break

# --- Gateway Section ---
if __name__ == "__main__":
    while True:
        banner()
        print(f"{G}[1]{W} LOGIN")
        print(f"{G}[2]{W} HOW TO REGISTER? (Get Access)")
        print(f"{G}[3]{W} EXIT")
        
        cmd = input(f"\n{C}Select Option: {W}")
        
        if cmd == '1':
            if login():
                main_tool()
        elif cmd == '2':
            registration_info()
        elif cmd == '3':
            hacker_print(f"{R}[!] SHUTTING DOWN...{W}")
            sys.exit()