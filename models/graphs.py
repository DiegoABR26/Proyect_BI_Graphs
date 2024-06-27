import numpy as np
from tkinter import Tk, ttk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mplcursors


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
         fig, ax = plt.subplots(figsize=(5,3), subplot_kw=dict(aspect="equal"), facecolor="#917FB3")

         colors = ["#9ec4bb","#ccccbb","#eed7c5"]

         wedges, texts, autotexts= ax.pie(data, 
                                           autopct = lambda pct:f"{pct:.1f}%\n({int(np.round(pct/100.*np.sum(data))):d}",
                                          textprops = dict(color="black"),
                                          colors=colors,
                                          )
         ax.legend(
                  wedges, labels,
                  title="Estados",
                  loc="center left",
                  bbox_to_anchor=(1,0,0.5,1))
         plt.setp(autotexts, size = 8, weight = "bold")
         ax.set_title("Trabajadores Pagados por Periodo")

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
            
          
