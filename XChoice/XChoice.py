import os
import time
import sys

###########
#colors   #
###########



WHITE = "\033[1;37;40m\n"
YELLOW = "\033[1;33;40m\n"
GREEN  = "\033[1;32;40m\n"
RED = "\033[1;31;40m\n"
BLUE  = "\033[1;34;40m\n"


print("""
                      ..:::::::::..
                  ..:::aad8888888baa:::..
              .::::d:?88888888888?::8b::::.
            .:::d8888:?88888888??a888888b:::.
          .:::d8888888a8888888aa8888888888b:::.
         ::::dP::::::::88888888888::::::::Yb::::
        ::::dP:::::::::Y888888888P:::::::::Yb::::
       ::::d8:::::::::::Y8888888P:::::::::::8b::::
      .::::88::::::::::::Y88888P::::::::::::88::::.
      :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
      :::::::Y88888888888P::|::Y88888888888P:::::::
      ::::::::::::::::888:::|:::888::::::::::::::::
      `:::::::::::::::8888888888888b::::::::::::::'
       :::::::::::::::88888888888888::::::::::::::
        :::::::::::::d88888888888888:::::::::::::
         ::::::::::::88::88::88:::88::::::::::::
          `::::::::::88::88::88:::88::::::::::'
            `::::::::88::88::P::::88::::::::'
              `::::::88::88:::::::88::::::'
                 ``:::::::::::::::::::''
                      ``:::::::::''
[Coded By NorthX] 
""")



def MenuItems():
    menuid = "1)WebScan\n" "2)DOS Tools\n""3)Password Crack\n""4)PayloadGenerator\n""5)Phishing\n""99)Exit\n"
    print(menuid)
    answer = int(input("Enter a choice : "))
    if answer == 1 :
        os.system("figlet WEBKILLER")
        ScanMenu()
    elif answer == 2:
        os.system("figlet D O S ")
        DOSMenu()
    elif answer == 3 :
        os.system("figlet PASSCRACK")
        Passmenu()
    elif answer == 4:
        PayloadGen()
        os.system("figlet PAYLOAD")
    elif answer == 5:
        os.system("figlet PHISH")
        Phish()
    elif answer == 99:
         exit("Byeeeeeee")
    else :
        print(RED +"[!] Enter a vailed optiom")


###########################################################################
###########################################################################
###########################################################################

def ScanMenu():
    portmenu = """
    
1) Nmap
2)Unicorn 
3)Striker
4)Th3inspector
99)Return to main menu         """
    print(portmenu)
    portanswer = int(input("Enter a choice ; "))
    if portanswer == 1 :
       os.system("git clone https://github.com/nmap/nmap.git ")
    elif portanswer == 2 :
       os.system("git clone https://github.com/IFGHou/Unicornscan.git ")
    elif portanswer == 3:
        os.system("git clone https://github.com/s0md3v/Striker.git ")
    elif portanswer == 4:
        os.system("git clone https://github.com/Moham3dRiahi/Th3inspector.git ")
    elif portanswer == 99:
        MenuItems()
    else:
        exit("[!] Enter a vailed option ")

def DOSMenu():
    dostools = """
    
1)Hulk 
2)Xerxes 
3)Slowloris     
4)LOIC (for linux) 
99)Return to main menu      """
    print(dostools)
    dosnswer = int(input("Enter an option : "))
    if dosnswer == 1:
        os.system("git clone https://github.com/darkwarrior3/hulk.git")
    elif dosnswer == 2:
        os.sytem("git clone https://github.com/zanyarjamal/xerxes.git ")
    elif dosnswer == 3:
        os.system("git clone https://github.com/llaera/slowloris.pl.git ")
    elif dosnswer == 4:
        os.system("git clone https://github.com/NewEraCracker/LOIC.git ")
    elif dosnswer == 99:
        MenuItems()
    else:
        exit("[!] Enter a vailed option")


def Passmenu():
    passmenu = """
    
1)Medusa
2)SocialBox 
3)Crunch (WordList generator)     
99)Return to main menu  
     """
    print(passmenu)
    passanswer = int(input("Enter a choice : "))
    if passanswer == 1 :
        os.system("git clone https://github.com/jmk-foofus/medusa.git ")
    elif passanswer == 2:
        os.system("git clone https://github.com/TunisianEagles/SocialBox.git ")
    elif passanswer == 3 :
        os.system("git clone https://github.com/crunchsec/crunch.git")
    elif passanswer == 99:
        MenuItems()
    else :
        exit("[!] Enter a vailed option")


def PayloadGen():
    payloadmenu = """
    
1)TheFatRat
2)Zirikatu
3)ezsploit
99)Return to main menu     
      """
    print(payloadmenu)
    payanswer = int(input("Enter your choice :"))
    if payanswer == 1:
        os.system("git clone https://github.com/Screetsec/TheFatRat.git ")
    elif payanswer == 2:
        os.system("git clone https://github.com/pasahitz/zirikatu.git ")
    elif payanswer== 3:
        os.system("git clone https://github.com/rand0m1ze/ezsploit.git ")
    elif payanswer == 99:
        MenuItems()
    else:
        exit("[!] Enter a vailed option ")


def Phish():
    phishmenu = """
    
1)PhishX (most powerful phishing tool)
2)Phisher=man 
3)shellphish
99)Return to main menu 
     """
    print(phishmenu)
    phishanswer = int(input("Enter an option : "))
    if phishanswer == 1:
        os.system("git clone https://github.com/WeebSec/PhishX.git ")
    elif phishanswer == 2:
        os.system("git clone https://github.com/FDX100/Phisher-man.git ")
    elif phishanswer == 3:
        os.system("git clone https://github.com/thelinuxchoice/shellphish.git ")
    elif phishanswer == 99:
        MenuItems()





MenuItems()
