# Made by Misspoken
# Give credits lol
# Use randomwordgenerator.com for good usernames without typing them in.
# yw :)

import requests
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

baselink = 'https://replit.com/@'
intro = rf"""

{Fore.LIGHTRED_EX} +--^----------,--------,-----,--------------------^-,
{Fore.YELLOW} | |||||||||   `--------'  Replit Username Checker  O
{Fore.LIGHTRED_EX} `+---------------------------^--------------------|
{Fore.YELLOW}   `\_,---------,---------,------------------------'
{Fore.LIGHTRED_EX}     / XXXXXX /'|       /'
{Fore.YELLOW}    / XXXXXX /  `\    /'
{Fore.LIGHTRED_EX}   / XXXXXX /`-------'
{Fore.YELLOW}  / XXXXXX / By Misspoken
{Fore.LIGHTRED_EX} / XXXXXX /
{Fore.YELLOW}(________(                
{Fore.LIGHTRED_EX} `------'  

{Fore.RESET}"""
print(intro)

def checkname(name):
    sendrequest = requests.get(baselink + name)
    if (sendrequest.status_code == 200): 
        print(f'\033[91m[CHECKER] {name} is not available!')
    elif (sendrequest.status_code == 404):
        print(f'\033[92m[CHECKER] {name} is available!')
    else:
        print(sendrequest.status_code)

def checknamefromlist(file_location):
    try:
        openfile = open(file_location, 'r')
        lines = openfile.readlines()
        for line in lines:
            checkname(line.strip())
            time.sleep(1)
    except:
        print('[ERROR] Something went wrong! Error: 404')

def main():
    running = True
    while (running == True):
        print(f'{Fore.YELLOW}[1]{Fore.RESET} Check Name\n{Fore.YELLOW}[2]{Fore.RESET} Checks From List\n{Fore.YELLOW}[3]{Fore.RESET} Exit')
        choice = input("> ")
        if (choice == '1'):
            name = input("\n[-] Enter Name: ")
            print('\n')
            checkname(name)
            print('\n')
        if (choice == '2'):
            print('\n')
            file_location = input("[-] Enter File Name: ")
            checknamefromlist(file_location)
            print('\n')
        if (choice == '3'):
            running = False

main()
