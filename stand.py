class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo_base = prezzo_base

        self.__espositore = None
        self.__disponibile = True

    @property
    def codice(self):
        return self.__codice

    @property
    def espositore(self):
        return self.__espositore

    @property
    def disponibile(self):
        return self.__disponibile

    # No setter individuale, uno per entrambi
    def assegna_espositore(self, espositore):
        self.__espositore = espositore
        self.__disponibile = False
    @property
    def prezzo(self):
        return self.__prezzo_base

    @property
    def prezzo_base(self):
        return self.__prezzo_base

    @property
    def tipologia(self):
        return "Standard"

    @property
    def dettagli_extra(self):
        return ""

    def __str__(self):

        if self.__disponibile:
            stato = "Disponibile"
        else:
            stato = "Non disponibile"

        return f"{self.__codice}: {self.tipologia} | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.prezzo:.2f}€ {self.dettagli_extra}- {stato}"

    def __repr__(self):

        if self.__disponibile:
            stato = "Disponibile"
        else:
            stato = "Non disponibile"

        return f"{self.__codice}: {self.tipologia} | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.prezzo:.2f}€ {self.dettagli_extra}- {stato}"

    def __eq__(self, other):
        if isinstance(other, Stand):
            return self.codice == other.codice

        return False

    def __lt__(self, other):
        return self.prezzo < other.prezzo


class StandPrese(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(codice, superficie, padiglione,
                         prezzo_base)  # Accede al costruttore del padre e crea l'oggetto
        self.__numero_prese = numero_prese

    @property
    def prezzo(self):
        return self.prezzo_base * (1 + 0.07 * self.__numero_prese)

    @property
    def tipologia(self):
        return "Prese Extra"

    @property
    def dettagli_extra(self):
        return f"- Prese aggiuntive: {self.__numero_prese} "


class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione,
                         prezzo_base)  # Accede al costruttore del padre e crea l'oggetto
        self.__posizione = posizione

    @property
    def prezzo(self):
        return self.prezzo_base * 1.30

    @property
    def tipologia(self):
        return "Premium"

    @property
    def dettagli_extra(self):
        return f"- Posizione: {self.__posizione} "