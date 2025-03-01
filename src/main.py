# src/main.py

from factory import ConcreteCladireFactory
from program_principal import ProgramPrincipal
from display import JsonDisplay, CsvDisplay, XmlDisplay
from command import (
    AdaugaCasaCommand,
    AdaugaBlocCommand,
    AdaugaSpitalCommand,
    AdaugaScoalaCommand,
    AfiseazaCladiriCommand,
    AfiseazaCladiriDeTipCommand,
    StergeCladireCommand,
    ModificaCladireCommand
)
from invoker import Invoker


def main():
    factory = ConcreteCladireFactory()
    program = ProgramPrincipal(factory)
    invoker = Invoker()

    VALID_TIPURI = ['casa', 'bloc', 'spital', 'scoala']

    while True:
        print("\nSelectează o operațiune:")
        print("1. Adaugă Casa")
        print("2. Adaugă Bloc")
        print("3. Adaugă Spital")
        print("4. Adaugă Școală")
        print("5. Afișează toate Clădirile")
        print("6. Afișează Clădirile de un Anume Tip")
        print("7. Șterge o Clădire")
        print("8. Modifică o Clădire")
        print("10. Undo")
        print("11. Redo")
        print("9. Ieși")

        alegere = input("Introdu numărul operațiunii dorite (1-11): ")

        if alegere == '1':
            proprietar = input("Introdu proprietarul: ")
            adresa = input("Introdu adresa: ")
            try:
                suprafata = float(input("Introdu suprafața (m²): "))
                command = AdaugaCasaCommand(program, proprietar, adresa, suprafata)
                invoker.execute_command(command)
            except ValueError:
                print("Valoarea pentru suprafață trebuie să fie un număr real.")

        elif alegere == '2':
            adresa = input("Introdu adresa: ")
            try:
                numar_nivele = int(input("Introdu numărul de nivele: "))
                numar_apartamente = int(input("Introdu numărul de apartamente: "))
                command = AdaugaBlocCommand(program, adresa, numar_nivele, numar_apartamente)
                invoker.execute_command(command)
            except ValueError:
                print("Valorile pentru numărul de nivele și numărul de apartamente trebuie să fie numere întregi.")

        elif alegere == '3':
            denumire = input("Introdu denumirea spitalului: ")
            adresa = input("Introdu adresa: ")
            sectii_input = input("Introdu sectiile (separate prin virgulă): ")
            sectii = [sectie.strip() for sectie in sectii_input.split(',')]
            command = AdaugaSpitalCommand(program, denumire, adresa, sectii)
            invoker.execute_command(command)

        elif alegere == '4':
            denumire = input("Introdu denumirea școlii: ")
            adresa = input("Introdu adresa: ")
            try:
                numar_clase = int(input("Introdu numărul de clase: "))
                command = AdaugaScoalaCommand(program, denumire, adresa, numar_clase)
                invoker.execute_command(command)
            except ValueError:
                print("Valoarea pentru numărul de clase trebuie să fie un număr întreg.")

        elif alegere == '5':
            print("\nSelectează formatul de afișare:")
            print("1. JSON")
            print("2. CSV")
            print("3. XML")
            format_alege = input("Introdu numărul formatului dorit (1/2/3): ")
            if format_alege == '1':
                display = JsonDisplay()
            elif format_alege == '2':
                display = CsvDisplay()
            elif format_alege == '3':
                display = XmlDisplay()
            else:
                print("Alegere invalidă. Se va utiliza formatul JSON implicit.")
                display = JsonDisplay()
            command = AfiseazaCladiriCommand(program, display)
            invoker.execute_command(command)

        elif alegere == '6':
            tip_cladire = input("Introdu tipul clădirii (Casa, Bloc, Spital, Scoala): ").strip().lower()
            if tip_cladire not in VALID_TIPURI:
                print(
                    "Tip de clădire invalid. Te rog să introduci unul dintre următoarele: Casa, Bloc, Spital, Scoala.")
                continue  # Revino la începutul buclei
            print("\nSelectează formatul de afișare:")
            print("1. JSON")
            print("2. CSV")
            print("3. XML")
            format_alege = input("Introdu numărul formatului dorit (1/2/3): ")
            if format_alege == '1':
                display = JsonDisplay()
            elif format_alege == '2':
                display = CsvDisplay()
            elif format_alege == '3':
                display = XmlDisplay()
            else:
                print("Alegere invalidă. Se va utiliza formatul JSON implicit.")
                display = JsonDisplay()
            command = AfiseazaCladiriDeTipCommand(program, display, tip_cladire)
            invoker.execute_command(command)


        elif alegere == '7':
            adresa = input("Introdu adresa clădirii de șters: ").strip()
            if not adresa:
                print("Adresa nu poate fi goală.")
                continue
            command = StergeCladireCommand(program, adresa)
            invoker.execute_command(command)

        elif alegere == '8':
            adresa = input("Introdu adresa clădirii de modificat: ").strip()
            cladire_gasita = next((c for c in program.cladiri if c.adresa.lower() == adresa.lower()), None)
            if not cladire_gasita:
                print(f"Clădirea de la adresa '{adresa}' nu a fost găsită.")
                continue

            atribute = program.get_atribute_cladire(cladire_gasita)
            print("\nAtribute disponibile pentru modificare:")
            for idx, attr in enumerate(atribute, start=1):
                print(f"{idx}. {attr}")

            try:
                select_atribut = int(input("Selectează numărul atributului de modificat: "))
                if 1 <= select_atribut <= len(atribute):
                    atribut = atribute[select_atribut - 1]
                else:
                    print("Selectare invalidă.")
                    continue
            except ValueError:
                print("Te rog să introduci un număr valid.")
                continue

            noua_valoare = input(f"Introdu noua valoare pentru '{atribut}': ")

            # Determinăm tipul atributului pentru conversie
            try:
                if isinstance(getattr(cladire_gasita, atribut), float):
                    noua_valoare = float(noua_valoare)
                elif isinstance(getattr(cladire_gasita, atribut), int):
                    noua_valoare = int(noua_valoare)
                elif isinstance(getattr(cladire_gasita, atribut), list):
                    noua_valoare = [item.strip() for item in noua_valoare.split(',')]
                else:
                    # Pentru string sau alte tipuri, nu facem conversie
                    pass
            except ValueError:
                print(f"Valoarea pentru '{atribut}' trebuie să fie de tipul corespunzător.")
                continue

            command = ModificaCladireCommand(program, adresa, atribut, noua_valoare)
            invoker.execute_command(command)

        elif alegere == '10':
            invoker.undo()

        elif alegere == '11':
            invoker.redo()

        elif alegere == '9':
            print("Ieşire din aplicație. La revedere!")
            break

        else:
            print("Alegere invalidă. Te rog să introduci un număr între 1 și 11.")


if __name__ == "__main__":
    main()
