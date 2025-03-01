# src/invoker.py

class Invoker:
    def __init__(self):
        self.history = []
        self.redo_stack = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)
        self.redo_stack.clear()  # Clear redo stack after executing a new command

    def undo(self):
        if not self.history:
            print("Nu există comenzi de anulat.")
            return
        command = self.history.pop()
        if hasattr(command, 'undo'):
            command.undo()
            self.redo_stack.append(command)
            print("Comanda a fost anulată.")
        else:
            print("Comanda nu suportă funcționalitatea Undo.")

    def redo(self):
        if not self.redo_stack:
            print("Nu există comenzi de refăcut.")
            return
        command = self.redo_stack.pop()
        if hasattr(command, 'redo'):
            command.redo()
            self.history.append(command)
            print("Comanda a fost refăcută.")
        else:
            print("Comanda nu suportă funcționalitatea Redo.")
