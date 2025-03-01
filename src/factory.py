# src/factory.py

from abc import ABC, abstractmethod
from models import Casa, Bloc, Spital, Scoala


class CladireFactory(ABC):
    @abstractmethod
    def create_casa(self, proprietar: str, adresa: str, suprafata: float) -> Casa:
        pass

    @abstractmethod
    def create_bloc(self, adresa: str, numar_nivele: int, numar_apartamente: int) -> Bloc:
        pass

    @abstractmethod
    def create_spital(self, denumire: str, adresa: str, sectii: list) -> Spital:
        pass

    @abstractmethod
    def create_scoala(self, denumire: str, adresa: str, numar_clase: int) -> Scoala:
        pass


class ConcreteCladireFactory(CladireFactory):
    def create_casa(self, proprietar: str, adresa: str, suprafata: float) -> Casa:
        return Casa(proprietar, adresa, suprafata)

    def create_bloc(self, adresa: str, numar_nivele: int, numar_apartamente: int) -> Bloc:
        return Bloc(adresa, numar_nivele, numar_apartamente)

    def create_spital(self, denumire: str, adresa: str, sectii: list) -> Spital:
        return Spital(denumire, adresa, sectii)

    def create_scoala(self, denumire: str, adresa: str, numar_clase: int) -> Scoala:
        return Scoala(denumire, adresa, numar_clase)
