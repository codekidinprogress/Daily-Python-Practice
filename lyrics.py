import time
import sys

BLUE = "\033[94m"
RESET = "\033[0m"

lyrics = [
        "Saahan te zor na chalda",
        "Dekhan te tham jaande ne",
        "Lokaan layi pagal munde",
        "Akhaan di man jaande ne",

        "Raatan nu takkiye taare",
        "Ohna vich tera chehra",
        "Jagdi meri ankh de vich tu",
        "Chann ne hi laya pehra",

        "Saade ton door je sohne",
        "Bin mileya sajjan khone",
        "Supne sab poore hone",
        "Par jeh tu akh milaave",

        "Aadat ban lag gayi dil nu",
        "Badlaan kinj samajh na aave",
        "Us din nu din na giniye",
        "Jis din tu nazar na aave"
]

def animate_text(color, text):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.07)
    print()

for line in lyrics:
    animate_text(BLUE, line)
    time.sleep(0.7)