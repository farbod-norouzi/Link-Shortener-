from os import system

# Check the requirements

try:
    import pyshorteners
    from colorama import Fore
except ImportError:
   system("pip install os ")
   system("pip install colorama ")
   system("pip install pyshortenerse")
   exit("\n\nRun script Again")

# Start APP

os.system("Cls")
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
