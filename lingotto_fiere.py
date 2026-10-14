import csv
from stand import Stand, StandPremium, StandPrese
from espositore import Espositore


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__stand = {}  # codice -> Stand
        self.__espositori = {}  # codice -> Espositore

    """Aggiungere setter e getter se necessari"""

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        self.__nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open(file_path, "r", encoding="utf-8") as in_file:
            reader = csv.reader(in_file)
            for riga in reader:
                codice = riga[0]

                if codice.startswith("ST"):
                    superficie = int(riga[1])
                    padiglione = int(riga[2])
                    prezzo_base = float(riga[3])
                    if len(riga) == 4:
                        nuovo_stand = Stand(codice, superficie, padiglione, prezzo_base)
                    elif len(riga) == 5:
                        # Dobbiamo capire se l'ultimo è intero o stringa
                        if riga[4].isdigit():  # numerico
                            numero_prese = int(riga[4])
                            nuovo_stand = StandPrese(codice, superficie, padiglione, prezzo_base, numero_prese)
                        else:
                            posizione = riga[4]
                            nuovo_stand = StandPremium(codice, superficie, padiglione, prezzo_base, posizione)

                    self.__stand[codice] = nuovo_stand
                elif codice.startswith("ES"):
                    nome = riga[1]
                    cognome = riga[2]
                    nuovo_espositore = Espositore(codice, nome, cognome)
                    self.__espositori[codice] = nuovo_espositore

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand not in self.__stand:
            raise ValueError(f"Errore, lo stand {codice_stand} non esiste")

        if codice_espositore not in self.__espositori:
            raise ValueError(f"Errore, l'espositore {codice_espositore} non esiste")

        # Dato che esistono, ricaviamo gli oggetti
        stand = self.__stand[codice_stand]
        espositore = self.__espositori[codice_espositore]

        if not stand.disponibile:
            raise ValueError(f"Errore, lo stand {codice_stand} non è disponibile")

        if espositore.stand is not None:
            raise ValueError(f"Errore, l'espositore {codice_espositore} ha già uno stand")

        # Finalmente tutto a posto
        stand.assegna_espositore(espositore)
        espositore.stand = stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self.__espositori.values():
            print(espositore)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.__stand.values())  # Lo ordina usando il metodo Stand.__lt__ per comparare
