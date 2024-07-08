import numpy as np
from tkinter import ttk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graficos():
      def __init__():
         super().__init__()

      @staticmethod
      def create_grafico_line(frame, data, labels, xlabel, ylabel, title, canvas=None, ax=None):
         if canvas and ax:
               # Actualizar los datos del gráfico existente
               ax.clear()
               ax.plot(labels, data, "o-b")
               ax.set_title(title, fontsize=10)
               ax.set_xlabel(xlabel)
               ax.set_ylabel(ylabel)
               canvas.draw()
         else:
               # Crear la figura de matplotlib
               fig = Figure(figsize=(5, 2), dpi=100)
               ax = fig.add_subplot(111)
               ax.plot(labels, data, marker="o", color = "#6698F6")
               ax.set_title(title, fontsize=10)
               ax.set_xlabel(xlabel)
               ax.set_ylabel(ylabel)

               # Crear el canvas de tkinter para la figura de matplotlib
               canvas = FigureCanvasTkAgg(fig, master=frame)
               canvas.draw()
               canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
         return canvas, ax
      
      @staticmethod
      def create_grafico_circular(frame, labels, data, title, title_legend="leyenda", canvas=None, ax=None):
            if canvas and ax:
                  # Actualizar los datos del gráfico existente
                  ax.clear()
                  wedges, texts, autotexts = ax.pie(
                     data, autopct=lambda pct: f"{pct:.1f}%\n({int(np.round(pct / 100. * np.sum(data))):d})",
                     textprops=dict(color="black"), colors=["#6698F6", "#6EE1F8", "#F7FAA3"],
                     wedgeprops={"edgecolor": "white", "linewidth": 1}
                  )
                  ax.legend(wedges, labels, title=title_legend, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
                  ax.set_title(title)
                  canvas.draw()
            else:
                  fig, ax = plt.subplots(figsize=(5, 2), subplot_kw=dict(aspect="equal"), facecolor="white")
                  wedges, texts, autotexts = ax.pie(
                     data, autopct=lambda pct: f"{pct:.1f}%\n({int(np.round(pct / 100. * np.sum(data))):d})",
                     textprops=dict(color="black"), colors=["#6698F6", "#6EE1F8", "#F7FAA3"],
                     wedgeprops={"edgecolor": "white", "linewidth": 1}
                  )
                  ax.legend(wedges, labels, title=title_legend, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
                  ax.set_title(title)
                  canvas = FigureCanvasTkAgg(fig, master=frame)
                  canvas.draw()
                  canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

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
            return canvas, ax

      @staticmethod
      def create_grafico_table(frame, table_columns, table_data, table=None):
         if table:
               # Limpiar la tabla existente y actualizar con los nuevos datos
               for row in table.get_children():
                  table.delete(row)
               for row_data in table_data:
                  table.insert("", "end", values=row_data)
         else:
               table = ttk.Treeview(master=frame, columns=table_columns, show='headings')
               for column in table_columns:
                  table.heading(column, text=column)
                  table.column(column, width=70)
               for row_data in table_data:
                  table.insert("", "end", values=row_data)
               style = ttk.Style()
               style.theme_use('default')
               style.configure("Treeview.Heading", background="#6E72F5", fieldbackground="#6E72F5", foreground="white")
               style.map('Treeview', background=[("selected", "#6E72F5")])
               table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
         return table            
          
