# BuildingManager-DesignPatterns

A Python application for managing buildings in a locality using design patterns. This project demonstrates the implementation of Abstract Factory, Bridge, and Command patterns to create a modular, scalable, and maintainable application.

## Features

- Create and manage different types of buildings (houses, apartment buildings, hospitals, schools)
- Display buildings in multiple formats (JSON, CSV, XML)
- Filter buildings by type
- Modify building attributes
- Delete buildings
- Undo/redo operations

## Architecture

The application is built using the following design patterns:

### Abstract Factory Pattern

Used for creating different types of buildings without specifying their concrete classes.

- `CladireFactory`: Abstract factory interface
- `ConcreteCladireFactory`: Concrete implementation

### Bridge Pattern

Separates the abstraction (building classes) from the implementation (display formats).

- `Display`: Abstract display interface
- `JsonDisplay`, `CsvDisplay`, `XmlDisplay`: Concrete implementations

### Command Pattern

Encapsulates operations as objects, enabling undo/redo functionality.

- `Command`: Base command interface
- Various command implementations (e.g., `AdaugaCasaCommand`, `StergeCladireCommand`)
- `Invoker`: Manages command execution history

## Project Structure

```
src/
├── models.py           # Building classes (Casa, Bloc, Spital, Scoala)
├── factory.py          # Abstract Factory implementation
├── display.py          # Bridge pattern implementation
├── command.py          # Command pattern implementation
├── invoker.py          # Command history management
├── program_principal.py # Main application logic
└── main.py             # Application entry point
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/BuildingManager-DesignPatterns.git
cd BuildingManager-DesignPatterns
```

2. Run the application:
```bash
python src/main.py
```

## Usage

The application provides a menu-based interface with the following options:

1. Add House
2. Add Apartment Building
3. Add Hospital
4. Add School
5. Display All Buildings
6. Display Buildings by Type
7. Delete a Building
8. Modify a Building
9. Exit
10. Undo
11. Redo

## Design Choices

### Why Abstract Factory?
- Manages multiple families of building types
- Facilitates adding new building types without modifying existing code
- Keeps implementation details separate from client code

### Why Bridge?
- Separates display formats from building classes
- Makes adding new display formats easy without changing existing code
- Provides flexibility in combining different types of buildings with various display methods

### Why Command?
- Encapsulates operations as objects
- Enables undo/redo functionality
- Simplifies adding new operations

## License

This project is available under the MIT License.
