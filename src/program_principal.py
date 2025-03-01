# src/program_principal.py

from factory import CladireFactory
from models import Casa, Bloc, Spital, Scoala
from display import Display


class ProgramPrincipal:
    def __init__(self, factory: CladireFactory):
        self.factory = factory
        self.cladiri = []

    def adauga_casa(self, proprietar: str, adresa: str, suprafata: float) -> None:
        try:
            casa = self.factory.create_casa(proprietar, adresa, suprafata)
            self.cladiri.append(casa)
            print(
                f"Clădirea a fost adăugată: Casa proprietar: {proprietar}, Adresa: {adresa}, Suprafata: {suprafata} m²")
        except Exception as e:
            print(f"A apărut o eroare la adăugarea casei: {e}")

    def adauga_bloc(self, adresa: str, numar_nivele: int, numar_apartamente: int) -> None:
        try:
            bloc = self.factory.create_bloc(adresa, numar_nivele, numar_apartamente)
            self.cladiri.append(bloc)
            print(
                f"Clădirea a fost adăugată: Bloc Adresa: {adresa}, Nivele: {numar_nivele}, Apartamente: {numar_apartamente}")
        except Exception as e:
            print(f"A apărut o eroare la adăugarea blocului: {e}")

    def adauga_spital(self, denumire: str, adresa: str, sectii: list) -> None:
        try:
            spital = self.factory.create_spital(denumire, adresa, sectii)
            self.cladiri.append(spital)
            print(
                f"Clădirea a fost adăugată: Spital Denumire: {denumire}, Adresa: {adresa}, Sectii: {', '.join(sectii)}")
        except Exception as e:
            print(f"A apărut o eroare la adăugarea spitalului: {e}")

    def adauga_scoala(self, denumire: str, adresa: str, numar_clase: int) -> None:
        try:
            scoala = self.factory.create_scoala(denumire, adresa, numar_clase)
            self.cladiri.append(scoala)
            print(
                f"Clădirea a fost adăugată: Scoala Denumire: {denumire}, Adresa: {adresa}, Număr Clase: {numar_clase}")
        except Exception as e:
            print(f"A apărut o eroare la adăugarea școlii: {e}")

    def afiseaza_cladiri(self, display: Display) -> None:
        try:
            display.display(self.cladiri)
        except Exception as e:
            print(f"A apărut o eroare la afișarea clădirilor: {e}")

    def get_cladiri_de_tip(self, tip_cladire: str):
        try:
            tip_cladire = tip_cladire.strip().lower()
            print(f"Tipul de clădire filtrat: '{tip_cladire}'")  # Mesaj de debugging
            for cladire in self.cladiri:
                cladire_tip = cladire.__class__.__name__.lower()
                print(f"Cladire tip: '{cladire_tip}', Adresa: '{cladire.adresa}'")  # Mesaj de debugging
            return [cladire for cladire in self.cladiri if cladire.__class__.__name__.lower() == tip_cladire]
        except Exception as e:
            print(f"A apărut o eroare la filtrarea clădirilor: {e}")
            return []

    def sterge_cladire(self, adresa: str) -> None:
        try:
            cladire_gasita = next((c for c in self.cladiri if c.adresa.lower() == adresa.lower()), None)
            if cladire_gasita:
                self.cladiri.remove(cladire_gasita)
                print(f"Clădirea de la adresa '{adresa}' a fost ștearsă.")
            else:
                print(f"Clădirea de la adresa '{adresa}' nu a fost găsită.")
        except Exception as e:
            print(f"A apărut o eroare la ștergerea clădirii: {e}")

    def modifica_cladire(self, adresa: str, atribut: str, noua_valoare) -> None:
        try:
            cladire_gasita = next((c for c in self.cladiri if c.adresa.lower() == adresa.lower()), None)
            if cladire_gasita:
                if hasattr(cladire_gasita, atribut):
                    setattr(cladire_gasita, atribut, noua_valoare)
                    print(f"Atributul '{atribut}' al clădirii de la adresa '{adresa}' a fost actualizat.")
                else:
                    print(f"Atributul '{atribut}' nu există în clasa '{cladire_gasita.__class__.__name__}'.")
            else:
                print(f"Clădirea de la adresa '{adresa}' nu a fost găsită.")
        except Exception as e:
            print(f"A apărut o eroare la modificarea clădirii: {e}")

    def get_atribute_cladire(self, cladire):
        # Returnează o listă de atribute care pot fi modificate
        # Ignorăm metodele și atributele private
        return [attr for attr in cladire.__dict__.keys()]
