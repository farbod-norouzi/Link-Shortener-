import os
from os import system
import pyshorteners
from colorama import Fore
import platform 

# Start APP
def clear():
   result = platform.uname()[0]
   if result == "Windows":
      system("cls")
   elif result == "Linux":
      system("clear")
clear()

print(Fore.RED + """ /$$       /$$           /$$              /$$$$$$  /$$                             /$$                                            
| $$      |__/          | $$             /$$__  $$| $$                            | $$                                            
| $$       /$$ /$$$$$$$ | $$   /$$      | $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
| $$      | $$| $$__  $$| $$  /$$/      |  $$$$$$ | $$__  $$ /$$__  $$ /$$__  $$|_  $$_/   /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$      | $$| $$  \ $$| $$$$$$/        \____  $$| $$  \ $$| $$  \ $$| $$  \__/  | $$    | $$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/
| $$      | $$| $$  | $$| $$_  $$        /$$  \ $$| $$  | $$| $$  | $$| $$        | $$ /$$| $$_____/| $$  | $$| $$_____/| $$      
| $$$$$$$$| $$| $$  | $$| $$ \  $$      |  $$$$$$/| $$  | $$|  $$$$$$/| $$        |  $$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$      
|________/|__/|__/  |__/|__/  \__/       \______/ |__/  |__/ \______/ |__/         \___/   \_______/|__/  |__/ \_______/|__/      
                                                                                                                                  
                                                                                                                                  
                                                                                                                                  """)
def short(url):
    link = pyshorteners.Shortener()
    return link.chilpit.short(url)
    

url = input(Fore.GREEN+ "send Your URL  : ")
print(Fore.WHITE+ f"Your short Url : {short(url)}")