import numpy as np
from tkinter import Tk, ttk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graficos():
      def __init__():
         super().__init__()

      def create_grafico_barras(frame):
         # Datos de ejemplo - reemplaza esto con la consulta a la base de datos
         periodos = ['012024', '022024', '032024', '042024', '052024']
         montos = [1000, 1500, 2000, 2500, 3000]

         # Crear la figura de matplotlib
         fig = Figure(figsize=(2, 2), dpi=111)
         ax = fig.add_subplot(111)
         ax.plot(periodos, montos)

         ax.set_xlabel('PERIODO', fontsize=1)
         ax.set_ylabel('MONTO',fontsize=1)
         ax.set_title('Monto por Periodo',fontsize=10)

         # Crear el canvas de tkinter para la figura de matplotlib
         canvas = FigureCanvasTkAgg(fig, master=frame)
         canvas.draw()
         canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


      def create_grafico_circular(frame, labels, data):
         plt.style.use('_mpl-gallery-nogrid')

         
         
         colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(data)))

         # plot
         fig, ax = plt.subplots()
         ax.pie(data,labels=labels, colors=colors, radius=3, center=(4, 4),
               wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

         ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
               ylim=(0, 8), yticks=np.arange(1, 8))

         canvas = FigureCanvasTkAgg(fig, master=frame)
         canvas.draw()
         canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)






      def create_grafico_table(frame, table_columns, table_data):
         table = ttk.Treeview(master=frame, columns=table_columns, show ='headings')

         for column in table_columns:
            table.heading(column=column, text=column)
            table.column(column=column,width=70)
         if len(table_data) > 0:
            for row_data in table_data:
               table.insert(parent="",index="end", values=row_data)
         else:
            table.insert(parent="",index="end", values="No hay data que mostrar")

         style = ttk.Style()
         style.theme_use('default')
         style.configure("Treeview", background="#917FB3", fieldbackground="#917FB3", foreground ="white")
         style.configure("Treeview.heading", background="#917FB3", fieldbackground="#917FB3", foreground ="white")
         style.map('Treeview', background=[("selected","#E5BEEC")])
         table.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
            
          
