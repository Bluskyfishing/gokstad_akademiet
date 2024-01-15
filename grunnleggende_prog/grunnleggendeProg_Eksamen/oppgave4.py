import os

FILENAME = "solgtevarer.csv" #Filen som er vedlagt oppgaven heter "solgtevarer (2).csv" Regner med at filen ikke skal ha (2).

try:
    bestillingerListe = []

    with open(FILENAME, "r", encoding="utf-8") as fileRead: #Velger filen med encoding utf-8 for å sikkere at æøå virker.
        #Bruker enumerate slik at jeg får indexen til linjene. Starter å telle på 1 istedenfor 0 for å få riktig linjenummer. 
        for linjeNr, linje in enumerate(fileRead, start = 1): 
            if linjeNr == 1: #Hopper over header linje, slik at den ikke blir tatt med i listen.
                continue

            bestillingLinje = linje.rstrip('\n').split(',')  #Deler hver linje til 7 forskjellig ord.

            #Sjekker at det er 7 elementer i listen for å kunne sjekke forskjellige elementer. 
            #Hvis ikke det er 7 elementer, hopper over iterasjonen.
            if not len(bestillingLinje) == 7:
                print(f"Manglene informasjon i feltet! Feil på linje: {linjeNr} '{linje}' i {FILENAME}")
                continue

            #Lager 7 variabler slik at felt kan bli sjekket i IF setninger. 
            forNavn, etterNavn, vare, farge, storrelse, antall, pris = bestillingLinje 

            #Sjekker at antall og pris er interger. 
            try:
                antall = int(antall)
            except:
                print(f"Feil i data: {type(antall)}! Antall er ikke et int: Feil på linje: {linjeNr} '{linje}' i {FILENAME}")
                continue
            try:
                pris = int(pris)
            except:
                print(f"Feil i data: {type(pris)}! Pris er ikke et int: Feil på linje: {linjeNr} '{linje}' i {FILENAME}")
                continue

            if storrelse.upper() not in ["S", "M", "L", "XL", "XXL"]: #Sjekker at størrelsen er innen for S - XXL. 
                print(f"Feil i data: '{storrelse}'! Gjenkjenner ikke størrelse! Feil på linje: {linjeNr} '{linje}' i {FILENAME}")
                continue
            
            #Legger til verifisert data i bestillingerListen.
            bestillingerListe.append((forNavn, etterNavn, vare, farge, storrelse, antall, pris))
except FileNotFoundError as FileNotFoundErr: #Fanger feilmelding hvis filen ikke finnes.
    print("Kan ikke finne fil!:", FileNotFoundErr)


ANALYSEFILE = "salgs_analyse_svar.txt"
try:
    with open(ANALYSEFILE , "w", encoding="utf-8") as fileWrite:
        #A
        genserTeller = 0 

        for linje in bestillingerListe:
            if "Genser" in linje:  
                antall = linje[5] 
                genserTeller += antall
        fileWrite.write(f"A: Antall gensere solgt: {genserTeller}\n")

        #B
        genserInntekt = 0
        for linje in bestillingerListe:
            if "Genser" in linje:
                antall = linje[5]
                pris = linje[6]
                genserInntekt += antall *  pris
        fileWrite.write(f"B: Total inntekt fra gensere: {genserInntekt}\n")

        #C
        xlKunder = 0
        for linje in bestillingerListe:
            if "XL" in linje:
                xlKunder  += 1
        fileWrite.write(f"C: Alle kunder som kjøpte varer i 'XL': {xlKunder }\n")

        #D
        kunderMed3ellerMer = 0 
        for linje in bestillingerListe:
            antall = linje[5]
            if antall > 3:
                kunderMed3ellerMer += 1
        fileWrite.write(f"D: Alle kunder som kjøpte mer enn 3 varer: {kunderMed3ellerMer}\n")

        #E
        foreKomst = {}

        for linje in bestillingerListe:
            farge = linje[3] 
            antall = linje[5]
            if farge in foreKomst:
                foreKomst[farge] += antall
            else:
                foreKomst[farge] = antall

        hoyesteVerdi = max(foreKomst.values())
        
        mestPopFarge = [key for key, value in foreKomst.items() if value == hoyesteVerdi] # #Går gjennom forekomst ordbok, og legger til fargen(e) 
        #                                                                                 #med høygest forekomst.
        for farge in mestPopFarge:
            fileWrite.write(f"E: Den meste populære fargen(e) var: {farge}")
            if len(mestPopFarge) > 1 : #Hvis det er likt mellom 2 eller flere farger lager en nylinje.
                fileWrite.write("\n")

        print(f"Lagde fil: '{ANALYSEFILE}'")
        fileWrite.close()
except ValueError as valErr:
    print("Verdier er feil!:", valErr)