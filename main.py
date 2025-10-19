# main.py
import tkinter as tk
from tkinter import messagebox
from formulario import VentanaPrincipal

class LoginApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login - Salvando Vidas")
        self.root.geometry("360x200")
        self.root.resizable(False, False)

        # Fuente base
        fuente = ("Segoe UI", 11)

        # Etiqueta "Contraseña:"
        tk.Label(self.root, text="Contraseña:", font=fuente).pack(pady=(25, 6))

        # Campo de entrada
        self.entry = tk.Entry(self.root, show="*", font=fuente, width=22, justify="center")
        self.entry.pack(pady=6)

        # Botones centrados
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=12)

        tk.Button(btn_frame, text="Ingresar", command=self.verificar, width=10, font=("Segoe UI", 10)).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Salir", command=self.root.destroy, width=10, font=("Segoe UI", 10)).grid(row=0, column=1, padx=5)

        # Botón "Acerca de" arriba a la izquierda
        tk.Button(self.root, text="Acerca de", command=self.mostrar_info, font=("Segoe UI", 9)).place(x=10, y=8)

        # Evento Enter
        self.entry.bind("<Return>", lambda e: self.verificar())

        self.root.mainloop()

    def verificar(self):
        if self.entry.get() == "unad":
            self.root.destroy()
            nueva_ventana = tk.Tk()
            VentanaPrincipal(nueva_ventana)
            nueva_ventana.mainloop()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")

    def mostrar_info(self):
        messagebox.showinfo(
            "Acerca de",
            "EPS Salvando Vidas\n"
            "Curso: Estructura de Datos\n"
            "Estudiante: Carlos Andrés Mena Vargas\n"
            "Grupo: 301305_56"
        )

if __name__ == "__main__":
    LoginApp()
