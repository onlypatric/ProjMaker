import os,sys
from colorama import *;

class MainApp:
    def __init__(self) -> None:
        init(True);
        self.message=f"""{Fore.RED}ProjMaker 1.0 {Fore.RESET}- {Fore.CYAN}Generatore di progetti
{Fore.RESET} 1 {Fore.GREEN} C e C++
{Fore.RESET} 2 {Fore.GREEN} Java
{Fore.RESET} 3 {Fore.GREEN} Python
{Fore.RESET} 4 {Fore.GREEN} HTML
{Fore.YELLOW}Seleziona un numero da 1 a 4 per generare il progetto{Fore.RESET}
-> """
        self.selection=self.getInt(self.message)
    def getInt(self,msg:str,start:int=1,stop:int=4):
        print(msg,end="")
if __name__ == "__main__":
    MainApp()