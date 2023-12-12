from psutil import cpu_percent, virtual_memory, boot_time
from os import system as S
from time import sleep
from datetime import datetime
from colorama import Fore, Style
import signal

exit_program = False

def Update(t):
    sleep(t)
    try: S("clear")
    except: S("cls")

def format_uptime(uptime):
    total = str(datetime.now() - datetime.fromtimestamp(uptime))
    return total[:7]

def signal_handler(sig, frame):
    global exit_program
    exit_program = True
signal.signal(signal.SIGINT, signal_handler)

def Verify_Resources():
    cpu = cpu_percent(interval=0)
    ram = virtual_memory()
    used_ram = int(ram.used/10**6)
    uptime = boot_time()
    
    print(f"""
        MINIMAL TOP
    ---------------------
      {Fore.GREEN}CPU🖥️ :    {cpu}%{Style.RESET_ALL}       
      {Fore.YELLOW}RAM🧠:    {used_ram} MB{Style.RESET_ALL}
      {Fore.CYAN}UPTIME⏰: {format_uptime(uptime)}{Style.RESET_ALL}  
    ---------------------
    """)

while not exit_program:
    Update(1)
    Verify_Resources()
