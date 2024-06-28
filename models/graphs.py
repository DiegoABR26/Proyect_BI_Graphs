import numpy as np
from tkinter import ttk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graficos():
      def __init__():
         super().__init__()

      def create_grafico_barras(frame,data,labels,xlabel,ylabel,title):
         # Datos de ejemplo - reemplaza esto con la consulta a la base de datos
         #periodos = ['012024', '022024', '032024', '042024', '052024']
         #montos = [1000, 1500, 2000, 2500, 3000]

         # Crear la figura de matplotlib
         fig = Figure(figsize=(2, 2), dpi=111)
         ax = fig.add_subplot(111)
         ax.plot(labels, data)

         ax.set_xlabel('{}'.format(xlabel), fontsize=1)
         ax.set_ylabel('{}'.format(ylabel),fontsize=1)
         ax.set_title('{}'.format(title),fontsize=10)

         # Crear el canvas de tkinter para la figura de matplotlib
         canvas = FigureCanvasTkAgg(fig, master=frame)
         canvas.draw()
         canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
 

      def create_grafico_circular(frame, labels, data,title,title_legend="leyenda",tipo=1):
         fig, ax = plt.subplots(figsize=(5, 3), subplot_kw=dict(aspect="equal"), facecolor="white")
         
         colors = ["#6698F6", "#6EE1F8", "#F7FAA3"]
         wedgeprops = {"edgecolor": "white", "linewidth":1}

         wedges, texts, autotexts = ax.pie(data, 
                                          autopct=lambda pct: f"{pct:.1f}%\n({int(np.round(pct / 100. * np.sum(data))):d})",
                                          textprops=dict(color="black"),
                                          colors=colors,
                                          wedgeprops=wedgeprops)
         
         ax.legend(wedges, labels, title="{}".format(title_legend), loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
         plt.setp(autotexts, size=8, weight="bold")
         ax.set_title("{}".format(title))

         if tipo == 2:
             plt.show()
         
         if tipo == 1:
            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            
            def on_hover(event):
               hovered = False
               for i, wedge in enumerate(wedges):
                     if wedge.contains_point([event.x, event.y]):
                        angle = (wedge.theta2 + wedge.theta1) / 2  # Calculate the middle angle of the wedge
                        x_offset = 0.1 * np.cos(np.deg2rad(angle))  # Calculate the x offset
                        y_offset = 0.1 * np.sin(np.deg2rad(angle))  # Calculate the y offset
                        wedge.set_center((x_offset, y_offset))  # Move the wedge center
                        wedge.set_radius(1.1)  # Highlight the hovered wedge by moving it outwards
                        autotexts[i].set_fontsize(12)  # Increase the font size of the text
                        canvas.draw()
                        hovered = True
                     else:
                        wedge.set_radius(1.0)  # Reset all wedges to their original position
                        wedge.set_center((0, 0))  # Reset center to original position
                        autotexts[i].set_fontsize(8)  # Reset font size of the text
               if not hovered:
                     for autotext in autotexts:
                        autotext.set_fontsize(8)  # Ensure all text is reset to normal size if not hovered
                     canvas.draw()

            canvas.mpl_connect("motion_notify_event", on_hover)


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
         #style.configure("Treeview", background="white", fieldbackground="white", foreground ="black")
         style.configure("Treeview.Heading", background="#6E72F5", fieldbackground="#6E72F5", foreground ="white")
         style.map('Treeview', background=[("selected","#6E72F5")])
         table.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
            
          
