import time
import colorama
from colorama import Fore
import random
import string
crypto = str(input('Choose between ETH and BTC >>'))

print(f"{Fore.BLUE}$$\      $$\ $$$$$$\ $$\   $$\ $$$$$$$$\ $$$$$$$\  ")
time.sleep(0.2)
print("$$$\    $$$ |\_$$  _|$$$\  $$ |$$  _____|$$  __$$\ ")
time.sleep(0.2)
print("$$$$\  $$$$ |  $$ |  $$$$\ $$ |$$ |      $$ |  $$ |")
time.sleep(0.2)
print("$$\$$\$$ $$ |  $$ |  $$ $$\$$ |$$$$$\    $$$$$$$  |")
time.sleep(0.2)
print("$$ \$$$  $$ |  $$ |  $$ \$$$$ |$$  __|   $$  __$$<")
time.sleep(0.2)
print("$$ |\$  /$$ |  $$ |  $$ |\$$$ |$$ |      $$ |  $$ |")
time.sleep(0.2)
print("$$ | \_/ $$ |$$$$$$\ $$ | \$$ |$$$$$$$$\ $$ |  $$ |")
time.sleep(0.2)
print(" \__|     \__|\______|\__|  \__|\________|\__|  \__|")
time.sleep(0.2)
if crypto == 'ETH' or crypto == 'BTC':
    print("Okey, Wallets are being prepared...")
    time.sleep(3)

    if crypto =='ETH':
        adress = str(input("Please enter your Etherum adress >>"))
        time.sleep(3)
        print("Check succesfully!")
        time.sleep(1)

    elif crypto == 'BTC':
        adress = str(input("Please enter your Bitcoin adress >>"))
        print("Check if Wallet exist...")
        time.sleep(3)
        print("Check succesfully!")
        time.sleep(1)

    class bcorols:
        won = '\033[92m'
        fail = '033[91m'

    def id_gen(size = 40, chars = string.ascii_uppercase + string.digits):
        return "".join(random.choice(chars) for _ in range(size))

    tries = 0

    colorama.init()
    if crypto == 'ETH':
            while(True):
                if(tries > random.randint(10000, 10000)):
                    print(Fore.GREEN + "[-] 0x" + id_gen() + " | Valid | " + "0.0124 ETH")
                    print("Transfer 0.0124 ETH to", adress)
                    time.sleep(6)
                    tries = 0
                    print("Done! Miner is running again")
                    time.sleep(3)
                else:
                    print(Fore.RED + "[-] 0x" + id_gen() + "| Invalid | " + "0.0000 ETH")
                    tries += 1
    colorama.init()
    if crypto == 'BTC':
            while(True):
                if(tries > random.randint(10000, 10000)):
                    print(Fore.GREEN + "[+] bc1" + id_gen() + " | Valid | " + "0.0124 BTC")
                    print("Transfer 0.0124 ETH to", adress)
                    time.sleep(6)
                    tries = 0
                    print("Done! Miner is running again")
                    time.sleep(3)
                else:
                    print(Fore.RED + "[-] 0x" + id_gen() + "| Invalid | " + "0.0000 BTC")
                    tries += 1

else:
    print("Invalid currency. Please choose 'ETH" and 'ETH')

