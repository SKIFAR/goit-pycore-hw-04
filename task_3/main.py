import sys
from pathlib import Path
from colorama import Fore

def print_directory_structure(directory: Path, tabulation: str = "\t"):
    for item in directory.iterdir():
        if item.is_dir():
            print(f"{tabulation}{Fore.BLUE}{item.name}/{Fore.RESET}")
            print_directory_structure(item, tabulation + "\t")
        else:
            print(f"{tabulation}{Fore.GREEN}{item.name}{Fore.RESET}")

if len(sys.argv) < 2:
    print(f"{Fore.RED}Помилка: Ви не вказали шлях до директорії.{Fore.RESET}")
    print("Використання: python script.py <шлях_до_директорії>")

else:
    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED}Помилка: Вказаний шлях не існує.{Fore.RESET}")

    elif not dir_path.is_dir():
        print(f"{Fore.RED}Помилка: Це не директорія.{Fore.RESET}")

    else:
        print(f"{Fore.BLUE}{dir_path.name}/{Fore.RESET}")
        print_directory_structure(dir_path)