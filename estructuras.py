# estructuras.py
# Estructuras de datos básicas: Pila, Cola y Lista

# 🔹 Clase Pila (LIFO)
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0

    def ver_tope(self):
        if not self.esta_vacia():
            return self.elementos[-1]

    def __len__(self):
        return len(self.elementos)


# 🔹 Clase Cola (FIFO)
class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __len__(self):
        return len(self.elementos)


# 🔹 Clase Lista (manejo genérico)
class Lista:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)

    def buscar(self, elemento):
        return elemento in self.elementos

    def obtener_todos(self):
        return self.elementos
