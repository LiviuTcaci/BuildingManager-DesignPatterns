# src/display.py

from abc import ABC, abstractmethod
import json
import csv
import xml.etree.ElementTree as ET
from typing import List
from models import Casa, Bloc, Spital, Scoala


# Implementarea Interfeței Display
class Display(ABC):
    @abstractmethod
    def display(self, cladiri: List):
        pass


# Implementare pentru format JSON
class JsonDisplay(Display):
    def display(self, cladiri: List) -> None:
        cladiri_dict = [cladire.__dict__ for cladire in cladiri]
        print(json.dumps(cladiri_dict, indent=4))


# Implementare pentru format CSV
class CsvDisplay(Display):
    def display(self, cladiri: List) -> None:
        if not cladiri:
            print("Nu există clădiri de afișat.")
            return

        # Colectează toate câmpurile din toate clădirile
        fieldnames = set()
        for cladire in cladiri:
            fieldnames.update(cladire.__dict__.keys())
        fieldnames = sorted(fieldnames)  # Sortare pentru consistență

        with open('cladiri.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for cladire in cladiri:
                # Asigură-te că toate cheile există, completând cu valori goale dacă este necesar
                row = {field: cladire.__dict__.get(field, "") for field in fieldnames}
                writer.writerow(row)
        print("Clădirile au fost salvate în 'cladiri.csv'.")


# Implementare pentru format XML
class XmlDisplay(Display):
    def display(self, cladiri: List) -> None:
        root = ET.Element("Cladiri")
        for cladire in cladiri:
            cladire_elem = ET.SubElement(root, cladire.__class__.__name__)
            for key, value in cladire.__dict__.items():
                if isinstance(value, list):
                    sub_elem = ET.SubElement(cladire_elem, key)
                    for item in value:
                        ET.SubElement(sub_elem, "Item").text = item
                else:
                    ET.SubElement(cladire_elem, key).text = str(value)
        tree = ET.ElementTree(root)
        tree.write("cladiri.xml", encoding='utf-8', xml_declaration=True)
        print("Clădirile au fost salvate în 'cladiri.xml'.")
