# formulario.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
from usuarios import EstructuraDatosUsuario
from estructuras import Pila, Cola, Lista

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("EPS Salvando Vidas - Control de Usuarios")
        self.master.geometry("1000x500")

        # Estructuras de datos
        self.pila = Pila()
        self.cola = Cola()
        self.lista = Lista()

        # Marco principal
        frame = ttk.LabelFrame(master, text="Registro de Usuarios")
        frame.pack(fill="x", padx=10, pady=10)

        # --- Campos de entrada ---
        ttk.Label(frame, text="Estructura:").grid(row=0, column=0, sticky="w")
        self.cmb_estructura = ttk.Combobox(frame, values=["Pila", "Cola", "Lista"], state="readonly")
        self.cmb_estructura.grid(row=0, column=1)
        self.cmb_estructura.current(0)

        ttk.Label(frame, text="Tipo ID:").grid(row=1, column=0, sticky="w")
        self.cmb_tipoid = ttk.Combobox(frame, values=["CC", "CE", "NUIP", "PAS"], state="readonly")
        self.cmb_tipoid.grid(row=1, column=1)
        self.cmb_tipoid.current(0)

        ttk.Label(frame, text="Número ID:").grid(row=2, column=0, sticky="w")
        self.txt_numid = ttk.Entry(frame)
        self.txt_numid.grid(row=2, column=1)

        ttk.Label(frame, text="Nombre:").grid(row=3, column=0, sticky="w")
        self.txt_nombre = ttk.Entry(frame)
        self.txt_nombre.grid(row=3, column=1)

        ttk.Label(frame, text="Edad:").grid(row=4, column=0, sticky="w")
        self.txt_edad = ttk.Entry(frame)
        self.txt_edad.grid(row=4, column=1)

        ttk.Label(frame, text="Estrato:").grid(row=5, column=0, sticky="w")
        self.cmb_estrato = ttk.Combobox(frame, values=["1", "2", "3", "4", "5", "6"], state="readonly")
        self.cmb_estrato.grid(row=5, column=1)
        self.cmb_estrato.current(0)

        ttk.Label(frame, text="Atención:").grid(row=6, column=0, sticky="w")
        self.atencion_var = tk.StringVar(value="Medicina General")
        ttk.Radiobutton(frame, text="Medicina General", variable=self.atencion_var, value="Medicina General").grid(row=6, column=1, sticky="w")
        ttk.Radiobutton(frame, text="Laboratorio", variable=self.atencion_var, value="Laboratorio").grid(row=6, column=2, sticky="w")

        ttk.Label(frame, text="Copago:").grid(row=7, column=0, sticky="w")
        self.txt_copago = ttk.Entry(frame, state="readonly")
        self.txt_copago.grid(row=7, column=1)
        self.cmb_estrato.bind("<<ComboboxSelected>>", self.actualizar_copago)

        ttk.Label(frame, text="Fecha:").grid(row=8, column=0, sticky="w")
        self.txt_fecha = ttk.Entry(frame)
        self.txt_fecha.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.txt_fecha.grid(row=8, column=1)

        ttk.Button(frame, text="Registrar", command=self.registrar_usuario).grid(row=9, column=0, pady=5)
        ttk.Button(frame, text="Limpiar", command=self.limpiar_formulario).grid(row=9, column=1, pady=5)

        # --- Sección inferior: Datos ---
        frame_datos = ttk.LabelFrame(master, text="Datos de Usuarios")
        frame_datos.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Label(frame_datos, text="Ver Estructura:").grid(row=0, column=0, sticky="w")
        self.cmb_ver = ttk.Combobox(frame_datos, values=["Pila", "Cola", "Lista"], state="readonly")
        self.cmb_ver.grid(row=0, column=1)
        self.cmb_ver.current(0)
        self.cmb_ver.bind("<<ComboboxSelected>>", lambda e: self.mostrar_datos())

        columnas = ("Estructura", "ID", "Nombre", "Edad", "Estrato", "Atencion", "Copago", "Fecha")
        self.tree = ttk.Treeview(frame_datos, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
        self.tree.grid(row=1, column=0, columnspan=6, sticky="nsew")

        ttk.Button(frame_datos, text="Reporte", command=self.mostrar_reporte).grid(row=2, column=0, pady=5)
        ttk.Button(frame_datos, text="Eliminar", command=self.eliminar_registro).grid(row=2, column=1, pady=5)
        ttk.Button(frame_datos, text="Salir", command=self.master.destroy).grid(row=2, column=2, pady=5)

        # Expansión
        frame_datos.rowconfigure(1, weight=1)
        frame_datos.columnconfigure(5, weight=1)

    # --- Funciones auxiliares ---
    def calcular_copago(self, estrato, tipo_atencion):
        estrato = int(estrato)
        if tipo_atencion == "Medicina General":
            valores = {1: 0, 2: 0, 3: 10000, 4: 15000, 5: 20000, 6: 30000}
        else:
            valores = {1: 0, 2: 0, 3: 0, 4: 5000, 5: 10000, 6: 20000}
        return valores.get(estrato, 0)
    
    def actualizar_copago(self, event=None):
        estrato = self.cmb_estrato.get()
        tipo_atencion = self.atencion_var.get()

        if not estrato or not tipo_atencion:
            self.txt_copago.config(state="normal")
            self.txt_copago.delete(0, tk.END)
            self.txt_copago.config(state="readonly")
            return

        copago = self.calcular_copago(estrato, tipo_atencion)
        self.txt_copago.config(state="normal")
        self.txt_copago.delete(0, tk.END)
        self.txt_copago.insert(0, str(copago))
        self.txt_copago.config(state="readonly")


    def registrar_usuario(self):
        try:
            tipo_id = self.cmb_tipoid.get()
            num_id = self.txt_numid.get()
            nombre = self.txt_nombre.get()
            edad = self.txt_edad.get()
            estrato = self.cmb_estrato.get()
            tipo_atencion = self.atencion_var.get()
            fecha = self.txt_fecha.get()

            if not num_id or not nombre or not edad:
                messagebox.showerror("Error", "Por favor complete todos los campos.")
                return

            copago = self.calcular_copago(estrato, tipo_atencion)
            self.txt_copago.config(state="normal")
            self.txt_copago.delete(0, tk.END)
            self.txt_copago.insert(0, str(copago))
            self.txt_copago.config(state="readonly")

            usuario = EstructuraDatosUsuario(tipo_id, num_id, nombre, edad, estrato, tipo_atencion, copago, fecha)

            estructura = self.cmb_estructura.get()
            if estructura == "Pila":
                self.pila.apilar(usuario)
            elif estructura == "Cola":
                self.cola.encolar(usuario)
            else:
                self.lista.agregar(usuario)

            self.mostrar_datos()
            self.limpiar_formulario()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar_formulario(self):
        self.txt_numid.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_edad.delete(0, tk.END)
        self.cmb_estrato.current(0)
        self.cmb_tipoid.current(0)
        self.atencion_var.set("Medicina General")
        self.txt_copago.config(state="normal")
        self.txt_copago.delete(0, tk.END)
        self.txt_copago.config(state="readonly")

    def mostrar_datos(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        estructura = self.cmb_ver.get()
        if estructura == "Pila":
            datos = self.pila.elementos
        elif estructura == "Cola":
            datos = self.cola.elementos
        else:
            datos = self.lista.elementos
        for usuario in datos:
            self.tree.insert("", "end", values=usuario.to_tuple())

    def mostrar_reporte(self):
        estructura = self.cmb_ver.get()
        if estructura == "Pila":
            total = sum(u.valor_copago for u in self.pila.elementos)
            messagebox.showinfo("Reporte Pila", f"Suma total de copagos: ${total:,}")
        elif estructura == "Cola":
            cantidad = len(self.cola.elementos)
            messagebox.showinfo("Reporte Cola", f"Cantidad de registros: {cantidad}")
        else:
            if len(self.lista.elementos) > 0:
                promedio = sum(u.edad for u in self.lista.elementos) / len(self.lista.elementos)
                messagebox.showinfo("Reporte Lista", f"Promedio de edades: {promedio:.2f}")
            else:
                messagebox.showinfo("Reporte Lista", "No hay registros en la lista.")

    from tkinter import messagebox, simpledialog

    def eliminar_registro(self):
        estructura = self.cmb_ver.get()  # obtiene la estructura seleccionada (Pila, Cola o Lista)

        # Confirmar acción
        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Deseas eliminar un registro de la estructura {estructura}?"
        )

        if not confirmar:
            return  # El usuario canceló

        # Pila
        if estructura == "Pila":
            if not self.pila.esta_vacia():
                self.pila.desapilar()
                messagebox.showinfo("Éxito", "Último registro desapilado correctamente.")
            else:
                messagebox.showwarning("Aviso", "La pila está vacía.")

        # Cola
        elif estructura == "Cola":
            if not self.cola.esta_vacia():
                self.cola.desencolar()
                messagebox.showinfo("Éxito", "Primer registro desencolado correctamente.")
            else:
                messagebox.showwarning("Aviso", "La cola está vacía.")

        # Lista
        elif estructura == "Lista":
            identificacion = simpledialog.askstring("Eliminar usuario", "Digite el número de identificación:")

            if not identificacion:
                messagebox.showwarning("Aviso", "Debes digitar un número de identificación.")
                return

            encontrado = False
            for usuario in self.lista.elementos:
                if str(usuario.num_id) == identificacion:
                    self.lista.eliminar(usuario)
                    encontrado = True
                    messagebox.showinfo("Éxito", f"Usuario con ID {identificacion} eliminado correctamente.")
                    break

            if not encontrado:
                messagebox.showerror("Error", f"No se encontró usuario con ID {identificacion}.")

        # Actualiza el Treeview
        self.mostrar_datos()


