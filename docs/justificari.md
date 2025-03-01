# Justificări pentru Alegerea Șablonului de Proiectare Creational

## Alegerea Șablonului: Abstract Factory

### Motivație:

În proiectul nostru, gestionăm mai multe tipuri de clădiri: `Casa`, `Bloc`, `Spital`, și `Scoala`. Fiecare dintre
acestea are propriile atribute și metode, dar toate fac parte dintr-o familie de produse (clădiri).

### De ce Abstract Factory:

- **Multiple Familii de Produse**: Având mai multe tipuri de clădiri, Abstract Factory permite crearea de obiecte din
  diferite familii într-un mod organizat.
- **Scalabilitate**: Este ușor să adaugi noi tipuri de clădiri fără a modifica codul existent. Trebuie doar să extinzi
  factory-ul concret.
- **Independența de Implementare**: Clasa `ProgramPrincipal` nu cunoaște detaliile concrete ale instanțierii obiectelor,
  ceea ce reduce dependențele și crește modularitatea.

### De ce nu Factory Method:

- **Singură Familie de Produse**: Factory Method este mai potrivit când se lucrează cu o singură familie de produse, în
  timp ce noi avem multiple tipuri de clădiri.
- **Complexitate**: Utilizarea Abstract Factory ne oferă o soluție mai potrivită pentru nevoile noastre, evitând
  complexitatea suplimentară care ar putea apărea cu Factory Method în contextul actual.

---

## **4. Testarea Implementării**

După ce ai creat toate fișierele și ai implementat codul conform indicațiilor de mai sus, este esențial să testezi
aplicația pentru a te asigura că totul funcționează corect.

### **4.1. Executarea Aplicației**

Navighează în directorul `src/` și rulează `main.py`:

```bash
cd src/
python main.py
```

# Justificări pentru Alegerea Șablonului de Proiectare Structural

## Alegerea Șablonului: Bridge

### Motivație:

Aplicația noastră necesită afișarea informațiilor despre clădiri în multiple formate: `JSON`, `CSV`, `XML`, etc. Dorim
să separăm logica de afișare de clasele de bază ale clădirilor pentru a facilita adăugarea de noi formate fără a
modifica clasele existente.

### De ce Bridge:

- **Separarea Abstracției de Implementare:** Permite gestionarea independentă a logicii de afișare și a claselor de
  clădiri.
- **Scalabilitate:** Adăugarea unui nou format de afișare este simplă, doar prin crearea unei noi clase care
  implementează interfața `Display`.
- **Flexibilitate:** Permite combinarea diferitelor metode de afișare cu diversele tipuri de clădiri fără crearea de
  clase intermediare complexe.

### De ce nu Adapter sau Decorator:

- **Adapter:** Este mai potrivit pentru a face interoperabile două interfețe existente, ceea ce nu este cazul nostru.
- **Decorator:** Este util pentru adăugarea de comportamente suplimentare la obiecte, dar nu pentru separarea logicii de
  afișare de clasele de bază.

# Justificări pentru Alegerea Șablonului de Proiectare Comportamental

## Alegerea Șablonului: Command

### Motivație:

Aplicația noastră gestionează diverse operațiuni asupra clădirilor, cum ar fi adăugarea, ștergerea și afișarea acestora.
Pentru a face aceste operațiuni mai flexibile și mai ușor de extins, am ales să utilizăm șablonul de proiectare
comportamental **Command**.

### De ce Command:

- **Separarea Responsabilităților:** Comenzile separă obiectele care emit cererea de obiectele care o execută.
- **Extensibilitate:** Este ușor să adaugi noi comenzi fără a modifica codul existent.
- **Istoric și Undo/Redo:** Facilitează implementarea funcționalităților de istoricul comenzilor sau de anulare a
  acestora.
- **Parametrizarea Obiectelor:** Permite trecerea comenzilor ca parametri, stocarea și gestionarea acestora în mod
  flexibil.

### Implementare:

- **Interfața `Command`:** Definește metoda `execute`.
- **Comenzi Concrete:** Fiecare operațiune (adăugare, afișare) este implementată ca o clasă care moștenește `Command` și
  implementează metoda `execute`.
- **Invoker:** Gestionază execuția comenzilor și poate menține un istoric al acestora.

### Avantaje:

- **Modularitate:** Fiecare comandă este o clasă separată, ceea ce face codul mai ușor de întreținut și de înțeles.
- **Flexibilitate:** Comenzile pot fi combinate și reutilizate în diferite contexte.
- **Extensibilitate:** Adăugarea de noi funcționalități se face prin crearea de noi clase de comenzi, fără a afecta
  codul existent.

### De ce nu Alte Șabloane:

- **Strategy:** Se potrivește pentru selectarea dinamică a algoritmilor, dar nu pentru gestionarea operațiunilor
  complexe.
- **Observer:** Este mai potrivit pentru notificări de schimbare de stare, dar nu pentru executarea operațiunilor de
  acțiune.