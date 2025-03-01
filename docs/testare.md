# Analiza Proiectului și Scenarii de Testare

## Analiza Proiectului

### 1. Structura Proiectului

Proiectul este organizat modular, ceea ce facilitează întreținerea și extensibilitatea acestuia. Iată o prezentare generală:

- **`src/`**: Director principal care conține codul sursă al aplicației.
  - **`models.py`**: Definește clasele de bază pentru tipurile de clădiri (`Casa`, `Bloc`, `Spital`, `Scoala`).
  - **`factory.py`**: Implementează șablonul `Abstract Factory` pentru crearea clădirilor.
  - **`program_principal.py`**: Conține clasa `ProgramPrincipal`, care gestionează operațiile asupra clădirilor (adăugare, ștergere, modificare).
  - **`display.py`**: Utilizează șablonul `Bridge` pentru separarea logicii de afișare de clasele model.
  - **`command.py`**: Implementează șablonul `Command`, definind operațiile executate, cu suport pentru `undo` și `redo`.
  - **`invoker.py`**: Gestionează execuția comenzilor și stivele de istoric pentru `Undo/Redo`.
  - **`main.py`**: Punctul de intrare al aplicației, cu interfață textuală pentru utilizator.
- **`diagrams/`**: Conține diagrame UML pentru structura claselor.
- **`docs/`**: Include documentația suplimentară și justificările șabloanelor utilizate.
  - **`justificari.md`**: Justificarea pentru șablonul `Abstract Factory`.
  - **`display_justificari.md`**: Justificarea pentru șablonul `Bridge`.
- **`README.md`**: Oferă o descriere generală și instrucțiuni de rulare.
- **`requirements.txt`**: Listează dependențele necesare.

---

### 2. Principalele Funcționalități

1. **Adăugare Clădiri**: Suportă mai multe tipuri de clădiri (`Casa`, `Bloc`, `Spital`, `Scoala`).
2. **Afișare Clădiri**: Clădirile pot fi afișate în formatele `JSON`, `CSV` sau `XML`.
3. **Modificare Clădiri**: Permite modificarea atributelor unei clădiri existente.
4. **Ștergere Clădiri**: Clădirile pot fi șterse pe baza adresei.
5. **Undo/Redo**: Permite anularea/refacerea comenzilor executate.
6. **Validare Input și Gestionare Excepții**: Se gestionează input-uri invalide și erori pentru a preveni întreruperi neașteptate.

---

## Scenarii de Testare

### 1. Adăugarea Clădirilor

#### 1.1. Adăugarea unei Case

- **Descriere**: Testează adăugarea unei case cu date valide.
- **Pași**:
  1. Rulează aplicația (`python main.py`).
  2. Selectează opțiunea `1. Adaugă Casa`.
  3. Introdu proprietarul: `Maria Popescu`.
  4. Introdu adresa: `Strada Libertății 10`.
  5. Introdu suprafața: `120`.
- **Rezultat Așteptat**:
  - Mesaj de confirmare.
  - Casa apare la opțiunea `5. Afișează toate Clădirile`.

#### 1.2. Adăugarea unui Bloc

- **Descriere**: Testează adăugarea unui bloc.
- **Pași**:
  1. Selectează opțiunea `2. Adaugă Bloc`.
  2. Introdu adresa: `Strada Principala 5`.
  3. Introdu numărul de nivele: `10`.
  4. Introdu numărul de apartamente: `100`.
- **Rezultat Așteptat**:
  - Mesaj de confirmare.
  - Blocul apare la opțiunea `5. Afișează toate Clădirile`.

#### 1.3. Adăugarea unui Spital

- **Descriere**: Testează adăugarea unui spital.
- **Pași**:
  1. Selectează opțiunea `3. Adaugă Spital`.
  2. Introdu denumirea: `Spitalul Central`.
  3. Introdu adresa: `Strada Spitalului 20`.
  4. Introdu secțiile: `Cardiologie, Neurologie, Pediatrie`.
- **Rezultat Așteptat**:
  - Mesaj de confirmare.
  - Spitalul apare la opțiunea `5. Afișează toate Clădirile`.

#### 1.4. Adăugarea unei Școli

- **Descriere**: Testează adăugarea unei școli.
- **Pași**:
  1. Selectează opțiunea `4. Adaugă Școală`.
  2. Introdu denumirea: `Liceul Teoretic`.
  3. Introdu adresa: `Strada Școlii 15`.
  4. Introdu numărul de clase: `30`.
- **Rezultat Așteptat**:
  - Mesaj de confirmare.
  - Școala apare la opțiunea `5. Afișează toate Clădirile`.

---

### 2. Afișarea Clădirilor

#### 2.1. Afișare în Format JSON

- **Descriere**: Verifică afișarea în format JSON.
- **Pași**:
  1. Selectează opțiunea `5. Afișează toate Clădirile`.
  2. Alege formatul `1. JSON`.
- **Rezultat Așteptat**:
  - Lista clădirilor este afișată în format JSON, cu indentare corespunzătoare.

#### 2.2. Afișare în Format CSV

- **Descriere**: Verifică salvarea în format CSV.
- **Pași**:
  1. Selectează opțiunea `5. Afișează toate Clădirile`.
  2. Alege formatul `2. CSV`.
- **Rezultat Așteptat**:
  - Fișierul `cladiri.csv` este creat în directorul `src/`.

#### 2.3. Afișare în Format XML

- **Descriere**: Verifică salvarea în format XML.
- **Pași**:
  1. Selectează opțiunea `5. Afișează toate Clădirile`.
  2. Alege formatul `3. XML`.
- **Rezultat Așteptat**:
  - Fișierul `cladiri.xml` este creat în directorul `src/`.

---

### 3. Modificarea Clădirilor

#### 3.1. Modificarea Adresei unei Case

- **Descriere**: Testează modificarea adresei.
- **Pași**:
  1. Selectează opțiunea `8. Modifică o Clădire`.
  2. Introdu adresa: `Strada Libertății 10`.
  3. Selectează atributul `adresa`.
  4. Introdu noua valoare: `Strada Libertății 20`.
- **Rezultat Așteptat**:
  - Mesaj de confirmare.
  - Adresa este actualizată.

#### 3.2. Modificarea Numărului de Apartamente

- **Descriere**: Testează modificarea numărului de apartamente.
- **Pași**:
  1. Selectează opțiunea `8. Modifică o Clădire`.
  2. Introdu adresa: `Strada Principala 5`.
  3. Selectează atributul `numar_apartamente`.
  4. Introdu noua valoare: `120`.
- **Rezultat Așteptat**:
  - Mesaj de confirmare.
  - Numărul de apartamente este actualizat.

---

### 4. Ștergerea Clădirilor

#### 4.1. Ștergerea unei Case

- **Descriere**: Testează ștergerea unei case.
- **Pași**:
  1. Selectează opțiunea `7. Șterge o Clădire`.
  2. Introdu adresa: `Strada Libertății 20`.
- **Rezultat Așteptat**:
  - Mesaj de confirmare.
  - Casa nu mai apare în listă.

---

### 5. Undo/Redo

#### 5.1. Undo Adăugare

- **Descriere**: Testează anularea adăugării unei clădiri.
- **Pași**:
  1. Adaugă o clădire.
  2. Selectează opțiunea `10. Undo`.
- **Rezultat Așteptat**:
  - Mesaj de confirmare.
  - Clădirea nu mai apare în listă.

#### 5.2. Redo

- **Descriere**: Testează refacerea unei comenzi.
- **Pași**:
  1. Execută `Undo`.
  2. Selectează opțiunea `11. Redo`.
- **Rezultat Așteptat**:
  - Mesaj de confirmare.
  - Clădirea reapare în listă.

---

### 6. Gestionarea Excepțiilor

#### 6.1. Input Invalid

- **Descriere**: Testează comportamentul pentru input-uri invalide.
- **Pași**:
  1. Introdu un text în loc de număr pentru suprafață.
- **Rezultat Așteptat**:
  - Mesaj de eroare: `Valoarea pentru suprafață trebuie să fie un număr real.`

