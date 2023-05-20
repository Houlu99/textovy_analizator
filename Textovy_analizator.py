"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jiří Strniště
email: jiristrniste@gmail.com
discord: Houlu#8777
"""
#import textu
from task_template import TEXTS

#správní uživatelé
users = {
    "jmeno": "heslo",
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

#zadání přihlašovacích údajů
jmeno = input("Zadej přihlašovací jméno:")
heslo = input("Zadej přihlašovací heslo:") 

#vymazání jmena a hesla pro prihlášení
users.pop("jmeno")

#ověření hesla
password = users.get(jmeno)

if password == heslo:
    print("Vítej", jmeno ,"v aplikaci!")
else:
    print("Jmeno nebo heslo je chybné!")

#výber textu
vyber_textu = input("Vyberte si text pro analyzu (1, 2 nebo 3)")

#ověření výběru textu
spravny_vyber = ["1", "2", "3"]

if vyber_textu.isnumeric():
    
    if vyber_textu == spravny_vyber[0]:
        print("Dobrý výběr!")
    else:
        print("Text je momentálně nedostupný!")
else:
     print("Zadaná hodnota musí být číslo!")

















