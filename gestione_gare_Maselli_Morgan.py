import random
#dizionario
global gare
gare={"Rossi Mario": [("Antipasti",(8,7,9),"Junior Chef"),("Primi",(7,8,8),"Junior Chef"),("Secondi",(9,9,8),"Junior Chef"),("Dessert",(8,8,9),"Junior Chef")],
      "Bianchi Luigi": [("Antipasti",(7,7,8),"Senior Chef"),("Primi",(8,9,7),"Senior Chef"),("Secondi",(7,7,8),"Senior Chef"),("Dessert",(9,8,8),"Senior Chef")],
      "Verdi Giulia": [("Antipasti",(9,8,8),"Junior Chef"),("Primi",(8,7,9),"Junior Chef"),("Secondi",(8,8,8),"Junior Chef"),("Dessert",(7,9,8),"Junior Chef")]}

#punto 2
aggiunta={"Maselli Morgan": [("Antipasti",(7,8,8),"Junior Chef"),("Primi",(9,3,9),"Junior Chef"),("Secondi",(9,7,8),"Junior Chef"),("Dessert",(7,9,9),"Junior Chef")]}
gare.update(aggiunta)

#punto 3
def aggiunta_piatto_unico():
    for key in gare.keys():
        if gare[key][0][2]=="Junior chef":
            gare[key].append(("Piatto Unico",(random.randint(1,10),random.randint(1,10),random.randint(1,10)),"Junior chef"))
        else:
            gare[key].append(("Piatto Unico",(random.randint(1,10),random.randint(1,10),random.randint(1,10)),"Senior chef"))
        
aggiunta_piatto_unico()
#punto 4
def stampa_chef(chiave):
    if chiave not in gare.keys():
        print("Concorrente non esistente")
    else:
        print(f"""
                Categoria chef: {gare[chiave][0][2]}
                Cognome Nome: {chiave}
                """)
        for piatto, punteggi, categoria in gare[chiave]:
            print(f"""
                        Piatto: {piatto}
                        Punteggi:
                        Creatività: {punteggi[0]}
                        Gusto: {punteggi[1]}
                        Presentazione: {punteggi[2]}
                    """)
stampa_chef("Masellli Morgan")
#punto 5
def stampa_piatto(piatto):
    piatti=("Antipasti","Primi","Secondi","Dessert","Piatto Unico")
    if piatto not in piatti:
        print("Piatto non esistente")
    else:
        print(f"""
                Categoria Piatto: {piatto}
                """)
        for key in gare.keys():
            for cibo, punteggi, categoria in gare[key]:
                if piatto==cibo:
                    print(f"""
                                Cognome Nome: {key}
                                Categoria Chef: {categoria}
                                Punteggi:
                                Creatività: {punteggi[0]}
                                Gusto: {punteggi[1]}
                                Presentazione: {punteggi[2]}
                            """)
stampa_piatto("Antipasti")
#punto 6
class analisi_punteggi: #Ho creato una classe per riordinare i metodi e riunirli per comunanza
    global piatti
    piatti=("Antipasti","Primi","Secondi","Dessert","Piatto Unico")
    global categorie_chef
    categorie_chef=("Junior Chef","Senior Chef")

    def punteggio_totale_max(gare,tipo_piatto,tipo_chef):
        if(controlla(tipo_piatto,tipo_chef)):
            massimi=[]
            grandi=[]
            for key in gare.keys():
                for cibo, punteggi, categoria in gare[key]:
                    if cibo==tipo_piatto and categoria==tipo_chef:
                        massimi.append(sum(punteggi))
                        grandi.append(key)

            for punteggio in massimi:
                if max(massimi)!=punteggio:
                    grandi.pop(massimi.index(punteggio))
                    massimi.remove(punteggio)
            return (grandi,massimi)
    
    def media_punteggi_totali(gare,tipo_piatto,tipo_chef):
        if(controlla(tipo_piatto,tipo_chef)):
            media=[]
            for key in gare.keys():
                for cibo, punteggi, categoria in gare[key]:
                    if cibo==tipo_piatto and categoria==tipo_chef:
                        media.append(sum(punteggi))
            return sum(media)/len(media)
    
    global controlla    
    def controlla(tipo_piatto,tipo_chef):
        if tipo_piatto not in piatti:
            print("Piatto non presente in elenco")
            return False
        elif tipo_chef not in categorie_chef:
            print("Categoria di chef non esistente")
            return False
        return True

print(f"Junior Chef che hanno ottenuto il punteggio massimo nella categoria primi: {analisi_punteggi.punteggio_totale_max(gare,'Primi','Junior Chef')}")
print(f"Media generale dei primi degli junior chef: {analisi_punteggi.media_punteggi_totali(gare,'Primi','Junior Chef'):.2f}")

#punto 7

def inserisci_dati():
    piatti=("Antipasti","Primi","Secondi","Dessert","Piatto Unico")
    insieme_punteggi=[]
    
    global controllo
    def controllo(parametro):
        if parametro not in range(1,11):
            print(parametro)
            print("Valore invalido")
            return False
        return True

    nome=str(input("Inserisci il nome "))
    cognome=str(input("Inserisci il cognome "))
    nominativo=(cognome,nome)
    categoria=str(input("Inserisci la categoria dello chef "))
    for piatto in piatti:
        while(True):
            creatività=int(input("Inserisci il punteggio per la creatività "))
            if(controllo(creatività)): break
        while(True):
            gusto=int(input("Inserisci il punteggio per il gusto "))
            if(controllo(gusto)): break
        while(True):
            originalità=int(input("Inserisci il punteggio per l'originalità "))
            if(controllo(originalità)): break
        insieme_punteggi.append((creatività,gusto,originalità))
    inserisci_nuovo_chef(gare,nominativo,piatto,insieme_punteggi,categoria)
    
def inserisci_nuovo_chef(gare,nominativo,piatto,risultati,categoria):
    nNominativo=nominativo[0]+" "+nominativo[1]
    aggiunta={nNominativo:[]}
    for i in range(0,5):
        aggiunta[nNominativo].append((piatto,risultati[i],categoria))
    gare.update(aggiunta)

inserisci_dati()
stampa_chef("Tolotta Gioele")

"""
Le funzioni 3 e 4 sono corrette ma non sono state chiamate nel programma originale. Nel punto 7 vengono riscontrati vari errori, tra 
la creazione della chiave incorretta, errori sui parametri del metodo append e i controlli durante degli inserimenti. 
"""