import time
import os

try:
    total_seconds = int(input("Enter the time in seconds: "))

    while total_seconds > 0:
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        os.system("cls" if os.name == "nt" else "clear")

        print("----COUNTDOWN TIMER----")
        print(f"\n{hours:02}:{minutes:02}:{seconds:02}")

        time.sleep(1)
        total_seconds -= 1

    os.system("cls" if os.name == "nt" else "clear")
    print("TIME'S UP!")

except ValueError:
    print("Please enter a valid number!")
except KeyboardInterrupt:
    print("\nTimer stopped by user.")
