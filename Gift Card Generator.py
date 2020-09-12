import random
from random import randint
import time
import os
import colorama
from colorama import Fore, init, Style, Back

gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
os.system("title [GiftCardGen] By Cihan820#0001")

os.system('cls')
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                       Gift Card Generator By Cihan820")
#print("Visit My Website: https://sites.google.com/view/cihan820/")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[0] "+Fore.RED+"Credits")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[1] "+Fore.YELLOW+"Amazon")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[2] "+Fore.YELLOW+"Roblox")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[3] "+Fore.YELLOW+"Webkinz")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[4] "+Fore.YELLOW+"Fortnite")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[5] "+Fore.YELLOW+"IMVU")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[6] "+Fore.YELLOW+"Ebay")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[7] "+Fore.YELLOW+"Netflix")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[8] "+Fore.YELLOW+"iTunes")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[9] "+Fore.YELLOW+"Paypal")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[10] "+Fore.YELLOW+"Visa")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[11] "+Fore.YELLOW+"PokemonTGC")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[12] "+Fore.YELLOW+"Playstation")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[13] "+Fore.YELLOW+"Steam")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[14] "+Fore.YELLOW+"Xbox")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[15] "+Fore.YELLOW+"PlayStore")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[16] "+Fore.YELLOW+"Minecraft")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")

mode = input("\nSelect The Type Of Gift Card That You Want To Generate: ")

#Credits
if(mode == "0"):
    os.system("cls")
    print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
    print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[+] "+Fore.RED+"Author: Cihan820")
    print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[+] "+Fore.RED+"Github: https://github.com/Cihan820")
    print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[+] "+Fore.RED+"Discord: https://discord.gg/fH5dPpm")
    print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[+] "+Fore.RED+"Credits: Matty#8952")
    print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[+] "+Fore.RED+"Credits: https://github.com/MattyTM")
    print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"[+] "+Fore.RED+"Credits")
    print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
    input(Style.BRIGHT + Fore.RED + Back.BLACK +"\nEnter to exit.")
#Minecraft
if(mode == "1"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
          out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+newline)
#Amazon
if(mode == "2"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+newline)
#iTunes
if(mode == "3"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        generate16 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+generate11+generate12+generate13+generate14+generate15+generate16+newline)

#Paypal
if(mode == "4"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+newline)
#Playstation
if(mode == "5"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+newline)

#Steam
if(mode == "6"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+space1+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+generate15+newline)

#Visa
if(mode == "7"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    types = input("Card Or Prepaid Code? ")
    if(types == "Prepaid Code"):
        gentype = '0123456789'
        for x in range(number):
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            generate4 = random.choice(gentype)
            generate5 = random.choice(gentype)
            generate6 = random.choice(gentype)
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)
            generate11 = random.choice(gentype)
            generate12 = random.choice(gentype)
            generate13 = random.choice(gentype)
            generate14 = random.choice(gentype)
            generate15 = random.choice(gentype)
            generate16 = random.choice(gentype)
            newline = "\n"
            space = " "
            gen1 = random.choice(gentype)
            gen2 = random.choice(gentype)
            gen3 = random.choice(gentype)
            gen4 = random.choice(gentype)
            gen5 = random.choice(gentype)
            gen6 = random.choice(gentype)
        
        
            with open(file, 'a') as out:
                out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+generate11+generate12+generate13+generate14+generate15+generate16+newline)
            with open(file2, 'a') as out2:
                out2.write(gen1+gen2+gen3+gen4+gen5+gen6+newline)
    elif(types == "Card"):
        gentype = '0123456789'
        for x in range(number):
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            generate4 = random.choice(gentype)
            generate5 = random.choice(gentype)
            space1 = "-"
            generate6 = random.choice(gentype)
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)
            space2 = "-"
            generate11 = random.choice(gentype)
            generate12 = random.choice(gentype)
            generate13 = random.choice(gentype)
            generate14 = random.choice(gentype)
            generate15 = random.choice(gentype)
            space3 = "-"
            generate16 = random.choice(gentype)
            generate17 = random.choice(gentype)
            generate18 = random.choice(gentype)
            generate19 = random.choice(gentype)
            generate20 = random.choice(gentype)
            space4 = "-"
            generate21 = random.choice(gentype)
            generate22 = random.choice(gentype)
            generate23 = random.choice(gentype)
            generate24 = random.choice(gentype)
            generate25 = random.choice(gentype)
            newline = "\n"
            space = ":"
            month = str(randint(0, 12))
            year = str(randint(19,25))
            slash = "/"
            space5 = " "
            generate26 = random.choice(gentype)
            generate27 = random.choice(gentype)
            generate28 = random.choice(gentype)
            with open(file, 'a') as out:
                out.write(generate1+generate2+generate3+generate4+generate5+space1+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+generate15+space3+generate16+generate17+generate18+generate19+generate20+space4+generate21+generate22+generate23+generate24+generate25+space+month+slash+year+space5+generate26+generate27+generate27+newline)
    
#Xbox
if(mode == "8"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    gentype = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        space1 = "-"
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        space3 = "-"
        generate16 = random.choice(gentype)
        generate17 = random.choice(gentype)
        generate18 = random.choice(gentype)
        generate19 = random.choice(gentype)
        generate20 = random.choice(gentype)
        space4 = "-"
        generate21 = random.choice(gentype)
        generate22 = random.choice(gentype)
        generate23 = random.choice(gentype)
        generate24 = random.choice(gentype)
        generate25 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+space1+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+generate15+space3+generate16+generate17+generate18+generate19+generate20+space4+generate21+generate22+generate23+generate24+generate25+newline)
#PlayStore
if(mode == "9"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    gentype = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        space3 = "-"
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        generate16 = random.choice(gentype)
        space4 = "-"
        generate17 = random.choice(gentype)
        generate18 = random.choice(gentype)
        generate19 = random.choice(gentype)
        generate20 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+space3+generate13+generate14+generate15+generate16+space4+generate17+generate18+generate19+generate20+newline)
#PokemonTGC
if (mode == "10"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    gentype = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        space1 = "-"
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        space2 = "-"
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space3 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+space1+generate4+generate5+generate6+generate7+space2+generate8+generate9+generate10+space3+generate11+generate12+generate13+newline)
#Netflix
if(mode == "11"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+newline)
#Ebay
if(mode == "12"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+newline)
#Fortnite
if(mode == "13"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        space1 = "-"
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        space2 = "-"
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+space1+generate6+generate7+generate8+generate9+space2+generate10+generate11+generate12+generate13+newline)
#Roblox
if(mode == "14"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    gentype = '0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        space1 = "-"
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        space2 = "-"
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)

        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+space1+generate4+generate5+space1+generate6+space2+generate7+generate8+generate9+space2+generate10+newline)
#Webkinz
if(mode == "15"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+newline)
#IMVU
if(mode == "16"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Gift Cards Generated.txt")
    file2 = 'GiftCardsCodes.txt'
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+newline)
print ("Thanks For Generating!! Remember That These Gift Cards Are Unchecked.")
time.sleep(3)