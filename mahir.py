import os
import sys
from colorama import Fore, init

init(autoreset=True)

def show_logo(username):
    logo = f"""
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
     ███╗   ███╗ █████╗ ███╗   ███╗ █████╗ 
     ████╗ ████║██╔══██╗████╗ ████║██╔══██╗
     ██╔████╔██║███████║██╔████╔██║███████║
     ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██║
     ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██║  ██║
     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
{Fore.MAGENTA}Welcome, {username}!
"""
    print(logo)

def show_menu():
    menu = f"""
{Fore.LIGHTCYAN_EX}1.{Fore.GREEN} Download YouTube Video
{Fore.LIGHTCYAN_EX}2.{Fore.BLUE} Download Facebook Video
{Fore.LIGHTCYAN_EX}3.{Fore.MAGENTA} Download Instagram Video
{Fore.LIGHTCYAN_EX}4.{Fore.YELLOW} Download TikTok Video
{Fore.LIGHTCYAN_EX}5.{Fore.CYAN} Download Others Video
{Fore.LIGHTCYAN_EX}6.{Fore.LIGHTGREEN_EX} Join Telegram Channel
{Fore.LIGHTCYAN_EX}7.{Fore.LIGHTRED_EX} Report A Problem
{Fore.LIGHTCYAN_EX}8.{Fore.RED} Exit Programme
"""
    print(menu)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    username = "MAHIR SHAHED"
    show_logo(username)
    show_menu()

    choice = input(f"{Fore.CYAN}Enter your choice (1-8): {Fore.RESET}")

    if choice == '1':
        print(f"{Fore.GREEN}Downloading YouTube video...")
    elif choice == '2':
        print(f"{Fore.GREEN}Downloading Facebook video...")
    elif choice == '3':
        print(f"{Fore.GREEN}Downloading Instagram video...")
    elif choice == '4':
        print(f"{Fore.GREEN}Downloading TikTok video...")
    elif choice == '5':
        print(f"{Fore.GREEN}Downloading Other video...")
    elif choice == '6':
        print(f"{Fore.CYAN}Joining Telegram Channel...")
    elif choice == '7':
        print(f"{Fore.RED}Reporting a problem...")
    elif choice == '8':
        print(f"{Fore.MAGENTA}Exiting... Goodbye!")
        sys.exit()
    else:
        print(f"{Fore.RED}Invalid choice. Try again.")

if __name__ == '__main__':
    main()
