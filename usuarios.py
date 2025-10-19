# usuarios.py
# Clases que representan a un usuario y la estructura de datos general

class EstructuraDatosUsuario:
    def __init__(self, tipo_id: str, num_id: int, nombre: str, edad: int,
                 estrato: int, tipo_atencion: str, valor_copago: float, fecha_registro: str):
        self.tipo_id = tipo_id
        self.num_id = int(num_id)
        self.nombre = nombre
        self.edad = int(edad)
        self.estrato = int(estrato)
        self.tipo_atencion = tipo_atencion
        self.valor_copago = float(valor_copago)
        self.fecha_registro = fecha_registro

    def to_tuple(self):
        """Devuelve una tupla con los campos para poblar el Treeview"""
        return (self.tipo_id, str(self.num_id), self.nombre, str(self.edad),
                str(self.estrato), self.tipo_atencion, f"${int(self.valor_copago):,}",
                self.fecha_registro)


# 🔹 Nueva clase contenedora para manejar varios usuarios
class ListaUsuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario: EstructuraDatosUsuario):
        self.usuarios.append(usuario)

    def obtener_todos(self):
        return self.usuarios
