import time
import sys
import os
GREEN = '\033[38;5;46m' 
BOLD = '\033[1m'
RESET = '\033[0m'
def typing_effect(text, speed=0.1):
    for char in text:
        sys.stdout.write(f"{BOLD}{GREEN}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(speed)
def run_performance():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n")
    lyrics = [
        ("Khod se karu jo batay", 0.1),
        ("Lagay k tum se ho rahi hai Guftagu", 0.12),
        ("Dekho jo ainay ma", 0.1),
        ("Lgay k aks hai tumhara hubahu", 0.15),
        ("Dil mera, mera na raha", 0.18),
        ("Ishq ma howa jo mubtala.....",0.19),
        ("Kaya hai ye dewangi??",0.12),
        ("Ya hai koi Khumar sa??",0.18)
    ]
    for line, speed in lyrics:
        sys.stdout.write("    ") 
        typing_effect(line, speed)
        print("\n") 
        time.sleep(1.2) 
    print("\n")
if __name__ == "__main__":
    run_performance()