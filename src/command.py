# src/command.py

from abc import ABC, abstractmethod
from program_principal import ProgramPrincipal
from display import Display
from models import Casa, Bloc, Scoala, Spital


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class AdaugaCasaCommand(Command):
    def __init__(self, program: ProgramPrincipal, proprietar: str, adresa: str, suprafata: float):
        self.program = program
        self.proprietar = proprietar
        self.adresa = adresa
        self.suprafata = suprafata

    def execute(self):
        try:
            self.program.adauga_casa(self.proprietar, self.adresa, self.suprafata)
        except Exception as e:
            print(f"A apărut o eroare la execuția comenzii AdaugaCasa: {e}")

    def undo(self):
        try:
            self.program.sterge_cladire(self.adresa)
            print(f"Undo: Casa de la adresa '{self.adresa}' a fost ștearsă.")
        except Exception as e:
            print(f"A apărut o eroare la anularea comenzii AdaugaCasa: {e}")

    def redo(self):
        try:
            self.program.adauga_casa(self.proprietar, self.adresa, self.suprafata)
            print(f"Redo: Casa de la adresa '{self.adresa}' a fost re-adăugată.")
        except Exception as e:
            print(f"A apărut o eroare la refacerea comenzii AdaugaCasa: {e}")


class AdaugaBlocCommand(Command):
    def __init__(self, program: ProgramPrincipal, adresa: str, numar_nivele: int, numar_apartamente: int):
        self.program = program
        self.adresa = adresa
        self.numar_nivele = numar_nivele
        self.numar_apartamente = numar_apartamente

    def execute(self):
        try:
            self.program.adauga_bloc(self.adresa, self.numar_nivele, self.numar_apartamente)
        except Exception as e:
            print(f"A apărut o eroare la execuția comenzii AdaugaBloc: {e}")

    def undo(self):
        try:
            self.program.sterge_cladire(self.adresa)
        except Exception as e:
            print(f"A apărut o eroare la anularea comenzii AdaugaBloc: {e}")


class AdaugaSpitalCommand(Command):
    def __init__(self, program: ProgramPrincipal, denumire: str, adresa: str, sectii: list):
        self.program = program
        self.denumire = denumire
        self.adresa = adresa
        self.sectii = sectii

    def execute(self):
        try:
            self.program.adauga_spital(self.denumire, self.adresa, self.sectii)
        except Exception as e:
            print(f"A apărut o eroare la execuția comenzii AdaugaSpital: {e}")


class AdaugaScoalaCommand(Command):
    def __init__(self, program: ProgramPrincipal, denumire: str, adresa: str, numar_clase: int):
        self.program = program
        self.denumire = denumire
        self.adresa = adresa
        self.numar_clase = numar_clase

    def execute(self):
        try:
            self.program.adauga_scoala(self.denumire, self.adresa, self.numar_clase)
        except Exception as e:
            print(f"A apărut o eroare la execuția comenzii AdaugaScoala: {e}")


class AfiseazaCladiriCommand(Command):
    def __init__(self, program: ProgramPrincipal, display: Display):
        self.program = program
        self.display = display

    def execute(self):
        try:
            self.program.afiseaza_cladiri(self.display)
        except Exception as e:
            print(f"A apărut o eroare la execuția comenzii AfiseazaCladiri: {e}")


class AfiseazaCladiriDeTipCommand(Command):
    def __init__(self, program: ProgramPrincipal, display: Display, tip_cladire: str):
        self.program = program
        self.display = display
        self.tip_cladire = tip_cladire.lower()

    def execute(self):
        try:
            cladiri_filtrate = self.program.get_cladiri_de_tip(self.tip_cladire)
            self.display.display(cladiri_filtrate)
        except Exception as e:
            print(f"A apărut o eroare la execuția comenzii AfiseazaCladiriDeTip: {e}")


class StergeCladireCommand(Command):
    def __init__(self, program: ProgramPrincipal, adresa: str):
        self.program = program
        self.adresa = adresa
        self.stergere_cladire = None

    def execute(self):
        try:
            cladire_gasita = next((c for c in self.program.cladiri if c.adresa.lower() == self.adresa.lower()), None)
            if cladire_gasita:
                self.stergere_cladire = cladire_gasita
                self.program.sterge_cladire(self.adresa)
            else:
                print(f"Clădirea de la adresa '{self.adresa}' nu a fost găsită.")
        except Exception as e:
            print(f"A apărut o eroare la execuția comenzii StergeCladire: {e}")

    def undo(self):
        try:
            if self.stergere_cladire:
                if isinstance(self.stergere_cladire, Casa):
                    self.program.adauga_casa(self.stergere_cladire.proprietar, self.stergere_cladire.adresa,
                                             self.stergere_cladire.suprafata)
                elif isinstance(self.stergere_cladire, Bloc):
                    self.program.adauga_bloc(self.stergere_cladire.adresa, self.stergere_cladire.numar_nivele,
                                             self.stergere_cladire.numar_apartamente)
                elif isinstance(self.stergere_cladire, Spital):
                    self.program.adauga_spital(self.stergere_cladire.denumire, self.stergere_cladire.adresa,
                                               self.stergere_cladire.sectii)
                elif isinstance(self.stergere_cladire, Scoala):
                    self.program.adauga_scoala(self.stergere_cladire.denumire, self.stergere_cladire.adresa,
                                               self.stergere_cladire.numar_clase)
                print(f"Ștergerea clădirii de la adresa '{self.adresa}' a fost anulată.")
        except Exception as e:
            print(f"A apărut o eroare la anularea comenzii StergeCladire: {e}")

    def redo(self):
        try:
            if self.stergere_cladire:
                self.program.sterge_cladire(self.adresa)
                print(f"Redo: Clădirea de la adresa '{self.adresa}' a fost ștearsă din nou.")
        except Exception as e:
            print(f"A apărut o eroare la refacerea comenzii StergeCladire: {e}")


class ModificaCladireCommand(Command):
    def __init__(self, program: ProgramPrincipal, adresa: str, atribut: str, noua_valoare):
        self.program = program
        self.adresa = adresa
        self.atribut = atribut.lower()
        self.noua_valoare = noua_valoare
        self.valoare_anterioara = None

    def execute(self):
        try:
            cladire_gasita = next((c for c in self.program.cladiri if c.adresa.lower() == self.adresa.lower()), None)
            if cladire_gasita:
                if hasattr(cladire_gasita, self.atribut):
                    self.valoare_anterioara = getattr(cladire_gasita, self.atribut)
                    setattr(cladire_gasita, self.atribut, self.noua_valoare)
                    print(f"Atributul '{self.atribut}' al clădirii de la adresa '{self.adresa}' a fost actualizat.")
                else:
                    print(f"Atributul '{self.atribut}' nu există în clasa '{cladire_gasita.__class__.__name__}'.")
            else:
                print(f"Clădirea de la adresa '{self.adresa}' nu a fost găsită.")
        except Exception as e:
            print(f"A apărut o eroare la execuția comenzii ModificaCladire: {e}")

    def undo(self):
        try:
            cladire_gasita = next((c for c in self.program.cladiri if c.adresa.lower() == self.adresa.lower()), None)
            if cladire_gasita and self.valoare_anterioara is not None:
                setattr(cladire_gasita, self.atribut, self.valoare_anterioara)
                print(
                    f"Undo: Atributul '{self.atribut}' al clădirii de la adresa '{self.adresa}' a fost revenit la valoarea anterioară.")
            else:
                print(
                    f"Clădirea de la adresa '{self.adresa}' nu a fost găsită sau nu există o valoare anterioară pentru '{self.atribut}'.")
        except Exception as e:
            print(f"A apărut o eroare la anularea comenzii ModificaCladire: {e}")

    def redo(self):
        try:
            cladire_gasita = next((c for c in self.program.cladiri if c.adresa.lower() == self.adresa.lower()), None)
            if cladire_gasita:
                setattr(cladire_gasita, self.atribut, self.noua_valoare)
                print(
                    f"Redo: Atributul '{self.atribut}' al clădirii de la adresa '{self.adresa}' a fost actualizat din nou.")
        except Exception as e:
            print(f"A apărut o eroare la refacerea comenzii ModificaCladire: {e}")
