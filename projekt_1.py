"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Adéla Černíková
email: adela.cernikova@seznam.cz
discord: adelacernikova_89606
"""


import source
oddelovac = "-" * 40

registrovani = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"  
}


# ********* uzivatel si vybere cislo text, kzery bude analyzovat
def vyber_text(cislo):
    if cislo.isdigit():
        if int(cislo) in (1,2,3):
           # print(source.TEXTS[int(cislo)-1])
            text_statistiky(source.TEXTS[int(cislo)-1])
        else:
            print("Zadanemu cislu neodpovida zadny text")
    else:
        print("Zadana hodnota neni cislo")

# ********* napocitani statistik pro text
def text_statistiky(TEXT):
    delky_slov = []
    pocet_slov = 0
    pocet_slov_title = 0
    pocet_slov_velkymi = 0
    pocet_slov_malymi = 0
    pocet_slov_cisla = 0
    soucet = 0
    for slovo in TEXT.split():
        # slova ocistim o interpunkci a mezery
        ciste_slovo = slovo.strip(",.:;'")
        # delka slova
        delky_slov.append(len(ciste_slovo))
        # pocet slov
        pocet_slov += 1
        # počet slov začínajících velkým písmenem
        if ciste_slovo.istitle():
            pocet_slov_title +=1
        # počet slov psaných velkými písmeny,
        if ciste_slovo.isupper():
            pocet_slov_velkymi +=1
        # počet slov psaných malými písmeny,
        if ciste_slovo.islower():
            pocet_slov_malymi +=1
        # počet čísel (ne cifer),
        if ciste_slovo.isnumeric():
            pocet_slov_cisla +=1
            # sumu všech čísel (ne cifer) v textu.
            soucet += int(ciste_slovo) 
    
    print("There are ", pocet_slov, "words in the selected text.")
    print("There are ", pocet_slov_title,"titlecase words.")
    print("There are ", pocet_slov_velkymi,"uppercase words.")
    print("There are ", pocet_slov_malymi,"lowercase words.")
    print("There are ", pocet_slov_cisla,"numeric strings.")
    print("The sum of all the numbers ", soucet)
    print(oddelovac)

    # pocty jednotlivych slov podle jejich delky
    print("LEN |  OCCURENCES            |  NR.")
    print(oddelovac)
    unikatni_delky_slov = set(delky_slov)
    for delka in unikatni_delky_slov:
        pocet_delky = delky_slov.count(delka)
        print(str(delka).rjust(3), "| ", "*" * pocet_delky, " " * (20-pocet_delky) ,"| ", pocet_delky)


# ********* prihlaseni do aplikace
def prihlaseni(prihlasovaci_jmeno, heslo):
    if prihlasovaci_jmeno in registrovani.keys():
        if registrovani.get(prihlasovaci_jmeno) == heslo:
            print(oddelovac)
            print("Welcome to the app,", prihlasovaci_jmeno)
            print("We have 3 texts to be analyzed.")
            print(oddelovac)
            cislo_textu = input("Enter a number btw. 1 and 3 to select: ")
            print(oddelovac)
            vyber_text(cislo_textu)
        else:
            print("wrong password")
    else:
        print("unregistered user, terminating the program.")




# ********* spousteni
print("$ python projekt1.py")

username = input("username: ")
password = input("password: ")

prihlaseni(username, password)





