class Espositore:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome

        self.__stand = None # inizialmente nessuno stand assegnato

    @property
    def codice(self):
        return self.__codice

    @property
    def stand(self):
        return self.__stand

    @stand.setter
    def stand(self, nuovo_stand):
        self.__stand = nuovo_stand

    def __str__(self):
        if self.__stand == None: # stand non ancora assegnato
            return f"{self.__codice}: {self.__nome} {self.__cognome} - Nessuno stand"

        return f"{self.__codice}: {self.__nome} {self.__cognome} - Stand: {self.__stand}"

    def __repr__(self):
        if self.__stand == None: # stand non ancora assegnato
            return f"{self.__codice}: {self.__nome} {self.__cognome} - Nessuno stand"

        return f"{self.__codice}: {self.__nome} {self.__cognome} - Stand: {self.__stand}"

    def __eq__(self, other): # nel caso in cui verifichiamo a == b, a sarebbe self, b sarebbe other
        if isinstance(other, Espositore):
            return self.__codice == other.__codice # alla fine stiamo comparando i codici UNIVOCI

        return False