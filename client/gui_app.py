import tkinter as tk
import tkinter as tk
from tkinter import ttk
from db_connection import obtener_datos

class Frame(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config( bg = 'green')
        self.crear_widgets()

    def crear_widgets(self):
        self.tree = ttk.Treeview(self, columns=("ID", "DNI", "NOMBRE", "TIPO_HORARIO", "TIPO_CONTRATO", 
                                                "FECHA_INGRESO", "ACTIVO", "FECHA_CESE", "NOMBRE_SEDE", 
                                                "EMAIL", "NUMERO_CONTACT"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("DNI", text="DNI")
        self.tree.heading("NOMBRE", text="NOMBRE")
        self.tree.heading("TIPO_HORARIO", text="TIPO_HORARIO")
        self.tree.heading("TIPO_CONTRATO", text="TIPO_CONTRATO")
        self.tree.heading("FECHA_INGRESO", text="FECHA_INGRESO")
        self.tree.heading("ACTIVO", text="ACTIVO")
        self.tree.heading("FECHA_CESE", text="FECHA_CESE")
        self.tree.heading("NOMBRE_SEDE", text="NOMBRE_SEDE")
        self.tree.heading("EMAIL", text="EMAIL")
        self.tree.heading("NUMERO_CONTACT", text="NUMERO_CONTACT")

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Entrada para el nombre del procedimiento almacenado
        self.procedimiento_var = tk.StringVar()
        self.entrada_procedimiento = tk.Entry(self, textvariable=self.procedimiento_var)
        self.entrada_procedimiento.pack(pady=10)

        # Botón para cargar datos
        self.boton_cargar = tk.Button(self, text="Cargar Datos", command=self.cargar_datos)
        self.boton_cargar.pack(pady=10)

    def cargar_datos(self):
        procedimiento = self.procedimiento_var.get()
        datos = obtener_datos(procedimiento)
        for fila in datos:
            self.tree.insert("", tk.END, values=fila)