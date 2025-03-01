# src/models.py

class Casa:
    def __init__(self, proprietar: str, adresa: str, suprafata: float):
        self.proprietar = proprietar
        self.adresa = adresa
        self.suprafata = suprafata

    def AccesProprietar(self) -> str:
        return self.proprietar

    def AccesAdresa(self) -> str:
        return self.adresa

    def AccesSuprafata(self) -> float:
        return self.suprafata

    def ActualizareProprietar(self, proprietar: str) -> None:
        self.proprietar = proprietar

    def ActualizareAdresa(self, adresa: str) -> None:
        self.adresa = adresa

    def ActualizareSuprafata(self, suprafata: float) -> None:
        self.suprafata = suprafata

    def Afisare(self) -> None:
        print(f"Casa proprietar: {self.proprietar}, Adresa: {self.adresa}, Suprafata: {self.suprafata} m²")


class Bloc:
    def __init__(self, adresa: str, numar_nivele: int, numar_apartamente: int):
        self.adresa = adresa
        self.numar_nivele = numar_nivele
        self.numar_apartamente = numar_apartamente

    def AccesAdresa(self) -> str:
        return self.adresa

    def AccesNumarNivele(self) -> int:
        return self.numar_nivele

    def AccesNumarApartamente(self) -> int:
        return self.numar_apartamente

    def ActualizareAdresa(self, adresa: str) -> None:
        self.adresa = adresa

    def ActualizareNumarNivele(self, numar_nivele: int) -> None:
        self.numar_nivele = numar_nivele

    def ActualizareNumarApartamente(self, numar_apartamente: int) -> None:
        self.numar_apartamente = numar_apartamente

    def Afisare(self) -> None:
        print(f"Bloc Adresa: {self.adresa}, Nivele: {self.numar_nivele}, Apartamente: {self.numar_apartamente}")


class Spital:
    def __init__(self, denumire: str, adresa: str, sectii: list):
        self.denumire = denumire
        self.adresa = adresa
        self.sectii = sectii

    def AccesDenumire(self) -> str:
        return self.denumire

    def AccesAdresa(self) -> str:
        return self.adresa

    def AccesSectii(self) -> list:
        return self.sectii

    def ActualizareDenumire(self, denumire: str) -> None:
        self.denumire = denumire

    def ActualizareAdresa(self, adresa: str) -> None:
        self.adresa = adresa

    def ActualizareSectii(self, sectii: list) -> None:
        self.sectii = sectii

    def Afisare(self) -> None:
        print(f"Spital Denumire: {self.denumire}, Adresa: {self.adresa}, Sectii: {', '.join(self.sectii)}")


class Scoala:
    def __init__(self, denumire: str, adresa: str, numar_clase: int):
        self.denumire = denumire
        self.adresa = adresa
        self.numar_clase = numar_clase

    def AccesDenumire(self) -> str:
        return self.denumire

    def AccesAdresa(self) -> str:
        return self.adresa

    def AccesNumarClase(self) -> int:
        return self.numar_clase

    def ActualizareDenumire(self, denumire: str) -> None:
        self.denumire = denumire

    def ActualizareAdresa(self, adresa: str) -> None:
        self.adresa = adresa

    def ActualizareNumarClase(self, numar_clase: int) -> None:
        self.numar_clase = numar_clase

    def Afisare(self) -> None:
        print(f"Scoala Denumire: {self.denumire}, Adresa: {self.adresa}, Număr Clase: {self.numar_clase}")
